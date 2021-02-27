s = input("Enter a string: ") 
start = s[0] 
end = s[-1] 
swapped_string = end + s[1:-1] + start 
print(swapped_string) 
