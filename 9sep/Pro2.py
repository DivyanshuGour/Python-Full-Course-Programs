from threading import Thread
import time

class Sample(Thread):
	def __init__(self,title):
		super().__init__()
		self.title = title
	def run(self):
		self.process()
	def process(self):
		for x in range(1,11):
			print(self.title," : ",x)
			time.sleep(0.5)

ob1 = Sample('Vikas')
ob2 = Sample('Mohan')
ob3 = Sample('Meena')

ob1.start()
ob2.start()
ob3.start()

"""
	Runnable
				Running
		
				Waiting
	Dead

"""




