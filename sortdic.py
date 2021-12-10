d={ 1:2, 3:4, 4:3, 2:1, 0:0 }
print("Orginal dictionary is :",d);
sort = sorted(d.items())
print("Dictionary in ascending order:",sort);
sort = sorted(d.items(), reverse = True)
print("Dictionary in decending order:",sort);
