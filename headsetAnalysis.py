#processes events as they come in
from PyEpoc import EpocHandler, ERRCODE

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

x = EpocHandler()

print x.EE_EngineConnect()

event = x.EE_EmoEngineEventCreate()
#state = x.EE_EmoStateCreate()

sumTup = (0,0)
numLoop = 0


while 1:
	state = x.EE_EngineGetNextEvent(event)
	# if state == ERRCODE.EDK_OK :
		# etype = x.EE_EmoEngineEventGetType(event)
		


	test = x.EE_HeadsetGetGyroDelta(0) 
	
	sumTup = (sumTup[0] + test[1][0] ,sumTup[1] + test[1][1])



	numLoop += 1

	if numLoop >= 10:
		sumTup = (sumTup[0] / numLoop, sumTup[1] / numLoop)

		processGyroData(sumTup)
		sumTup = (0,0)
		numLoop = 0

	


# x.EE_EngineDisconnect()