class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return"Ob1 is smaller than Obj2"
        else:
            return'obj 2 is smaller than ob1'
    def __eq__(self, other):
        if(self.a==other.a):
            return'Objs are euqal'
        else:
            return'not euqal'
Obj1 =A(3)
Obj2 =A(4)
print("Passed value",Obj1.a, Obj2.a)
print(Obj1 < Obj2)
Obj3 =A(4)
Obj4 =A(4)
print("Passed value",Obj3.a, Obj4.a)
print(Obj3 == Obj4)