#tuples are similar to lists but they are immutable - they cannot change after creation aka cannot be modified
#list of constants
#tuples are faster than lists
#values that do not or should be changed after creation
#great for fixed data to avoid the magic number situation
#they only way to 'change' a tuple is to make a new tuple and store the information from the old tuple with new added data

#first lets talk about how immutability
#string are technically immutable - you cannot replace individual letters in a string, you can only replace the whole string itself
#string in most langauges are a list or array of individual characters
#you can replace the whole string, but not insert or modify the characters after creation

# name = "zach"
# name = "tim"
# name[0] = "j"  #cannot change the individual letter..have to replace whole thing
# print(name)

#tuples are created using parenthesis...tuplename = (10,34,55)
#accessing a tuple is virtually identical to accessing a list
states = ("IL", "IN", "KY")

#for in loop to grab them
for state in states:
    print(state)

#Maybe you need to create another tuple from two other tuples. Tuples can only be combined or accessed
states2 = ("FL","NY", "NJ")
states3 = states + states2
print(states3)