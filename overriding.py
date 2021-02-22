class publisher:
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("Name",self.pname)
class book(publisher):
    def __init__(self,pname,bname,title):
        self.pname=pname
        self.bname=bname
        self.title=title
    def display(self):
        print("Pname",self.pname)
        print("Bname",self.bname)
        print("Title",self.title)
class python(book):
    def __init__(self,pname,bname,title,page,price):
        self.pname=pname
        self.bname=bname
        self.title=title
        self.page=page
        self.price=price
    def display(self):
        print("Pname",self.pname)
        print("Book",self.bname)
        print("Title",self.title)
        print("Pages",self.page)
        print("Price",self.price)
n=input("Enter publisher:")
b=input("Enter book:")
t=input("Enter title:")
p=int(input("Enter pages:"))
pr=int(input("Enter price:"))
obj=python(n,b,t,p,pr)
obj.display()
