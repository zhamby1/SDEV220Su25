# we can use loops to create ways to validate input until we get an answer or value that is acceptable
#we ususally do this by nesting if/else statements inside of a while loop

#we can also use raw boolean values to run our loops and in this case, we can use the special keyword break to break a loop vs a sentinel value

#this program will ask the user to accept the terms and conditions..if they do not it will continually ask them until they do

while True:
    accept = input("Do you accept the terms and conditions of running this program? ")
    if accept != "y":
        print("Not accepted.  You cannot run this program until you accept the terms.  I will ask again")
    else:
        print("Thanks for accepting our terms of use")
        break
