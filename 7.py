class order:
    def __init__(self,product,price):
        self.product=product
        self.price=price
    def __gt__(self,o3):
        return self.price>o3.price
    
o1=order("laptop",5000)
o2=order("mobile",20000)
print(o1>o2)