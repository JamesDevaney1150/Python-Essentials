#Python Essentials -  Module 2  - Last updated 21/09/2021
#---------------------------------------------------------------------------------2.1.1.6: The print() function--------------------------------------------------------------------------------------
#use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string;
print("Hello, Python!")

#having done that, use the print() function again, but this time print your first name;
print("Jim")

#Test with single quotes
print('Jim with single quotes')

#---------------------------------------------------------------------------------2.1.1.18: The print() function--------------------------------------------------------------------------------------
#Modify the first line of code in the editor, using the sep and end keywords, to match the expected output
print("Programming","Essentials","in...",sep="***",end="")
#Don't change anything in the second print() invocation.
print("Python")

#---------------------------------------------------------------------------------2.1.1.19: Formatting the output--------------------------------------------------------------------------------------
#minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    * \n   * * \n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****" )
#make the arrow twice as large (but keep the proportions)
print("           **")
print("           **")
print("        **    **")
print("        **    **")
print("      **        **")
print("      **        **")
print("    **            **")
print("    **            **")
print("  ******        ******")
print("  ******        ******")
print("      **        **")
print("      **        **")
print("      **        **")
print("      **        **")
print("       **********")
print("       **********")

#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring"
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)
#---------------------------------------------------------------------------------2.2.1.11: Python literals - strings------------------------------------------------------------------------
#Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.
print("\"I'm\" \n\"\"learning\"\" \n\"\"Python\"\"\"")

#---------------------------------------------------------------------------------2.4.1.7: Variables--------------------------------------------------------------------------------------
#create the variables: john, mary, and adam;assign values to the variables. 
#The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=",")

total_apples = john+mary+adam
print("Total number of apples:",total_apples)

#---------------------------------------------------------------------------------2.4.1.9: Variables and simple converter-------------------------------------------------------------------
#Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, 
#complete the program in the editor so that it converts: miles to kilometers; kilometers to miles.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#---------------------------------------------------------------------------------2.4.1.10: Operators and expressions----------------------------------------------------------------------
#Evaluate the following expression: 3x3 - 2x2 + 3x - 1. The result should be assigned to y.

x =  -1
x = float(x)
y=(3*x**3)-(2*x**2)+(3*x)-1
print("y =", y)
#---------------------------------------------------------------------------------2.5.1.2:Comments--------------------------------------------------------------------------------------
#Becoming familiar with the concept of comments in Python:
#this program computes the number of seconds in a given number of hours
#this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

print("\"Goodbye\"")#here we should also print "Goodbye", but a programmer didn't have time to write any code
a=3
print("Number of seconds in 3 Hours:", a * seconds)#this is the end of the program that computes the number of seconds in 3 hour

#---------------------------------------------------------------------------------2.6.1.9:Simple input and output--------------------------------------------------------------------------------------
#Evaluate the results of four basic arithmetic operations:
a = float(input("Input a")) # input a float value for variable a here
b = float(input("Input b:")) # input a float value for variable b here

print(a + b) # output the result of addition here
print(a - b) # output the result of subtraction here
print(a * b) # output the result of multiplication here
print(a / b) # output the result of division here
print("\nThat's all, folks!")

#---------------------------------------------------------------------------------2.6.1.10:Operators and expressions--------------------------------------------------------------------------------------
#Evaluate the expression from the lab:
x = float(input("Enter value for x: "))

# Write your code here.
y=1/((x+1/(x+1/(x+(1/x))))) #evaluating expression given in lab,

print("y =", y)

#---------------------------------------------------------------------------------2.6.1.11:Operators and expressions--------------------------------------------------------------------------------------
#Simple code able to evaluate the end time of a period of time:

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#Evaluates end timeby using floor division then modulus to give the results of the remainder.
print((hour +(mins+dura)//60) %24,":",(mins+dura)%60,sep="")

#---------------------------------------------------------------------------------3.1.1.4:Questions and answers--------------------------------------------------------------------------------------
#simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100
n=int(input())
print(n>=100) #prints True if n greater than 100 and False if n less than 100

#---------------------------------------------------------------------------------3.1.1.10:Comparison operators and conditional execution----------------------------------------------------------------
#Write a program that utilizes the concept of conditional execution, takes a string as input and output is dependant on input.
spath=(input())
lowerspath="spathiphyllum" #used to check if matches input
lowerspathresult= "No, I want a big Spathiphyllum!" #prints if spath equals lowerspath
upperspath="Spathiphyllum" #used to check if matches input
upperspathresult = "Yes - Spathiphyllum is the best plant ever!" #prints if spath equals upperspath
nospath = "Spathiphyllum! Not "+ spath + "!" #prints if spath doesn't equal lowerspath or upperspath

if spath == lowerspath: print(lowerspathresult) #prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
elif spath == upperspath: print(upperspathresult) #prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
else: print(nospath) #prints "Spathiphyllum! Not [input]!" 

#---------------------------------------------------------------------------------3.1.1.11: Essentials of the if-else statement----------------------------------------------------------------
#Tax Calculator
income = float(input("Enter the annual income: ")) #accept one floating-point value: the income.
threshold = 85528 #Tax threshold that defines tax rate

if income < threshold: tax = income *(0.18)-556.02 #pay lower tax if income below threshold
else: tax =(income - threshold)*0.32 + 14839 #pay higher tax if income above threshold
if tax <=0: tax = 0 #if calculated tax is less than zero, pay no tax
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#---------------------------------------------------------------------------------3.1.1.12: Essentials of the if-elif-else statement----------------------------------------------------------------
#Gregorian Calendar Leap Year checker
year = int(input("Enter a year: ")) #Variables defined
leap = "Leap year"
common = "Common year"
gc=1582
	
if year < gc:print("Not within the Gregorian calendar period")
elif year % 4 !=0: print(common) #if a remainder is returned that is not equal to 0 the print function will execute
elif year % 100 !=0: print(leap) 
elif year % 400 !=0: print(common)
else: print(leap)
