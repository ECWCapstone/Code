from epocInterface import EpocInterface
import ../drone/Drone/ardrone  

def write_file_generator(file_id):
	def write_file(str_out):
		line = "{0} {1}\n".format(str_out[0],str_out[1])
		file_id.write(line);

	return write_file

def write_copter(copter):
	def fly_copter(tup):
		coords = {"x": tup[0], "y": tup[1]}
		Directions = [] #array that holds directions
		sumDirect = float(abs(coords['x']) + abs(coords['y']))

		if sumDirect ==0:
			return

		percentX = abs(coords['x'] / sumDirect)
		percentY = abs(coords['y'] / sumDirect)

		#simplified threshold for x and y
		if percentX > 0.25 and percentX > percentY:
			if coords['x'] > 0:
				copter.right()
			else:
				copter.left()

		else if percentY > 0.25:
			if coords['y'] > 0:
				copter.up()
			else:
				copter.down()


#file_id = open('down.txt','w')
drone = ardrone.ARDrone()
drone.setup()
drone.flat_trims()
time.sleep(3)
print 'drone set'
drone.set_speed(25)
# interface = EpocInterface(write_file_generator(file_id))
# interface = EpocInterface()
interface = EpocInterface(write_copter(drone))
# interface.connect()
interface.run()
#file_id.close()
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

