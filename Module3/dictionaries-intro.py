#dictionaries create key-value paris that associate a name(key) with a value
#python treats dictionaries like objects or maps
#objects are containers that have properties(characteristics) that describe an item that has charactertics that describe or are a part of that item.
#Person - name, age
#Car - make, model, year

#so dictionaries are flexible because we can describe them as objects or as like an actualy dictionary would look.
#ie an object and dictonary are the same thing in python, it is just how we organize the data
#let's use a dictionary like an actual dictionary.
#we have a list of related values that we want to associate with names (like with terms and definitions)
#if we are a bank and we wanted a list of bank_balances, we would have to have some way to associate the balances by a name of key
#syntax for dictionary is dictname = {"key_name" :value,}

#dict of bank customers and their balances
bank_customers = {
    #keys are always strings surrounded by quotes
    "Alice" : 100.00,
    "Tim" : 500.25,
    "Sam" : 850.21
    
}

#to display things in a dictionary, we can access by their keys
# for key in bank_customers:
#     #to access values we have similar syntax to how we would access our list values...instead of an index we use the keyname
#     print(key, bank_customers[key])

# #we can also use a dict like an object in that we are describing one thing that has multiple related characteristics
# #often times when we organize it this way we can the keys properties or fields (more on that when we get to classes)
# #they describe a single object and it's characteristics
# person_zach = {
#     "name": "Zach Hamby",
#     "age": 39,
#     "city": "Indy"
# }

# for details in person_zach:
#     print(details,":", person_zach[details])

#dicts are mutable - they can be modified and added to
#all you have to do is add a new key name with a value
#key names do have to be unique
#name_of_dictionary[newkeyname] = value
bank_customers["Zach"] = 400.00
print(bank_customers)

#if we want to modify the dict, we do the same thing, but we just have to know the name of the key
#what is actually happening when we make a new entry in a dict, is that it first searches to see if they key is already there or being used
#if it, it will just replace the value with the new value you have given it, otherwise it makes a new entry
bank_customers["Alice"] = 1000.00
print(bank_customers)

#to grab a single item to see its value in a dictionary, we can use .get() function
alice_balance = bank_customers.get("Alice")
print(alice_balance)

#to delete we say del dict_name[key]
del bank_customers["Alice"]
print(bank_customers)

#seaching is similar to a list.. we can use the in keyword
key = "Tim"
if key in bank_customers:
    print(key, "is in the dict")
else:
    print(key, "is not in the dict")

#maybe want a more detailed search..ie keyname and value match search terms
find_name = "Tim"
value = 500.25

#.items() function with in keyword statements allows us to search things with keys AND values
for name, balance in bank_customers.items():
    if name == find_name and balance == value:
        print("Found Tim and his balance match")