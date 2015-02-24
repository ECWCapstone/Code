from epocInterface import EpocInterface

interface = EpocInterface()

interface.connect()

event = interface.e_handler.EE_EmoEngineEventCreate()
#state = x.EE_EmoStateCreate()

sumTup = (0,0)
numLoop = 0


while 1:
	state = interface.e_handler.EE_EngineGetNextEvent(event)
	# if state == ERRCODE.EDK_OK :
		# etype = x.EE_EmoEngineEventGetType(event)
		


	test = interface.e_handler.EE_HeadsetGetGyroDelta(0) 
	
	sumTup = (sumTup[0] + test[1][0] ,sumTup[1] + test[1][1])



	numLoop += 1

	if numLoop >= 10:
		sumTup = (sumTup[0] / numLoop, sumTup[1] / numLoop)

		interface.processGyroData(sumTup)
		sumTup = (0,0)
		numLoop = 0
