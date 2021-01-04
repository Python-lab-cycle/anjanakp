str1=input("Enter the first string:")
str2=input("Enter the second string:")
a=str2[:2]+str1[2:]
b=str1[:2]+str2[2:]
print("The new string after swapping first two characters of both string is:",a+' '+b)
