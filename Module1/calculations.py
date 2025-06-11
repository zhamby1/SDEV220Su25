#calculations in python consist of your basic math operations (addition, subtraction, multiplication, division)

#addition
a = 5
b = 3
sum = a + b
print(sum)

#subtraction
c = 10
d = 4
difference = c - d
print(difference)

#multiplication
e = 6
f = 7
product = e * f
print(product)

#division
g = 20
h = 4
quotient = g / h
print(quotient)

#integer division - drop a decimal
i = 20
j = 3
integer_quotient = i // j
print(integer_quotient)

#modulus - remainder of a division
k = 100
l = 7
remainder = k % l
print(remainder)

#exponentiation - raising a number to a power
m = 2
n = 3
exponent = m ** n
print(exponent)


#for the most part, strings cannot typically use the same mathmatical operations, because they are not numbers
#however, you can use the + operator to concatenate strings (combine strings together)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


#all inputs come in as strings...so what do we do when we want to do math with user input?
#we need to convert the string to a number using the int() or float() function

#int() - converts a string to an integer
#float() - converts a string to a float

#the cool thing about python is that it considers functions as first class citizens ie high order functions
#this means that you can use other functions as arguments to other functions
#ie chain functions together
#so if I want to convert a string to an integer from a input, I can do it all in one line
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
total = number1 + number2
print("The total is:", total)


#floats
number3 = float(input("Enter a decimal number: "))
number4 = float(input("Enter another decimal number: "))
total_float = number3 + number4
print("The total is:", total_float)