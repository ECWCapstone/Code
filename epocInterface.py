#processes events as they come in
from PyEpoc import EpocHandler, ERRCODE


class EpocInterface:

	def __init__(self):
		e_handler = EpocHandler()

	def connect(self):
		print e_handler.EE_EngineConnect()

	#consumer function
	#directions processed by headset represented in tupples
	#each tupple represents (x,y) where:(x,y) = ((left/right,up/down) = ((horizontal,vertical))
	#each direction pair, horizontal or vertical holds magnitude of change in its direction
	#coords is a hash table where X: delta(X), and Y:delta(Y)
	#overall: returns percentage of each change in direction while ignoring values under 25%

	def processGyroData(tup):
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
			

