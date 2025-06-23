#another use of loops is using it as an accumulator (ie keep up with running values or totals)
#averaging numbers is a good example..see below

total_sum = 0
average = 0

#we can ask the user how many numbers they wish to give us..thus using a count-controlled loop
#we doing this technique, remember loops use whole numbers (ints) because you can't go through a loop 3.5 times
how_many_numbers = int(input("How many numbers do you with to average? "))

for i in range(0,how_many_numbers,1):
    value = float(input("Please give me your value"))
    total_sum = total_sum + value

print("Your total sum is", total_sum)
average = total_sum / how_many_numbers

print("Your average is", average)