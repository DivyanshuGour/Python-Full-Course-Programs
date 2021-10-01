# Parent
class A:
    def fun1(self):
        print("A's Fun1 ..... ")
    def fun2(self):
        print("A's Fun2 ..... ")        
    def fun3(self):
        print("A's Fun3 ..... ")         

# Child
class B(A):
    def hello(self):
        print("B's Hello ....")  
    def fun2(self):
        print("B's Fun2 ..... ")   
    def fun3(self):
        super().fun3()
        print("B's Fun3 ....")         


ob = B()
ob.hello() # own function
ob.fun1() # inherited function
ob.fun2() # Override Function
ob.fun3()  # Override Function