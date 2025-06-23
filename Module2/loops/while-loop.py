#loops are also control structures that repeat a block of code until a codition is met.  They use the same relational operators as if statements.
#Two types of loops - for and while
# while loops run until a condition is met usually with the use of sentinel value or flag
# a flag is a value that changes within the loop body to allow for an exit condition
# a for loop is a count-controlled loop that loops a certain number of times
# this can be based on a data structure and the number of items in it (list) or just a raw number

#flag
keep_going = "y"

#make a commission program to check sales and commission for an employee...breaks when the user is done with the program

#while syntax - while(condition):
while(keep_going == "y"):
    sales = float(input("Please give me your sales for the month "))
    com_rate = float(input("What is your commission rate in decimal form "))
    total_earned = sales * com_rate
    print("You have earned", total_earned, "this month")
    #break condition
    keep_going = input("Do you wish to run this program again? If so press y and enter. Otherwise press any other letter and enter to exit")

print("Thanks for using our program!")
