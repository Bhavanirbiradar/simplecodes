import random
import string
#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
pass_len=int(input("enter the length of yoour password:"))
charvalue=string.ascii_letters + string.digits + string.punctuation
password="".join([random.choice(charvalue) for i in range(pass_len)])
#for i in range(pass_len):
 ##  password+=value
print("your password is:",password)
