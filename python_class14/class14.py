#oops concept: object orianted programming. 
class student(): #defining class
    pass
s1 = student() # creating object
s1.name = "Harry" #assignning values to attributes
s1.mark = 95
print(s1.name)
print(s1.mark)

class employee:
    name="chandan"
s1= employee()
print(s1.name)

class car:
  color= "blue"
  brand = "mercities"
car1 = car()
print(car1.color)
print(car1.brand)

#constructor in python
class supermarket:
    def __init__(self,product_name, product_price, product_color):
        self.name = product_name
        self.price = product_price
        self.color = product_color
s1 = supermarket("tv", "1000", "black")
print(s1.name)
print(s1.price)
print(s1.color)

#inheritance

class Animal:
    def Eat(self):
        print("i can eat")
class Dog(Animal):
    def Bark(self):
        print("dog can bark")
d1 = Dog()
d1.Bark() 
d1.Eat()         
#
