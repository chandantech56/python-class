#File : file is collection of data. 

# mode: Specifies the purpose for opening the file:
# 'r': Read (default mode).
# 'w': Write (overwrites if the file exists).
# 'a': Append.
# 'b': Binary mode (use with 'r', 'w', or 'a').
# 'x': Create a new file (fails if the file exists).
# 't': Text mode (default, used with 'r', 'w', or 'a').

with open("hello_world.txt", "w") as f:
    f.write("Hello world!, How are you. ")
    print(f)

    # read mode
with open("hello_world.txt","r") as r:
    c=r.read()
    print(c)
#append 
with open("hello_world.txt", "a") as a:
    a.write("Welcome to india!!"   )
    print(a)

