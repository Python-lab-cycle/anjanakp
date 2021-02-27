a=int(input("enter a number:"))
factor(a)
    
def factor(a):
    for i in range (1, (a+1)):
        if (a%i==0) : print(i)
        return;
