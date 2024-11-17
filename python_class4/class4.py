institute="besent technology"
for char in institute:
    print("institute name character wise: ", char)
    # if(char =="S"):
            # count+=1
            # print("number of letter t is:", count)

text= "python"
print("p" in text)
print("law" in text)
print("hon" in text)

text = "HELLO,WORLD" # for method lower case (text.lower())
result= text.lower()
print("ther result is:" , result)

text = "hello world" #for upper case (.upper)
result= text.upper()
print("the result is:" , result)

text = "hello world"
result= text.replace("hello", "hi") #replace methods(.replace)
print("change letter hello:", result)
result= text.replace("o", "m")
print("change letter o:", result)

text= "hello world" # find methods(.find())
result= text.find("w")
print("find char w is:", result)

text= "this is a python class" #split methods (.splite())
result= text.split()
print(result)
