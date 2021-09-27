#x = float(input("Enter value for x: "))

# Write your code here.
#y=1(x+1/(x+1/(x+(1/x))))

#print("y =", y)

#x = int(input())
#y = int(input())

#x = x / y
#y = y / x

#print(y)

#x = int(input())
#y = int(input())

#x=x%y
#x=x%y
#y=y%x
#print(y)

#x=1 / 2 + 3 // 3 + 4 ** 2
#print(x)

#z = y = x = 1
#print(x,y,z, sep='*')
#x = int(input())
#y = int(input())
#print(x+y)

#income = float(input("Enter the annual income: "))

# Write your code here.
#threshold = 85528

#if income < threshold: tax = (income *0.18)-556.02
#else: tax = (income -threshold)*32 +14839.02
#tax = round(tax, 0)
#print("The tax is:", tax, "thalers")

#income = float(input("Enter the annual income: "))

# Write your code here.
#threshold = 85528

#if income < threshold: tax = income *(0.18)-556.02
#else: tax = 14839+((income - threshold)*32)
#if tax <=0: tax = 0
#tax = round(tax, 0)
#print("The tax is:", tax, "thalers")

#nums = [1,2,3]
#vals = nums
#del vals[1:2]
#print(nums, vals)

#i = 0
#while i <=5:
 #   i+=1
  #  if i %2 ==0:
  #      break
#my_list = [i for i in range(-1,2)]
#print(my_list)

#for i in range(1):
#    print("#")
#else:
#    print("#")

#my_list_1 = [1,2,3]
#my_list_2 = []
#for v in my_list_1:
#    my_list_2.insert(0,v)
#print(my_list_2)

#vals=[0,1,2]
#print(vals)
#vals[0],vals[2]=vals[2],vals[0]
#print(vals)

#var=1
#while var<10:
#    print("#")
#    var=var<<1

#i=0
#while i <=3:
#    i+=2
#    print("*")

#my_list=[1,2,3]
#for v in range(len(my_list)):
#    my_list.insert(1,my_list[v])
#print(my_list)

#z=10
#y=0
#x=y<z and z>y or y>z and z<y
#print(x)

#vals=[0,1,2]
#vals.insert(0,1)
#del vals[1]
#print(vals)

#my_list = [[0,1,2,3]for i in range(2)]
#print(my_list[2][0])

#nums = [1,2,3]
#vals = nums[-1:-2]
#print(nums,vals)

#t = [[3-i for i in range (3)] for j in range(3)]
#s=0
#for i in range(3):
#    s +=t[i][i]
#print(s)

#a=1
#b=0
#c=a&b
#d=a|b
#e=a^b
#print(c+d+e)

#x=1
#x=x==x
#print(x)

#my_list=[3,1,-2]
#print(my_list[my_list[-1]])

#var=0
#while var <6:
#    var+=1
#    if var % 2 ==0:
#        continue
#    print("#")

#my_list = [1,2,3,4]
#print(my_list[-3:-2])

#nums = [1,2,3]
#vals = nums
#del vals[1:2]
#print(nums, vals)
def is_year_leap(year):
    if year < 1582:return False          #code copied from 4.3.1.6
    elif year % 4 != 0: return False
    elif year % 100 != 0: return True
    elif year % 400 != 0: return False
    else: return True

def days_in_month(year, month):
    monthlength=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year <1582 or month <1 or month >12: return None  #code copied from 4.3.1.7
    if is_year_leap(year) and month ==2: return 29
    return monthlength[month-1] 
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

def day_of_year(year, month, day):
    if year <1582 or month <1 or month >12 or day<1 or day >31: return None #returns None if any arguments are invalid
    days=day #assigns number of days in current month to days variable
    month=month-1 #doesn't use current month selected in parameter as it has been counted already in days
    while month >0: #while loop to count each month
        days += days_in_month(year,month) #counts the days in each month as it iterates through the while loop
        month -=1 #subtracts 1 from month for while loop
    return days #returns variable days once while loop has ran
print(day_of_year(2000, 12, 31)) 
        




 
