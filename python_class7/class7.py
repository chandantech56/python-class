list=[3,5,7,9,11,13,15]
print(list)
list.append(17)
print(list)

print(list.index(7)) #show index number wise search and given output.

print(list.count(9)) #total count in given values in list.

a = [1,2,2]
a.append(5)
print(a)
b = a.copy() # copy item in list
print(b)

prime_number= [11,15,7,5,23,]
prime_number.sort() #sort method asccending to descending(arrange items)
print(prime_number)

# a = ['p', 'y', 't', 'h', 'o', 'n']
#  = list(reversed(a))  # Reverses the list 'a' and prints it as a list
# print(a)
# b = "apple"


# b= list(reversed(b))  # Reverses the string 'b' and prints it as a list of characters
# print(b)

a= [1,2,3,4,5,6,8]
a.reversed()
print(a)
for fruits in ["mango","banana","grapes"]:
    print("i like fruits:", fruits)

matrix =[]
for i in range(2):
    matrix.append([])
    for j in range (2):
        matrix[i].append([j])
        print(matrix)

