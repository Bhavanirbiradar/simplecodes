class employee:
    def __init__(self,name,dept,sal):
        self.name=name
        self.dept=dept
        self.sal=sal
    def showdetail(self):
        print("name:",self.name)
        print("dept:",self.dept)
        print("sal:",self.sal)
class engineer(employee):
    def __init__(self,role,sername):
        self.role=role
        self.sername=sername 
        super().__init__("bhavani","cse",50000)   


e1=engineer("engineer","biradar")
e1.showdetail()
print(e1.role)
print(e1.sername)