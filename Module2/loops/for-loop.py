#for loops repeat code a certain number of times, but is often the more useful of the two loops for one big reason
#organizing, searching, and displaying data from data structures like a list
#python is a little weird with for loops... There are several ways to do it, but in other languages, this is the typical syntax for a =for loop

#for(int i = 0; i < 10; i++)
#the i variable is just shorthand for iterator
# iterators are values that keep up with the current loop number / value
#iteration means to go through a loop or cycle

#python uses a range function to take care of the iteration values
# for in loop - for blank in blank.  for i in the number of loops
#syntax  - for iternatorname in range(starting_value,ending_value,step/increment/decrememnt)

number = 5
#we will use i for our variable name, and i can also keep track of the current loop to do things like display the current loop value
for i in range(0,number,1):
    print(i)

print("******************")

#decrements - use negative values or countdown vs countup
count_down = 0
for i in range(10,count_down,-1):
    print(i)


print("***************")
#You also do not have to count up just by 1s....you can other step values to count
number2 = 10
for i in range(0,number2,2):
    print(i)