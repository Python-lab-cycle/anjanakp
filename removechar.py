str1=input("Enter the string:")
n=int(input("Enter the index of the character to be removed:"))
first_part=str1[:n-1]
last_part=str1[n:]
print("The new string after removing the character is :",(first_part+last_part))
