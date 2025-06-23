#data structures define how data is stored and organized outside of normal primitive types (float, int string)
#data structures contain more than one piece of data
#python simplest data structure is a list
#this is similar to an array in other langauge with some difference (array-list)
#lists are dynamic in size (there is no fixed size)
#lists can contain multiple types of data (ie intergers and strings in one list..do not recommend)
#lists really are a way to organize things a list like structure...so items that are related in some way
#list are mutable - can they change, deleted, or added to 

#create a list - syntax
# varname = []
# a list can be empty or initialized with values

#create a list with some data values for test scores
test_scores = [100,99,77,55]
#each item in list is separated by a comma
#to acces items in a list you say listname[index]
#index is just the order or position of an item in a list
#start at 0, and then count up from each item in the list
#ie in the above example test_scores[0] = 100, test_scores[1] = 99, etc..
print(test_scores[0])
print(test_scores[1])

# #another advantage of a list is the ability to use loops to process a list
# #this allows us to process or display mutiple items at once
# #display data = we call a for in loop
# # a for in loop allows us to say for each item in this list do the following thing to it
# # a for in loop counts the number of items in a list and loops through it
# #syntax for iteratorname in listname

for test_score in test_scores:
    print(test_score)

# #modify things in a list
for test_score in test_scores:
    test_score = test_score + 5
    print(test_score)

# #add things to a list
# #.append method/function - adds item to end of list
test_scores.append(82)
print(test_scores)

# #when modifying a list those changes are not save to the orignial list, there are a couple ways you can do that
# #the easiest and most common is to make a new list and save those changes to that list
new_list = []
for test_score in test_scores:
    test_score = test_score + 5
    new_list.append(test_score)

print(new_list)

#you can also combine list together
#extend() function combines one list with another
test_scores2 = [95,44,76, 95]
test_scores.extend(test_scores2)
print(test_scores)

# #remove the first instance of a given value in a list using .remove
test_scores.remove(100)
print(test_scores)

# #searching through a list
# #if you are just wanting to see if something is in a list, we can use the in keyword similar to how we use for in
looking_for = 95
found = looking_for in test_scores
print(found)
if found == True:
    print("Found the value")
    test_scores.remove(looking_for)
    print("Removed")
    print(test_scores)
else:
    print("Value not found..nothing removed")

# #count the number of same values in a list
print(test_scores.count(95))

# #sort a list in ascending order (smallest to largest)..use .sort()
test_scores.sort()
print(test_scores)

# #sort in desc order (largest to smallest)
test_scores.sort(reverse=True)
print(test_scores)

# #see the length of a list.. use len function
print(len(test_scores))

#there are also other ways to process data.. for instance if you need to use the index value in the loop to help you process data..this is possible
#this is more of a 'traditional' way people would loop through a list or an array
for i in range(len(test_scores)):
    print(i + 1, ".", test_scores[i])