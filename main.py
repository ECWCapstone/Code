from epocInterface import EpocInterface
import ardrone
import time
from emotiv import Epoc
from fake_drone import FakeDrone
import numpy

import sys, tty, termios



##############################################################################################################
### WTF python, Really?
##############################################################################################################
# def getch():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch


def write_file_generator(file_id):
	def write_file(str_out):
		line = "{0} {1} {2} {3}\n".format(str_out[0],str_out[1],str_out[2],str_out[3])
		file_id.write(line);

	return write_file

def write_count_func(counter_class):
	def counter(tup):
		counter_class.up()
		if counter_class.value == 100000:
			print 'made it to 100000'
			quit()
	return counter

class counter:
	value = 0

	def up(self):
		self.value = self.value + 1


class State:
	x = 0
	y = 0
	totalX = 0
	totalY = 0

	prevTime = 0

	alternate_flying_mode = False

	def add_x(self,newX):
		self.x = newX + self.x

	def add_y(self,newY):
		self.y = newY + self.y

	def start_new_window(self):
		self.totalX += self.x
		self.totalY += self.y
		self.x = 0
		self.y = 0

	def reset(self):
		self.totalX = 0
		self.totalY = 0


def write_copter(copter):
	stat = State()

	def low_pass_filter(data, times, cut_off, prevTime):		
		prev = 0
		data_out = [0] * len(data)


		for i in range (0,len(data)):
			x = data[i]
			dt = times[i] - prevTime
			prevTime = times[i]
			alpha = dt / (cut_off + dt) 
			yi = alpha * x + (1 -alpha) * prev
			data_out[i] = yi
			prev = yi

		return data_out


	def fly_copter(data, gyros, times):
		gyros[0] = low_pass_filter(map(lambda x: x - 1702.66, gyros[0]), times, 4, stat.prevTime)
		gyros[1] = low_pass_filter(map(lambda x: x - 1677.6, gyros[1]), times, 4, stat.prevTime)
		stat.prevTime = times[-1]

		max_af3 = max(data[0])
		

		max_af4 = max(data[-1])
		

		max_f3 = max(data[2])

		max_f4 = max(data[-3])

		max_overal =  max(max_af3, max_af4, max_f3, max_f4))

		if max_overal > 6000:
			if max_overal == max_af3:			
				print "Reset dead zone"
				stat.reset()

			elif max_overal == max_af4:
				print "Toggle Take off"
				drone.toggle_flying()

			elif max_overal == max_f3:
				print "Alt Fling mode"
				stat.alternate_flying_mode = not stat.alternate_flying_mode

			else:
				pass

		if m > 6000:
			print "Toggling flying state"
			drone.toggle_flying()
			return
		# print gyros

		for i in range(0, len(times)):
			x, y = (gyros[0][i], gyros[1][i])
			stat.add_x(x)
			stat.add_y(y)
			


		stat.start_new_window()

		windowX = 50
		windowY = 30
		
		directions = {
			"up": False,
			"down": False,
			"left": False,
			"right": False
		}

		direction = 'stop'

		if stat.totalX < -windowX:
			directions["right"] = True
			direction = "right"
			stat.totalY = 0
		elif stat.totalX > windowX:
			directions["left"] = True
			direction = "left"
			stat.totalY = 0


		if stat.totalY < -windowY:
			directions["up"] = True
			direction = "up"
			stat.totalX = 0
		elif stat.totalY > windowY:
			directions["down"] = True
			direction = "down"
			stat.totalX = 0

		if directions["up"]:
			copter.up()
		elif directions["down"]:
			copter.down()
		elif directions["left"]:
			copter.left()
		elif directions["right"]:
			copter.right()

		print str.format('{0} {1} {2}', direction, stat.totalX, stat.totalY)

	return fly_copter

###
# Pyemotiv Goodness
###

# epoc = Epoc()
# while True:
#     gyros = epoc.get_gyros() #2-by-n-row array containing data for GYROX and GYROY
#     times = epoc.times #1d array containing timestamp values (interpolated)
#     # everything = epoc.all_data # 25-by-n array containing all data returned by emotiv
#     # data = epoc.get_raw()
#     print gyros

### 
# Drone
###

drone = ardrone.ARDrone()
drone.setup()
drone.flat_trims()
time.sleep(3)
print 'drone set'
drone.set_speed(.1)

# drone = FakeDrone()

interface = EpocInterface(write_copter(drone))
# interface = EpocInterface()
interface.start()


# # print 'main is in control'

while True:

	try: 
		cmd = raw_input()
		if ord(cmd) == 3:# looking for ctrl + c
			drone.land()
			drone.disconect()
			sys.exit(0)

		
		if cmd == 'g':
			drone.land()
		elif cmd == 't':
			print "Taking off"
			drone.take_off()
		elif cmd == 'a':
			drone.left()
		elif cmd == 'd':
			drone.right()
		elif cmd =='w':
			drone.forward()
		elif cmd == 's':
			drone.backward() 
		elif cmd == 'i':
			drone.up()
		elif cmd == 'u':
			drone.up_left()
		elif cmd == 'o':
			drone.up_right()
		elif cmd == 'k':
			drone.down()
		elif cmd == 'm':
			drone.down_left()
		elif cmd == '.':
			drone.down_right()
		elif cmd == 'j':
			drone.rotate_left()
		elif cmd == 'l':
			drone.rotate_right()
		elif cmd == 'e':
			drone.emergency_stop() 
		else:
			pass
	except Exception as e:
		print type(e)
		print e.message           
		print "It was Will's fault"



###
# File write
###
# file_id = open('sample.txt','w')
# interface = EpocInterface(write_file_generator(file_id))
# interface.start()
# file_id.close()

###
# Simple print
###
def pitch_print(arr_arr):
	print arr_arr[1]

# interface = EpocInterface(pitch_print)
# interface.start()
 
def print_XY(arr_arr):
	for i in range(0,4):
		print str.format('{0} {1}',arr_arr[0][i],arr_arr[1][i] )

# interface = EpocInterface(print_XY)
# interface = EpocInterface()
# interface.start()




###
# counter
###

# interface = EpocInterface(write_count_func(counter()))
# interface.start()