from epocInterface import EpocInterface

interface = EpocInterface()

interface.connect()#connect to headset

event = interface.e_handler.EE_EmoEngineEventCreate()
#state = x.EE_EmoStateCreate()
#creates new event from headset

sumTup = (0,0)
numLoop = 0 #count of how many tupples sampled


while 1:
	state = interface.e_handler.EE_EngineGetNextEvent(event)
	# if state == ERRCODE.EDK_OK :
		# etype = x.EE_EmoEngineEventGetType(event)
		#updataing state and getting a new event
		


	test = interface.e_handler.EE_HeadsetGetGyroDelta(0) 
	
	sumTup = (sumTup[0] + test[1][0] ,sumTup[1] + test[1][1])
	#summing toop get back with previous tupples
	#taking first delta x and adding it to the next
	#taking first delta y and addint it to the next
	#this repeats similar to a sum



	numLoop += 1 #incrementing loop

	if numLoop >= 10:
		sumTup = (sumTup[0] / numLoop, sumTup[1] / numLoop)
		#on the 10th loop will take average of sum

		interface.processGyroData(sumTup)
		#sending data to processGyroData command
		sumTup = (0,0)
		numLoop = 0
		#tells us average of command was a right, left, up, or down
