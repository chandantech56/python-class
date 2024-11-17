str = "programiz"
print("string is :", str)
print("print :", str[3])
print(str[1:5]) #slicing: slicing is a technique that allows you to retrieve specific parts, or "slices," of sequences such as strings, lists, tuples, or other iterable objects. 
print(str[5:-2])
# print(str[10]) # error: out of charactor
print(str)
str = "python" # replace all values but not replace one character in string. bcz string is a immutable.
print(str)
# length methods
txt1 = "python class starts at 7am"
print(txt1)
print(len(txt1))
# enumerate() function : print data index number with string charactor on by one.
txt2 = "python"
txt3 = list(enumerate(txt2)) #print index number with character name.
print("txt3:", txt3) # out put: txt3: [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]

#mutable: number, integer,float,
#immutable: string,