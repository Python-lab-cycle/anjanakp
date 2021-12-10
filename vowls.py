a=input("Enter any word:");
vow = ['a','e','i','o','u'];
lis=[]
for x in a:
    if x in vow and x not in lis:
        lis.append(x);
print("Vowls are :",lis);

