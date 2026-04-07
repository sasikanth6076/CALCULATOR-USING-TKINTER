#importing 
from tkinter import *


#GUI Interaction
window = Tk()
window.title("CALCULATOR USING TKINTER")
window.geometry("300x350")


#Entry Box
entry_box = Entry(window, width=50, borderwidth=5)
entry_box.place(x=0, y=0)


#click function
def click(num):
    result = entry_box.get()
    entry_box.insert(END, str(num))

#Number Buttons
button_1 = Button(window, text="1", padx=25, pady=20, command=lambda: click(1))
button_1.place(x=0, y=50)
button_2 = Button(window, text="2", padx=25, pady=20, command=lambda: click(2))
button_2.place(x=75, y=50)
button_3 = Button(window, text="3", padx=25, pady=20, command=lambda: click(3))
button_3.place(x=150, y=50)
button_4 = Button(window, text="4", padx=25, pady=20, command=lambda: click(4))
button_4.place(x=0, y=125)
button_5 = Button(window, text="5", padx=25, pady=20, command=lambda: click(5))
button_5.place(x=75, y=125)
button_6 = Button(window, text="6", padx=25, pady=20, command=lambda: click(6))
button_6.place(x=150, y=125)
button_7 = Button(window, text="7", padx=25, pady=20, command=lambda: click(7))
button_7.place(x=0, y=200)
button_8 = Button(window, text="8", padx=25, pady=20, command=lambda: click(8))
button_8.place(x=75, y=200)
button_9 = Button(window, text="9", padx=25, pady=20, command=lambda: click(9))
button_9.place(x=150, y=200)
button_0 = Button(window, text="0", padx=25, pady=20, command=lambda: click(0))
button_0.place(x=0, y=275)


#Math Operator Buttons
#addition
def add():
    first_num = entry_box.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    entry_box.delete(0, END)

button_add = Button(window, text = '+', padx=25, pady=20, command  = add)
button_add.place(x=225, y=125)


#subtraction
def sub():
    first_num = entry_box.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    entry_box.delete(0, END)

button_sub = Button(window, text = '-', padx=26.5, pady=20, command = sub)
button_sub.place(x=225, y=200)


#multiplication
def mult():
    first_num = entry_box.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    entry_box.delete(0, END)

button_mult = Button(window, text = 'x', padx=25, pady=20, command  = mult)
button_mult.place(x=150, y=275)


#Division
def div():
    first_num = entry_box.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    entry_box.delete(0, END)

button_divide = Button(window, text = '/', padx=25, pady=20, command = div)
button_divide.place(x=75, y=275)


#Other Buttons
#Equal Button
def equal():
        second_num = entry_box.get()
        entry_box.delete(0, END)

        #Handling division by zero error by try except method
        try:
            if math == 'addition':
                entry_box.insert(0, f_num + int(second_num))
            elif math == 'subtraction':
                entry_box.insert(0, f_num - int(second_num))
            elif math == 'multiplication':
                entry_box.insert(0, f_num * int(second_num))   
            elif math == 'division':
                    entry_box.insert(0, f_num / int(second_num))

        except ZeroDivisionError:
            entry_box.insert(0, "Error: Division by zero")
        

button_equal = Button(window, text = '=', padx=25, pady=20, command = equal)
button_equal.place(x=225, y=275)


#Backspace Button
def back():
    entry_box.delete(len(entry_box.get())-1, END)

button_back = Button(window, text="<-", padx=23, pady=3, command= back)
button_back.place(x=225, y=50)


#Clear Everything Button
def clear():
    entry_box.delete(0, END)

button_clear = Button(window, text="CE", padx=22, pady=3, command= clear)
button_clear.place(x=225, y=85)


#mainloop
mainloop()
