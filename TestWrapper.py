from PyEpoc import EpocHandler, ERRCODE

x = EpocHandler()

print x.EE_EngineConnect()

event = x.EE_EmoEngineEventCreate()
#state = x.EE_EmoStateCreate()

while 1:
	state = x.EE_EngineGetNextEvent(event)
	# if state == ERRCODE.EDK_OK :
		# etype = x.EE_EmoEngineEventGetType(event)
		
	test = x.EE_HeadsetGetGyroDelta(0) 
		
	if not (test[1][0] == 0 and test[1][1] == 0):
		print test


# x.EE_EngineDisconnect()