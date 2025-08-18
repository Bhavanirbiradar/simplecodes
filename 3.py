class student:
    def __init__(self,name,list):
        self.name=name
        self.list=list
        sum=0
        avg=0
        for i in range(len(list)):
            sum+=list[i]
            avg=sum/len(list)
        
        print("Average marks of", self.name, "is", avg) 
        print("Total marks of", self.name, "is", sum)
list=[2,4,6,8]
s1=student("bhavani",list)
