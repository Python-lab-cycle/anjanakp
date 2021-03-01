import csv
with open('Employee2.CSV',newline='')as CSVfile1:
    data=csv.DictReader(CSVfile1)
    print("empno empname")
    print("--------------")
    for i in data:
        print(i['Empno'],i['EmpName'])
