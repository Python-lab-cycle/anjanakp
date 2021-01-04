dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
print("Dictionary 1=",dic1)
print("Dictionary 2",dic2)
print("Dictionary 3",dic3)
print("The concatenated dictionary:",end=' ')
for d in (dic1,dic2,dic3): dic4.update(d)
print(dic4)
