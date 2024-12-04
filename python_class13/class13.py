#File : file is collection of data. 
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

