

#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:

my_dict = {'name':'harry', 'age':30}
print(my_dict['name']) #1st method
print(my_dict.get('age')) #2nd method print

my_dict["age"] = 26 #add extra values and element.
print(my_dict)

my_dict.pop('age') #delete last key and values
print(my_dict)

print(my_dict.clear()) #clear entire element

#iterating dict. only print values not print variable...
squares = {1:1,3:9,5:25,6:36,7:49}
for i in squares:
    print(squares[i])

#set data types: Sets are used to store multiple items in a single variable.
#output is given jumble series
animal= {"cat","lion","monkey","tiger"}
print(animal)

animal= {"cat","lion","monkey","tiger","lion"} # duplicate values not allowed.
print(animal)

a= set() 
print(type(a))
a = {} #create empty dict.
print(type(a))


