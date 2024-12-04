#Lambda Functions: In Python, an anonymous function is a function that is defined without a name.
add= lambda a,b: a+b
print(add(50,30))

#Global Variables:  A variable declared outside of the function or in global scope is known as a global variable.
#  This means that a global variable can be accessed inside or outside of the function.
message="hello how are you?" #assigning global variable
def greet():
    print("this is global variable: ", message)
greet()

#Local Variables: A variable declared inside the function's body or in the local scope is known as a local variable.
def greet():
    message="i am fine" #assigning local variable
    print("this is local variable: ", message)
greet()

#What are modules in Python? 
     # ● Modules refer to a file containing Python statements and definitions.*//

#inbuilt modules
#importing math module
import math
number = 50
result = math.sqrt(number)
print(result)
print(math.pi)
#To import specific function need to use "from" keyword
from math import sqrt
num = sqrt(625)
print(num)

#Custom modules (user defined modules)
# # def add(a,b):
# #     return a+b
# # def sub(a,b):
# #     return a-b

# import main
# result1 = main.add(50,20)
# print(result1)
# result2 = main.sub(80,40)
# print(result2)

# Zip(): The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
language =['java','python', 'html']
version=[14,20,15]
result= zip(language,version)
print(list(result)) #output [('java', 14), ('python', 20), ('html', 15)]

# Unzipping the Value Using zip(): 
language =['java','python', 'html']
version=[14,20,15]
result= zip(language,version)
result_list = list(result)
print(result_list)
l,v = zip(*result_list)
print('l=',l)
print('v=',v)

# map(): The map() function applies a given function to each item of an iterable (list, 
# tuple etc.) and returns an iterator. 

# (finding square of number using map and lambda function.)
num = [8,9,5]
squared_num = map(lambda n:n**2, num)
print(list(squared_num)) # Output: [64, 81, 25]

#adding two list values using map and lambda function.
num1 = [2,6,4,5]
num2 =[4,7,8,9]
result = map(lambda n1,n2: n1+n2, num1,num2)
print(list(result))

# filter(): The filter() function filters out the value of iterable if they don’t match the given condition.
num =[20,25,11,12,13,14]
even_num = filter(lambda n:n%2==0, num)
print(list(even_num)) # output: [20, 12, 14]

# format(): The format() function returns a formatted representation of a given value specified by the format specifier.
# integer
print(format(20,"d")) #output 20

#float
print(format(15.89,"f"))

#binary
print(format(4, "b")) #output 100

# End:  print statement in python. By default, the print function ends with a newline. Passing the whitespace to the 
# end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline. end the output with a space.
print("python", end="@") 
print("class") #output python @ class



