import struct
import socket
import signal

import multiprocessing as mp
import time

# 5556 send
# 5554 receive navdata
CTRL_PORT = 5556
STATUS_PORT = 5554

class ARDrone:
	def __init__(self,IP_ADDRESS="192.168.1.1"):

		self.cmd_queue = mp.Queue()
		self.processes = []
		self.speed = 0.5

		self.ip_address = IP_ADDRESS;
		self.ctrl_socket = socket.socket()
		self.status_socket = socket.socket()
		self.is_flying = mp.Value('b', False)
		self.is_emergency_mode = mp.Value('b', False)


	def setup(self):
		self.ctrl_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.status_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.status_socket.bind(('', STATUS_PORT))
		self.status_socket.sendto("\x01\x00\x00\x00", (self.ip_address, STATUS_PORT))
		
		p = mp.Process(target=self.send_from_queue, args=(self.cmd_queue,))  # Queue dispatch thread 
		p2 = mp.Process(target=self.update_navdata, args=(self.is_flying,self.is_emergency_mode))  # Nav data listener thread

		self.processes.append(p)
		self.processes.append(p2)
		p.start()
		p2.start()

		self.reset_alarm()
		self.hover()	

	def reset_alarm(self):
		signal.signal(signal.SIGALRM, self.send_hover)
		signal.setitimer(signal.ITIMER_REAL, 1.8)
		

	def __set_navdata(self,flying,emergency_mode):
		drone_info = dict()
 		data = self.status_socket.recv(65535)
		navdata = struct.unpack_from("IIII", data, 0)

		flying = navdata[1] & 1 == 1
		emergency_mode = navdata[1] & 0x80000000 == 1

	def flat_trims(self):    # Levels the trim for flight !!! Must be on the ground, level!!!
		self.enqueue_cmd("FTRIM", "")

	def take_off(self):
		take_off_int = 0b10001010101000000001000000000
		self.enqueue_cmd("REF", (",%d" % take_off_int))

	def land(self):
		land_int = 0b10001010101000000000000000000
		self.enqueue_cmd("REF", (",%d" % land_int))
		

	def emergency_stop(self):
		stop_int = 0b10001010101000000000100000000
		self.enqueue_cmd("REF", (",%d" % stop_int))

	def right(self): 
		self.enqueue_cmd("PCMD", self.movement_cmd(self.speed,0,0,0))

	def left(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(-self.speed,0,0,0))
		
	def up(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(0,0,self.speed,0))

	def down(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(0,0,-self.speed,0))

	def backward(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(0,self.speed,0,0))		

	def forward(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(0,-self.speed,0,0))

	def rotate_right(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(0,0,0,self.speed))

	def rotate_left(self):
		self.enqueue_cmd("PCMD", self.movement_cmd(0,0,0,-self.speed))

	def hover(self):
		self.enqueue_cmd("PCMD", ",0,0,0,0,0")

	def set_speed(self,f):
		if is_valid_speed(f):
			self.speed = f
		else: 
			print ("Speed not valid, should range from 0 to 1, input was %f", f)

	def send_hover(self, signum, frame):
		self.hover()
		
	def enqueue_cmd(self, cmd_name, args):
		cmd_tup = (cmd_name, args)
		self.cmd_queue.put(cmd_tup)

	def send_ctrl_cmd(self,msg):
		self.ctrl_socket.sendto(msg, (self.ip_address,CTRL_PORT))

	def movement_cmd(self, right,foward,up,spin):
		return (",%i,%i,%i,%i,%i" % (1,f2i(float(right)),f2i(float(foward)),f2i(float(up)),f2i(float(spin))))		

	def send_from_queue(self,queue):
		sequence_nbr = 1;
		while True:
			if not queue.empty():
				cmd_tup = queue.get()
				msg = "AT*%s=%i%s\r" % (cmd_tup[0],sequence_nbr,cmd_tup[1])
				sequence_nbr += 1
				self.send_ctrl_cmd(msg)
				self.reset_alarm()
				time.sleep(.03)
			

	def update_navdata(self,flying,emergency_mode):
		while True:
			self.__set_navdata(flying,emergency_mode)
			time.sleep(.25)

	def disconect(self):

		self.processes[0].terminate()
		self.processes[1].terminate()
		self.processes[0].join()
		self.processes[1].join()
		self.ctrl_socket.close()
		self.status_socket.close()
	
def is_valid_speed(speed):
	return 0 <= speed <= 1

def f2i(flo):
	return struct.unpack('i',struct.pack('f',flo))[0]