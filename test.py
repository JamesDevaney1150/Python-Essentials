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

income = float(input("Enter the annual income: "))

# Write your code here.
threshold = 85528

if income < threshold: tax = (income *0.18)-556.02
else: tax = (income -threshold)*32 +14839.02
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

income = float(input("Enter the annual income: "))

# Write your code here.
threshold = 85528

if income < threshold: tax = income *(0.18)-556.02
else: tax = 14839+((income - threshold)*32)
if tax <=0: tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


