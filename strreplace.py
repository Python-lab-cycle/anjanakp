str1=input("Enter a string:")
print("Original string is :",str1)
char=str1[0]
str1=str1.replace(char,'$')
str1=char+str1[1:]
print("The replaced string is:",str1)
