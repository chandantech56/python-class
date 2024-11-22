#tupple(): tupple always values asign in paranthesis().

my_tupple=()
print(my_tupple)
my_tupple= (1,21,3)
print(my_tupple)

my_tupple = (1,"hello",20.25) #tupple with mix datatypes.
print(my_tupple)

my_tupple= ("mouse",[8,4,6],(1,2,3)) #nested tupple.
print(my_tupple)

 #packing tupple
my_tupple= 3,4.6,"dog"
print(my_tupple)

 #unpacked tupple
a,b,c= my_tupple
print(my_tupple)
print(a)
print(b)

my_tupple=("hello") 
print(type(my_tupple))
my_tupple= ("hello",) #tupple compalsary each value after given comma
print(type(my_tupple))

my_tupple= ("man",1,2,3,[9,5]) #nested tuple
my_tupple[3][0]= 4 # only list values change. but not change tupple values.
print(my_tupple)

atupple= ("tiger",28, "mango")
print(type(atupple))

#converting tupple to list 
aList= list(atupple)
print(aList)
print(type(aList))

#Deleting a Tuple:
#  ● Wecannotchangetheelements in a tuple. It means that we cannot delete or remove items from a tuple.
#  ● Deleting atuple entirely, however, is possible using the keyword del

# Changing a Tuple:
#  ● Unlikelists, tuples are immutable.
#  ● Thismeansthatelements of a tuple cannot be changed once they have been assigned. But,nested items can be changed.
#  ● Wecanalsoassignatuple to different values (reassignment).