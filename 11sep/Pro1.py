from bank import BankAccount,Transaction

act = BankAccount(100000)

t1 = Transaction(act,5000)
t2 = Transaction(act,45000)
t3 = Transaction(act,2000)
t4 = Transaction(act,15000)
t5 = Transaction(act,10000)
t6 = Transaction(act,5000)
t7 = Transaction(act,45000)
t8 = Transaction(act,2000)
t9 = Transaction(act,15000)
t10 = Transaction(act,10000)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
