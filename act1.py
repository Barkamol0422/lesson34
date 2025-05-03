class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a<other.a:
            return "obj1 is lesser than obj2"
        else:
            return "obj1 is not lesser than obj2"
    def __eq__(self,other):
        if self.a==other.a:
            return "obj1 is equal to obj2"
        else:
            return "obj1 is not equal to obj2"
p1=A(3)
p2=A(3)
print(p1<p2)
p3=A(3)
p4=A(3)
print(p3==p4)
