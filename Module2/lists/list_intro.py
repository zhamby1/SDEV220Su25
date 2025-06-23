#data structures - define how data is store and organized outside of normal (primative) data types like floats, strings, or ints
#usualy contain more than one piece of data
#pythons simpliest data structure is a list
#this is similar to arrays in other languages with some differences
#lists are dynamic in size (ie no fixed size)
#list can contain multiple data types inside of it (usually recommend not to do this)
#lists are mutable, they can change after they are created and items inside of it can be modified or deleted or added

#syntax to create a list
#nameoflist = []
#list can be empty or initialized with values

#create a list of test cores
test_scores = [100,90,77,85]
#each item in a list is separated by a comma
#to access items in a list you say listname[index]
#index is the order/position of the item in a list
#indexes satar at 0, in the above example to access the number 100 we would say test_scores[0], 90 test_scores[1] etc...

print(test_scores[0])
print(test_scores[1])

#another advantage of a list is to loop through it to access all the values of a list or process data
#to do this we need to us a loop to display all the items of a list
#we can still use our for in loop...the syntax is just slightly different
#count the number of items in a list and loop through those items and process or display data

#syntax - for singular_version_of_variable_name in list
#display all test_scores

for test_score in test_scores:
    print(test_score)

#you can modify data in a list
for test_score in test_scores:
    test_score = test_score + 5
    print(test_score)


#to add values to a list we use the append function
new_score = 67
test_scores.append(new_score)

#if you want a shorthand way to just LOOK at a list, you can use the print function(listname) aka peek at a list
print(test_scores)

#save modified data
new_test_scores = []
for test_score in test_scores:
    test_score = test_score + 5
    new_test_scores.append(test_score)

print(new_test_scores)
