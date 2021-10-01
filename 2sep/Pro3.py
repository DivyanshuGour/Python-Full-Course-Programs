class A:
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b
    def show(self):
        print("\nA : ",self.a," B : ",self.b)        

class X(A):
    def __init__(self,x=0,y=0,a=0,b=0):
        super().__init__(a,b)
        self.x = x
        self.y = y
    def show(self):
        super().show()
        print("X : ",self.x," Y : ",self.y)        

ob1 = X(44,21,55,76)
ob2 = X(4,1,6)
ob3  = X(a=34,y=11)
ob4 = X(66,b=55)

ob1.show()
ob2.show()
ob3.show()
ob4.show()


"""
    State
        Behaviour
            Identity
"""
















