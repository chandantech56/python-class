# ---------FOR LOOP---------------
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
for i in range(10):
    print(i)
#print table using for loop
number= int(input("Enter the number"))
for count in range(1,11):
    table= number*count
    print(number, "x" , count, "=", table)
# #----------------------------------------
for i  in range(1,50):
    print(i)

# --------WHILE LOOP-------------------
#Python while loop: The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
count=0
while count<=4:
    print("hello, im a while loop") #print unfinite bcz not given stop...
    count= count+1

# #print table using while loop
number= int(input("Enter the number"))
count=1
while count<=10:
    table= number*count
    print(number, "x", count, "=", table)
    count = count+1

#print table in reverse using while loop
number= int(input("Enter the number"))
count=10
while count>=1:
    table= number*count
    print(number, "x", count, "=", table)
    count = count-1

# Python break and continue Statement:
for i in range(1,6):
    print(i)

for i in range(1,6):
    print(i)
    break  

for i in range(1,5):
    if i==3:
        break
    print(i)
print("the end")  

for i in range(5):
    number= float(input("enter the number: "))
    if number<0:
        continue
    print(number)

#Pass Statement: pass statement is a null statement.
number=5
if number>0:
    pass


#---------FUNCTION------------
# Functions: A function is a group of related statements that performs a specific task. 
#          * functions help break our program into smaller and modular chunks. As our program grows 
#          * larger and larger, functions make it more organized and manageable. 
#          * It avoids repetition and makes the code reusable.

def greet():
  print("hello")
  print("how are you")
greet()   

#print greet values 3 times (again again)
def greet():
    print("hello")
    print("how are you")
greet() 
greet() 
greet() 

#add function
def add(a,b):
    c = a+b
    print("The result of c is: ", c)
add(20,30)  #output 50

# Calculatong factorial in function
def factorial(n): #"""Return the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Lambda Functions: In Python, an anonymous function is a function that is defined without a name.
add=lambda a,b:a+b
print(add(10,20)) #output 30
