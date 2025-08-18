with open("pra.txt", "r") as f:
    data = f.read()     
    print(data)
    """num=""
    for i in range(len(data)):
        if data[i]==",":
            print(int(num))
            num=""
        else:
            num+=data[i]"""
    nums=data.split(",")
    sum=0
   
    for i in nums:
        if (int(i) % 2 == 0):
            sum+=1
    print(sum)


    