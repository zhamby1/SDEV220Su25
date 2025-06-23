#we already used functions like print() and input()
#if we want to make or own or custom function, we have to define or create a template for it
#in python we call this a defined function

#lets take a look at how a function works from a intro standpoint
#functions can be defined in several ways but lets look first
#functions in math take a series inputs, processes/calculates, the has an output
#functions in prog definition - a series of statements that can be called with a keyword, that CAN take input, process data, and CAN return an output

#functions can be used as summary of statements that you want to repeat, but do not return a value
#if there is no return value, we call this a void function
#to define a function we say def functioname(): , and indent all the code we want associated with it under the statement

#example of void function.  Adds two numbers but does not return data
def my_function():
    x = 4
    y = 6
    total = x + y
    print(total)

#so far we just defined the function.  To use it we need to call it..in this case just say my_function() and it will run

my_function()
#functions are great cause they are repeatable
my_function()

#power of functions start to become apparent when we use parameters
#we often use functions so we can pass data to it (or give it input data like a function in math)
#parameters - variables that are passed as data to a function
#variables are just placeholders for incoming data
#parameters are just an argument that we have not used yet and defined when creating a function
#reminder - arguments is what we use when running a function, parameters are the placeholders when defining a function...often people interchange these and that is fine
#print(name) - name is an argument
#def myfunction(name) - name is a parameter
#parameters are placed insed the parenthesis of a defined function
#passing data - givin the function some outside data to process
#we can pass any data type we want to the function including data structures like list
#in python we can also pass data to another function inside of it, this is known as higher order functions or functions as first class citizens
#this means we can chain functions
#number = int(input("Give me a number"))

def display_number(number): #number is a placeholder for data that we can pass to the function body
    print(number)

#when calling the function, the argument or variable name DOES NOT have to be the same name as the parameter
#the parameter is just there to tell the function what to do with the data.
my_number = 50
display_number(my_number)

#multiple parameters are separated by a comma
def add_numbers(num1,num2):
    sum = num1 + num2
    print(sum)

add_numbers(10,20)
mynum1 = 40
mynum2 = 50
add_numbers(mynum1, mynum2)

#order matters in functions
def divide_numbers(num1,num2):
    answer = num1 / num2
    print(answer)

divide_numbers(9,3)
divide_numbers(3,9)