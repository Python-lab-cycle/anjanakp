import csv
with open('Employee2.CSV',newline='')as file1:
    reader1=csv.reader(file1,delimiter=' ',quotechar='|')
    for row in reader1:
        print(','.join(row))
