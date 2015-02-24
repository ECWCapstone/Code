#processes events as they come in
from PyEpoc import EpocHandler, ERRCODE


class EpocInterface:

	def __init__(self):
		e_handler = EpocHandler()

	def connect(self):
		print e_handler.EE_EngineConnect()

	#consumer function
	def processGyroData(tup):
		coords = {"x": tup[0], "y": tup[1]}
		Directions = []
		sumDirect = float(abs(coords['x']) + abs(coords['y']))

		if sumDirect ==0:
			return

		percentX = abs(coords['x'] / sumDirect)
		percentY = abs(coords['y'] / sumDirect)

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

		if len(Directions) > 0:

			print ", ".join(Directions)
