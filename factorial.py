num=int(input("Enter the number:"));
fact=1
if num < 0:
    print("Factorial does not exsist!!");
elif num == 0:
    print("The factorial is 1.");
else:
    for i in range(1,num+1):
        fact=fact*i;
print("The factorial of the given number is ",fact);
