#processes events as they come in
from PyEpoc import EpocHandler, ERRCODE

#consumer function
def processGyroData(tup):
	Directions = []

	if tup[0] < 0:
		 Directions.append("left")

	if tup[0] > 0: 
		Directions.append("right")

	if tup[1] < 0: 
		Directions.append("down")

	if tup[1] > 0:
		Directions.append("up")

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
		sumTup = (sumTup[0]/10, sumTup[1]/10)

		processGyroData(sumTup)
		sumTup = (0,0)
		numLoop = 0

	


# x.EE_EngineDisconnect()