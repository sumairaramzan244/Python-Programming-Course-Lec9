
# List is a collection which is ordered and changeable. Allows duplicate members.



mylist = ["apple", "banana", "cherry"]
print(mylist)

mylist.append(" new fruit orange") # This will raise an error because list does not have an add method
print(mylist)

mylist.insert(1, " new fruit orange") # This will insert the new fruit at index 1
print(mylist)

mylist.remove("banana") # This will remove the first occurrence of "banana" from the list
print(mylist)

mylist.pop(1) # This will remove the item at index 1 and return it
print(mylist) 



mylist.append("grape") # This will add "grape" to the end of the list
print(mylist)
# mylist.clear() # This will remove all items from the list

print(len(mylist)) # This will print the length of the list





# Conditional statements in Python are used to perform different actions based on different conditions. The most common conditional statements are if, elif, and else.


age=20

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

    