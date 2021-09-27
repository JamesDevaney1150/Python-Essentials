#Python Essentials -  Module 4  - Last updated 27/09/2021
#---------------------------------------------------------------------------------4.3.1.6: A leap year: writing your own functions--------------------------------------------------------------------------------------
#Familiarise projecting and writing parameterized functions, utilising return statement, testing functions

def is_year_leap(year):
	if year < 1582: return False
	elif year % 4 != 0: return False                  #same code as 3.1.1.12, if there is a remainder then return.
	elif year % 100 != 0: return True
	elif year % 400 != 0: return False
	else: return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

#---------------------------------------------------------------------------------4.3.1.7: How many days: writing and using your own functions--------------------------------------------------------------------------------------
#Familiarise projecting and writing parameterized functions, utilising return statement, using own functions
def is_year_leap(year):
    if year < 1582: return False          #code copied from 4.3.1.6
    elif year % 4 != 0: return False
    elif year % 100 != 0: return True
    elif year % 400 != 0: return False
    else: return True

def days_in_month(year, month):
    monthlength=[31,28,31,30,31,30,31,31,30,31,30,31] #list filled with month's lengths
	#if year<1582 or month <1 or month >12: return None  #if selection is out of range return None
    if is_year_leap(year) and month ==2: return 29 #checking if leap year and feb selected, if so return 29
    return monthlength[month-1] #returns the element in list, subtracts 1 from month as list starts at 0
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
#---------------------------------------------------------------------------------4.3.1.8: Day of the year: writing and using your own functions--------------------------------------------------------------------------------------
#Familiarise projecting and writing parameterized functions, utilising return statement,building a set of utility functions, using own functions
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
#---------------------------------------------------------------------------------4.3.1.9: Prime numbers - how to find them--------------------------------------------------------------------------------------
#familiarise with classic notions and algorithms, improve skills in definding and using functions
def is_prime(num):
    for i in range (2,num): #range starts at 2 and between num parameter selected in function to create a for loop
        if num % i == 0: #num is checked throughout the loop to see if modulo by i
            return False #if not modulo then return false
    return True			 #else return true

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
#---------------------------------------------------------------------------------4.3.1.10:LAB: Converting fuel consumption--------------------------------------------------------------------------------------
#Improving skills in defining, using, testing functions
def liters_100km_to_miles_gallon(liters):
    miles = 100*1000 /1609.344   #maffs
    gallons = liters /3.785411784
    return miles /gallons                        #Not much on this, just working out the maths.

def miles_gallon_to_liters_100km(miles):
    km = miles *1609.344 /1000  #more maffs
    liters = 3.785411784
    return liters / (km /100)
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
