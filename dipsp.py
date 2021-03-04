import csv
csv_columns = ['id','name', 'place']
dict_data = {'id':['1', '2', '3'],
    'name':['Manu','Minnu','Kichu'],
    'place':['Banglore','Ernamkulam','Muvattupuzha'],
     }
csv_file = "temp.csv"
try:
   with open(csv_file, 'w') as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           writer.writerow(dict_data)
except IOError:
   print("I/O error")
data = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
   print(row)
