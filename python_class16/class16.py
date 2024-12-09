#iterate :● Iterators in Python: IteratorinPythonissimplyanobjectthatcanbeiterated
#  upon. An object which will return data, one element at a time.
#  ● Pythoniterator objects implement two special methods, __iter__() and __next__(), collectively called
#  the iterator protocol
my_list=[5,3,2,]
value= iter(my_list)

item1= next(value)
print(item1)

item2= next(value)
print(item2)

item3= next(value)
print(item3)

# item4= next(value)
# print(item4)         // (throw error: StopIteration)

#Generator in Python: :Pythongeneratorsareasimplewayofcreating
##  iterators. All the work we mentioned above is automatically handled by generators in Python.
##  ● Itusesayield statement instead of a return statement
print(next(number))  

def even_generetor(max):
    n = 2
    while n<=max:
        yield n
        n+=2
number = even_generetor(4)  
print(next(number))  
print(next(number))  

def add(a,b):
    def result():
        sum = a+b
        print(sum)
    return()
add(4,5)

# #closure function: Afunctionthatisdefinedinsideanotherfunction
#  is known as a nested function. Nested functions are able to access variables of the
#  enclosing scope(Outer function).
#  ● InPython,these non-local variables can be accessed only within their
#  scope and not outside their scope.
#  ● AClosureisafunction object that remembers values in enclosing
#  scopes(Outer function) even if they are not present in memory
def outerfunction(text): # this is parent function
    def innerfunction():  #child function
        print(text)
    return innerfunction
a= outerfunction("hello")  #call outer function
del outerfunction #deleting outer function

