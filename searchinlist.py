lis=input("Enter a list(seperated by space):")
n=int(input("Enter the number to be searched:"))
lis1=list(map(int,lis.split()))
print(lis1)
k=len(lis1)
for value in lis1:
    if n==value:
        print("The number",n,"is found in the list.")
        break
else:
    print("The number not found in the list.")
