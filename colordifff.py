color1=input("Enter a set of colours(space seperated):")
color2=input("Enter a set of colours(space seperated):")
c1=set(color1.split())
c2=set(color2.split())
print("The difference between c1 and c2 is :",c1.difference(c2))
