listofInt=[]

for i in range(4,24,2):
	listofInt.append(i)

#print("a suitable message",listofInt)

tripledlist=[i*3 for i in listofInt]
print(tripledlist)