def sum(a,b):
    sum= a+b   
    print(sum)
sum (5,4)

#ReGex ([]- square bracket)
import re
pattern='[abc]'
test_string = 'abcd3'
result = re.match(pattern,test_string)
print(result) #// <re.Match object; span=(0, 1), match='a'>

import re
pattern='[cbc]'
test_string = 'abcd3'
result = re.match(pattern,test_string)
print(result) #// none

import re
pattern='..'
test_string = 'abcd'
result = re.match(pattern,test_string)
print(result) #// <re.Match object; span=(0, 2), match='ab'>


import re
pattern='...'
test_string = 'abcd'
result = re.match(pattern,test_string)
print(result) # // <re.Match object; span=(0, 3), match='abc'>

#tkinter: 

from tkinter import *  
parent = Tk()  
parent.title("Login Page")
parent.geometry("400x400")
name = Label(parent,text = "Enter the Name").grid(row = 0, column = 0)  
e1 = Entry(parent).grid(row = 0, column = 1)  
password = Label(parent,text = "Enter the Password").grid(row = 1, column = 0)  
e2 = Entry(parent).grid(row = 1, column = 1)  
submit = Button(parent, text = "Submit Now").grid(row = 3, column = 1)  
parent.mainloop()

from tkinter import *
import tkinter.messagebox as box
#------------------------------------------------


def dialog1():
    username=entry1.get()
    password = entry2.get()
    if (username == 'admin' and  password == 'secret'):
        box.showinfo('info','Correct Login')
    else:
        box.showinfo('info','Invalid Login')

window = Tk()
window.title("Login Page")
window.geometry("500x500")

frame = Frame(window)

Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)


Label2 = Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)

btn = Button(frame, text = 'Check Login',command = dialog1)

btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()
#_____________________________________________________

from tkinter import *  
parent = Tk()  
parent.title("Button Page")
parent.geometry("500x500")
redbutton = Button(parent, text = "Red", fg = "red")  
redbutton.pack( side = LEFT)  
greenbutton = Button(parent, text = "Black", fg = "black")  
greenbutton.pack( side = RIGHT )  
bluebutton = Button(parent, text = "Blue", fg = "blue")  
bluebutton.pack( side = TOP )  
blackbutton = Button(parent, text = "Green", fg = "red")  
blackbutton.pack( side = BOTTOM)  
parent.mainloop()