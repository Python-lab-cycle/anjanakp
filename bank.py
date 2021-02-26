class bank():
    def __init__(self,acnt,nam,typ,amt):
        self.ac=acnt
        self.name=nam
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("Account name:",self.name)
        print("Account number:",self.ac)
        print("account type:",self.type)
        print("account balance:",self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("Enter the name:")
t=input("Enter type:")
a=int(input("Enter ac number:"))
am=int(input("Enter amount:"))
obj=bank(a,n,t,am)
print("Account details:")
obj.printamt()
w=int(input("Enter amount to withdraw:"))
print("b1=",obj.with1(w))
