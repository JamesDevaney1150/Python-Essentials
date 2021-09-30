

def caseChanger(hello):
	if hello == "hello":
		hello.lower()
		hello=hello.replace("e","E")
		return hello
	else:
		lowercase=str.lower(input("(task15)This will output all words into lower case except E: "))
		lowercase=lowercase.replace("e","E")
		return lowercase
print("(task15)",caseChanger("hello"))