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

ob = X(44,21,55,76)
ob.show()