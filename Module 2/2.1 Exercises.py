#-----------------------------------------------------------------------------------------------2.1.1.6--------------------------------------------------------------------


#use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string;
print("Hello, Python!")

#having done that, use the print() function again, but this time print your first name;
print("Jim")

#remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?

#print(Jim)
#Traceback (most recent call last):
#  File "main.py", line 6, in <module>
#    print(Jim) 

    
#then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?   

#print"Jim"
#  File "main.py", line 14
#    print"Jim"
#             ^
#SyntaxError: invalid syntax


#Test with single quotes
print('Jim with single quotes')


#---------------------------------------------------------------------------------2.1.1.18--------------------------------------------------------------------------------------


#Modify the first line of code in the editor, using the sep and end keywords, to match the expected output
print("Programming","Essentials","in...",sep="***",end="")
#Don't change anything in the second print() invocation.
print("Python")


#---------------------------------------------------------------------------------2.1.1.19--------------------------------------------------------------------------------------


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

#duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

#remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
#print("***   ***)  #quote removed on this line
print("  *   *")
print("  *   *")
print("  *****")
#File "main.py", line 5
#    print("***   ***)
#                    ^
#SyntaxError: EOL while scanning string literal

#do the same with some of the parentheses;

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
#print("***   ***" parentheses removed from this line
print("  *   *")
print("  *   *")
print("  *****")
# File "main.py", line 6
#    print("  *   *")
#        ^
#SyntaxError: invalid syntax


#change any of the print words into something else, differing only in case (e.g., Print) - what happens now?

print("    *")
print("   * *")
print("  *   *")
# Print(" *     *") P changed to upper case in print function name
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#   *
#   * *
#  *   *
#Traceback (most recent call last):
#  File "main.py", line 4, in <module>
#    Print(" *     *")
#NameError: name 'Print' is not defined

#replace some of the quotes with apostrophes; watch what happens carefully.

print("    *")
print("   * *")
print("  *   *")
#print(' *     *") double quote changed to single quote on this line
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#File "main.py", line 4
#    print(' *     *")
#                    ^
#SyntaxError: EOL while scanning string literal