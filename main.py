from epocInterface import EpocInterface

def write_file_generator(file_id):
	def write_file(str_out):
		line = "{0} {1}\n".format(str_out[0],str_out[1])
		file_id.write(line);

	return write_file


file_id = open('down.txt','w')
interface = EpocInterface(write_file_generator(file_id))
# interface = EpocInterface()
# interface.connect()
interface.run()
file_id.close()

