#functions can also return value into variables or other functions
#return value = value that is returned into something outside of the function
#we use keyword return to do this

def add_numbers(num1,num2):
    sum = num1 + num2
    return sum  #this will return data into something else...we have to then process the data outside the function


total = add_numbers(4,5)
print(total)

#chainging functions together is encouraged in python, and works as long as the innerfunction is a return statement
def add_tax(total):
    tax = total * 0.06
    total_with_tax = total + tax
    print(total_with_tax)


add_tax(add_numbers(5,5))