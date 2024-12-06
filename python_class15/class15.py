class employee():
    s1 = employee(self)
    s1.name = david
    s1.salary = 5000
    s1.company = google
    print(s1.name)
    print(s1.salary)
    print(s1.company)

    #polimorphism
class ferrari:
    def fuel_type(self):
        print("petrol")
    def max_speed(self):
        print("max_speed 350")   
class bmw:
    def fuel_type(self):
        print("diesel")
    def max_speed(self):
        print("max_speed 240")    
f1 = ferrari()
b1 = bmw() 
f1.max_speed()        
b1.max_speed()
f1.fuel_type()   
b1.fuel_type()

# #2nd

class polygon:
    def display_info(self):
        print("a poligon has 2 dimentional shape")
class triangle (polygon):
    def display_info(self):
        print("a triangle has 3 side")
        super().display_info() 
class square (polygon):
    def display_info(self):
        print("a square has 4 side")
        super().display_info()   

t1 = triangle()
t1.display_info()

s1 = square()
s1.display_info()


try:
    numerator= int(input("enter numerator: "))
    denominitor= int(input("enter demonitor: "))
    result= numerator/denominitor
    print(result)
except:
    print("*****************")
    print("denominator cannot be 0. please enter valid number")
    print("*****************")
    print("end program")


#**************
try:
    my_list=[5,7,8]
    i = int(input("enter the index number "))
    print(my_list[i])
except:
    print("*******")

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for values in self.marks:
            sum += values
            print("Hi",self.name,"Your score is:", sum/3)
s1 = student("jukarbarg", [98,87,95])
s1.get_average()

