#variables store data
#Python is a weakly typed language, meaning you do not have to declare the type of variable you are using. 

#Python uses mainly the following data types:
#int - integer, whole number
#float - decimal number
#str - string, text
#bool - boolean, True or False

x = 8 #int
y = 3.14 #float
name = "John" #str
is_student = True #bool

#functions are basically actions that can be performed
#functions are the verbs of the programming language
#we will use built-in function for now that is provided by Python
#you know something is a function if it has parentheses after it vs a variable which does not have parentheses
#the text inside of the parentheses is called an argument...it is used to pass some type of data to the function

#one function we will use is the print() function
#print displays the data to your screen
print(x) # - the argument of print is the variable x
print(y)
print(name)
print(is_student)

#to join (concatenate) strings together, we can use the , in python to separate the strings and give a space between them
print("Hello", name)

#another function we will use the is the input() function
#input allows the user to enter data into the program
#the data is stored in a variable, and is always a string

username = input("Enter your name: ") #the argument of input is what will be displayed to the user as a prompt
print(username)

#the cool thing about variables is that you can change their value at any time
#you can also use the current value of a variable in a calculation

x = x + 2 #this adds 2 to the current value of x
print(x) #this will now print 10, because we changed the value of x