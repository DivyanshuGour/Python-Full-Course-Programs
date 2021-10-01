# Data Mangling
class A:
    def __init__(self):
        self.__x = 10 # _A__x
    def show(self):
        print("A : ",self.__x)        

class B(A):
    def __init__(self):
        super().__init__()
        self.__x = 20 # _B__x
    def show(self):
        super().show()
        print("B : ",self.__x)                

ob = B()
#print(ob.__x)
print(ob.__dict__)


