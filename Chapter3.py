#Python Essentials -  Module 3  - Last updated 22/09/2021
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

#---------------------------------------------------------------------------------3.2.1.3: Essentials of the while loop - Guess the secret number----------------------------------------------------------------
#Familiarise with while loop.
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

choice = int(input("Pick a number: ")) #User choice that can be used to compare to secret number

while choice != secret_number: #while loop works aslong as choice doesn't equal secret_number
    print("Ha ha! You're stuck in my loop!")
    choice = int(input("Try again (Don't choose 777): "))
print(secret_number, "Well done, muggle! You are free now.") #prints if choice is 777

#---------------------------------------------------------------------------------3.2.1.6: Essentials for the for loop - counting mississippily----------------------------------------------------------------
#Using the for loop
import time

# Write a for loop that counts to five.
i=0
for i in range (1,6):
    print(i, "Mississippi") # Body of the loop - print the loop iteration number and the word "Mississippi"
    time.sleep(1)# Body of the loop - use: time.sleep(1)
print("Ready or not, here I come!")# Write a print function with the final message.
#---------------------------------------------------------------------------------3.2.1.9: The break statement - Stuck in a loop----------------------------------------------------------------
#Familiarise break statement in loops
while True:
    word = input("Enter a word (Do not enter chupacabra): ")
    if word == "chupacabra": #compares word to string chupacbra if not same them loop again, break when chupacabra is entered.
        break
print("You've successfully left the loop!")

#---------------------------------------------------------------------------------3.2.1.10: The continue statement - the Ugly Vowel Eater----------------------------------------------------------------
#Familiarise continue statement in loops
user_word = input("Enter a word: ")
user_word = user_word.upper() #changes user_word to all uppercase
for letter in user_word:
    if letter == "A": continue #Any A in user_word will not continue, same for the elif letters below,
    elif letter == "E": continue
    elif letter == "I": continue
    elif letter == "O": continue
    elif letter == "U": continue
    else: print(letter) #only consonants printed as the vowels can't continue in the for loop

#---------------------------------------------------------------------------------3.2.1.11: The continue statement - the Pretty Vowel Eater----------------------------------------------------------------
#Familiarise with continue statement in loops and modify and upgrade existing code
word_without_vowels = ""
user_word = input("Enter a word: ")
user_word = user_word.upper() 
for letter in user_word:
    if letter == "A":continue #Any A in user_word will not continue, same for the elif letters below,
    elif letter == "E":continue
    elif letter == "I":continue
    elif letter == "O":continue
    elif letter == "U":continue
    else:word_without_vowels += letter #adds all the letters that get through the loop (only consonants) and adds 
print(word_without_vowels)             #them to the variable words_without_vowels, so they print on same line.

#---------------------------------------------------------------------------------3.2.1.14: Essentials of the while loop----------------------------------------------------------------

blocks = int(input("Enter the number of blocks: "))
height = 0
row = 1
while row <= blocks:
    height += 1 #addition assignment operator, adding 1 to height
    blocks -= row #subtraction assigment operator, subtracting row from blocks
    row += 1 #adding 1 to row
print("The height of the pyramid:", height)

#---------------------------------------------------------------------------------3.2.1.15: Collatz's hypothesis----------------------------------------------------------------
#Familiarise using the while loop

c0 = int(input("Enter a number: "))
if c0 < 1: print("¯\_(ツ)_/¯ Can't be a non-negative/zero") #take any non-negative and non-zero integer number and name it c0;
else: steps=0
while c0 != 1: #if c0 ≠ 1, skip to point 2
	if c0 %2 == 0: c0=int(c0/2) #otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1 #if it's even, evaluate a new c0 as c0 ÷ 2
	else:c0=3*c0+1 #otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1
	print(c0)
	steps += 1 #step counter, counts the number of loops by incrementing 1 everyone loop
print("steps =",steps)