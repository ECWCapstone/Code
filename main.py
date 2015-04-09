from epocInterface import EpocInterface
import ardrone
import time

import sys, tty, termios



##############################################################################################################
### WTF python, Really?
##############################################################################################################
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def write_file_generator(file_id):
	def write_file(str_out):
		line = "{0} {1}\n".format(str_out[0],str_out[1])
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


class state:
	x = 0
	y = 0
	count = 0
	count_final = 75    # using "time python main.py" it was 11.2359 samples per ms And the drone samples every 3 ms  therefore 33 samples is good
						# or not?
	def add_x(self,newX):
		self.x = newX + self.x

	def add_y(self,newY):
		self.y = newY + self.y

	def inc_count(self):
		self.count = self.count + 1

	def zero_count(self):
		self.count = 0

def write_copter(copter, stat):
	def fly_copter(tup):
		coords = {"x": tup[0], "y": tup[1]}

		if abs(coords['x'])< 5 and abs(coords['y'])<5:
			stat.inc_count()
			return
		stat.add_x(coords['x'])
		stat.add_y(coords['y'])
		stat.inc_count()



		if stat.count >= stat.count_final:
			sumDirect = float(abs(stat.x) + abs(stat.y))
			if sumDirect ==0:
				return

			percentX = abs(stat.x / sumDirect)
			percentY = abs(stat.y / sumDirect)

			#simplified threshold for x and y
			
			if percentX > 0.25 and percentX > percentY:
				if coords['x'] > 0:
					print 'right'
					copter.right()
				else:
					print 'left'
					copter.left()

			elif percentY > 0.25:
				if coords['y'] > 0:
					print 'up'
					copter.up()
				else:
					print 'down'
					copter.down()
			stat.zero_count()
	return fly_copter

### 
# Drone
###

drone = ardrone.ARDrone()
drone.setup()
drone.flat_trims()
time.sleep(3)
print 'drone set'
drone.set_speed(.1)

interface = EpocInterface(write_copter(drone,state()))
interface.run()
print 'main is in control'

while True:

	try: 
		cmd = getch()

		if ord(cmd) == 3:# looking for ctrl + c
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
		elif cmd == 'k':
			drone.down()
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
#file_id = open('down.txt','w')
# interface = EpocInterface(write_file_generator(file_id))
#file_id.close()

###
# Simple print
###
# interface = EpocInterface()

###
# counter
###

# interface = EpocInterface(write_count_func(counter()))
# interface.run()