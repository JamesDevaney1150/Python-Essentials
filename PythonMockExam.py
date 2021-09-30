#James Devaney
#SIMR 20/001
#30071150

#####################################################
#Section 1 25 Marks

#1)
fltOne=float(10)

#2)
fltTwo=float(20)

#3)
fltThree=fltTwo + fltOne

#4)
stringOne = "The product of fltOne and fltTwo = "

#5)
print("(task5)",stringOne,fltThree)

#6)
fltOne = fltOne+1

#7)
fltTwo = float(input("(task 7) Please provide another number for fltTwo:"))
print("(task7)",fltTwo)

#8)
print("(task8) The product of fltOne and fltTwo is:",fltOne + fltTwo)

#####################################################
#Section 2 35 Marks

#8)
fltTwo = 99
if fltTwo<100:
	print("(task8)below 100")
else:
	exit

#9)
fltdif = fltOne - fltTwo
if fltdif <0:
	print("(task9)below 0")
elif fltdif >0:
	print("(task9)above 0")
else:
	print("(task9)value is zero")

#10)
listofInt=[]

#11a)
listofInt=[]

for i in range(4,24,2):
	listofInt.append(i)

print("(task 11a)a suitable message",listofInt)

#11b)
tripledlist=[i*3 for i in listofInt]

#11c)
print("(task11c)a suitable message",tripledlist)

#####################################################
#Section 3 20 marks

#14)
def calcPerc(cost,percentage=10):
	decrease = cost / 100 * percentage
	return cost - decrease
print("(task14)",calcPerc(50))

#15)
#def caseChanger():                          
#	lowercase=str.lower(input("(task15)This will output all words into lower case except E: "))      #This was the original code that uses methods
#	lowercase=lowercase.replace("e","E")                                                             # to lower and/or replace.
#	return lowercase
#print("(task15)",caseChanger())

def caseChanger(hello):                                                                               #This is my casechanger with an parameter that replaces
	if hello == "hello":                                                                              #the input which I found much harder
		hello.lower()
		hello=hello.replace("e","E")
		return hello
	else:
		lowercase=str.lower(input("(task15)This will output all words into lower case except E: "))
		lowercase=lowercase.replace("e","E")
		return lowercase
print("(task15)",caseChanger("hello"))



##################################################### 
#Section 4 20 marks

#16a)
student=["Clark","Horan","Rai""","White","Cooper","Jones","Cox","Smith"]

#16b)
student.sort()

#17)
marks=(65,66,67,80,90,65,65,93)

#18)
results={}
for i in range(len(student)):
    results[student[i]] = marks[i]
print("(Task18)",results)






