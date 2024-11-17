a= "python "
b= "programiz"
print(a+ b) #cancatination(+)
#
str1= "hello "
str2 = "world!"
print("str1 + str2= ", str1 + str2)

str1 = "python is " #for spacing given one spaces {"values____(space) "}
str2 = "programing language"
print("str1 + str2=", str1 + str2)

str1= "hello"
str2 = "world!"
print("str1 * 3 = " , str1 * 3) # (*asetric operator)

text = "python" #for loops
for char in text: #for and in is a reserved keyword(for loops), text is a variable and char is a data types.
    print(char),

    count=0
    for letter in "hello world":
        print(letter)
        if(letter=="l"):
            count+=1
            print("number of letter l is:", count)

            count=0
            for char in "chandan":
                if(char=="n"):
                    count+=1
                    print("n" ,count)

                    num = [1,4,9,16,25,36,49,]
                    for list in num:
                        print(list)

                        # for i in range(1, 100): # Range function (start, stop, step)
                        #     print(i)

                        n= 5
                        for i in range(n+1):
                            print(i)