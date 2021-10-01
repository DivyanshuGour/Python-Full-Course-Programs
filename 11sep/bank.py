from threading import Thread
from threading import Lock

lock = Lock()
class BankAccount:
	def __init__(self,balance):
		self.balance = balance
	def withdraw(self,amount): # t1:10000,t2:60000,t3:40000
		lock.acquire()
		if self.balance >=  amount:
			old = 	self.balance
			self.balance -= amount
			print("Withdraw Done : ",amount,", Old : ",old," , Current Balance : ",self.balance)
		else:
			print("Withdraw Failed : ",amount," Current Balance : ",self.balance)	
		lock.release()


class Transaction(Thread):
	def __init__(self,account,amount):
		super().__init__()
		self.account = account
		self.amount = amount
	def run(self):	
		self.account.withdraw(self.amount)






