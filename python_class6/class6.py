even= [2,4,6,8,10]
even[3]= 5
print(even)

even= [3,5,7,9,11]
even[4]=10
print(even)

odd= [3,5,7,9,11]
odd[2:4]= [2,4,8]
print(odd)

odd = [1,3,5]
odd.append(6)
print(odd)

#odd.apend(2,9):  there are error show. bcz only one value put in value in append method.

odd.extend([9,11,13]) #multiple value added in extend methods
print(odd)

odd = [1,9]
odd.insert(1,3) #print index before 
print(odd)
odd[2:2]=[5,7]
print(odd)
# concatination and repeting
odd= [1,3,5]
print(odd+[9,7,5])
print(["re"]*3)

#deleting list items
my_list = ["p","r", "o","y","t"]
del my_list[2]
print(my_list)
del my_list[1:3]
print(my_list)
del my_list
# print(my_list) #deleting all variable and values so showing error

my_list = ["p","r", "o","y","t"]
my_list.remove("r") #remove method : remove at the given particular values
print(my_list)
my_list.pop() #pop method: remove last list value
print(my_list)
my_list.pop(1) # remove index wise in list
print(my_list)