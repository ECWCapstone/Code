#processes events as they come in
from PyEpoc import EpocHandler, ERRCODE
import multiprocessing as mp
import threading
import time
from emotiv import Epoc

class EpocInterface:

	def print_me(data, gyros, times):
		print (data, gyros, times) 

	def __init__(self, funct=print_me):
		self.handler_funct = funct

	def connect(self):
		return self.e_handler.EE_EngineConnect()

	@staticmethod
	def run(funct):
		epoc = Epoc()
		print 'Connected'
		while True:
			epoc.get_all()
			gyros = epoc.gyros
			data = epoc.raw
			times = epoc.times
			funct(data, gyros, times)
			time.sleep(.03)

	def start(self):
		# threading.Thread(target=self.run, args=(self.handler_funct,)).start()
		# thread.start_new_thread(self.run(self.handler_funct))
		p = mp.Process(target=self.run, args=(self.handler_funct,))
		p.start()
		# return p

