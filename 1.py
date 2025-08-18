"""f=open("practice.txt","r")
f.write(" Hi everyone\n we are learning file io\n using java\n i like programming in java")
f.close()


f=open("practice.txt","r")
data=f.read()
ndata=data.replace("java","python")
print(ndata)
f.close()

f=open("practice.txt","w")
f.write(ndata)
f.close()
"""

def check_line():
    word="shravani"
    data=True
    no=1
    f=open("practice.txt","r")
    while data:
        data=f.readline()
        if data.find(word)!=-1:
            print(no)
        no+=1
    return -1
        
    f.close()
s=check_line()
print(s)
    