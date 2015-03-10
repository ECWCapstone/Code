#processes events as they come in
from PyEpoc import EpocHandler, ERRCODE
import threading
import time

class EpocInterface:

	def print_me(str_input):
		print str_input

	def __init__(self, funct=print_me):
		# self.e_handler = EpocHandler()
		self.handler_funct = funct

	def connect(self):
		return self.e_handler.EE_EngineConnect()

	def sample_gyro_data():
		engine = EpocHandler()
		print engine.EE_EngineConnect()

		new_event = engine.EE_EmoEngineEventCreate()

		while True:
			state = engine.EE_EngineGetNextEvent(new_event)
			gyro_data = engine.EE_HeadsetGetGyroDelta(0)
			self.handler_funct(gyro_data[1])

	def run(self):
		threading.Thread(target=sample_gyro_data).start()

	
			


	#consumer function
	#directions processed by headset represented in tupples
	#each tupple represents (x,y) where:(x,y) = ((left/right,up/down) = ((horizontal,vertical))
	#each direction pair, horizontal or vertical holds magnitude of change in its direction
	#coords is a hash table where X: delta(X), and Y:delta(Y)
	#overall: returns percentage of each change in direction while ignoring values under 25%

	def processGyroData(self,tup):
		coords = {"x": tup[0], "y": tup[1]}
		Directions = [] #array that holds directions
		sumDirect = float(abs(coords['x']) + abs(coords['y']))

		if sumDirect ==0:
			return

		percentX = abs(coords['x'] / sumDirect)
		percentY = abs(coords['y'] / sumDirect)

		#simplified threshold for x and y
		if percentX > 0.25:
			if coords['x'] > 0:
				Directions.append("right-{0:.2f}".format(percentX))
			else:
				Directions.append("left-{0:.2f}".format(percentX))

		if percentY > 0.25:
			if coords['y'] > 0:
				Directions.append("up-{0:.2f}".format(percentY))
			else:
				Directions.append("down-{0:.2f}".format(percentY))

				#append the direction to the directions array

		if len(Directions) > 0:

			print ", ".join(Directions)

			# appending two strings together 
			# each string has the direction and percentage of change
			# ["right" -.30, up-.70]
			

