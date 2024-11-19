number = 123
print(number)
print(type(number))

name = "chandan kumar"
print(name)
print(type(name))
print(len(name))

txt ="this is a python class"
for letter in txt:
    print(letter)

    #list data types []

my_list = [123, "ram" , 32.25]
print(my_list)
print(type(my_list))

#nested data types: [2]
L = ['a', 'b' ,['cc','dd',['eee','fff']],'g','h']
print(L)
print(L[2])
print(L[2][0])
print(L[2][2])
print(L[3])
#negative index data 
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# slicing in list
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

