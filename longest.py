str = input("Enter the listof words:");
list = str.split()
print(list)
max1 = len(list[0])
temp = list[0]
for i in list:
    if(len(i) > max1):
        max1 = len(i)
        temp=i
print("Longest word in the listb is:",temp)
print("Length is:",len(temp))
