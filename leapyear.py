print("Leap year between two given years")
print("Enter start year")
startyear=int(input())
print("Enter last year")
endyear=int(input())
print("List of leap  years: ")
for year in range(startyear,endyear):
    if((year%4==0)and(year%100!=0)or(year%400==0)):
     print(year)
      
