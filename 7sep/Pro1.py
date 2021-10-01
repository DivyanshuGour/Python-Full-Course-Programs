from abc import ABC , abstractmethod

class A(ABC):
    def fun1(self):
        print("A's Fun1 ....")
    @abstractmethod    
    def fun2(self):
        pass        

class B(A):
    def hello(self):
        print("B's Hello ....")
    def fun2(self):
        print("B's Fun2 ....")        

class C(A):
    pass

ob = C()

ob.fun1()
ob.hello()
ob.fun2()