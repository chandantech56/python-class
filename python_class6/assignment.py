number= [10,20,5,8,9,7,11]
number[1]=30
print(number)

number[2:3]= 15,16
print(number)
number.append(12)
print(number)

number.extend([13,14,15,16])
print(number)

number.insert(1,15)
print(number)

number.remove(10)
print(number)

number.pop(2)
print(number)
#delete function
del number[2]
print(number)
cities= ["delhi","hydrabad","bangalore","pune","goa"]
del cities[3] 
print(cities)
