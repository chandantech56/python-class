#Dictionary example
student_details = {"name":"David", "subject":"python","subject2":"SQL", "marks":95,"section":"A"}
print(student_details)

#add methods: add values in sets
student={'david','sham','rahul','vinay'}
student.add('aniket')
print(student)

#update methods: add 2 element values in set 
language1 = {"python","sql","java","html"}
language2 = ["java_script","react","python","css"]
language1.update(language2)
print(language1)
# .discard: delete particular values 
student={'david','sham','rahul','vinay','manoj'}
student.discard("sham")
print(student)
#same method work .discard and remove key word...
student.remove("rahul")
print(student)

#clear : this methods use clear the entire values.
student.clear()
print(student)
#union methods in set
a1 = {"rose","sunflower","sham",}
a2 = {"jasmine","sunflower"}
flower= a1.union(a2)
print(flower)

#intersection (|) methods: result print only common(match values) values..
flower = a1|a2
print(flower)

#Result print only common element
flower= a2.intersection(a1) 
print(flower)


#if else statment
score= int(input("enter your score: "))
if score>=20:
    print("you are pass")
else:
    print("you are faild")
#program for driving pass age
age = int(input("enter your age: ")) 
if age>=18:
    print(f"you are {age} years old,  so you are  eligible for drive")    
elif age<18:
    print(f"your age is {age}.so you are not eligible for drive")
elif age >=60:
    print(f"your age is {age}, so your age out of drive")    
else:
    print(f"your age is {age}, so you are not eligible for drive")

