# PASSWORD GENERATE
# import string, random
# string_lower = list(string.ascii_lowercase)
# string_upper = list(string.ascii_uppercase)
# integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# belgi = '!@#$%^&*()_-+=/*'
# belgi_list = []
#
# for i in belgi:
#     belgi_list.append(i)
#
# list = string_upper + string_lower + integer + belgi_list
# new_list = []
# for i in list:
#     new_list.append(random.choice(list))
# password = ""
# for i in range(8):
#     password += str(random.choice(new_list))
#
# with open('qanaqadir.txt', 'a') as file:
#     file.write('parol:' + password + '\n')
# print(f"parol: {password}")
import tkinter
# REAL TIME PRINT
# import time
# import sys
#
# a = 'hello'
# string = list(string.ascii_lowercase)
# for i in string:
#     for l in a:
#         if l == i:
#             print(i, end='')
#             sys.stdout.flush()
#             time.sleep(1)
#             print('\t',)
#         else: continue
# print(string)


# CALCULATOR
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
# root.geometry("250x300")
# root.resizable(False, False)

text_var = tk.StringVar()
calculation = ""
text_result = tkinter.Text(root, height=5, width=30)
text_result.grid(columnspan=4, row=0)


def clear_f():
    global calculation
    calculation = ""
    text_result.delete('1.0', 'end')

def set_value_by_button1(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete('0.0', 'end')
    text_result.insert('1.0', calculation)

def calculation_eval():
    try:
        global calculation
        total = str(eval(calculation))
        text_result.delete('1.0', 'end')
        text_result.insert('1.0', total)
        calculation = ''
    except:
        clear_f()
        text_result.insert('1.0', 'error')

def calculation_clear():
    try:
        global calculation
        calculation = calculation[:len(calculation) - 1]
        text_result.delete('1.0', 'end')
        text_result.insert('1.0', calculation)
    except:
        pass

def clear_display():
    try:
        global calculation
        calculation = ''
        text_result.delete('1.0', 'end')
        text_result.insert('1.0', calculation)
    except:
        pass

def add_minus():
    try:
        global calculation
        calculation = "-" + calculation
        text_result.delete('1.0', 'end')
        text_result.insert('1.0', calculation)
    except:
        pass

button1 = Button(root, text='-', command=add_minus, width=20, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(columnspan=5, row=6)

button1 = Button(root, text='C', command=clear_display, width=5, height=2,  fon=('arial', 14), bg="#F72C00", fg="white")
button1.grid(column=0, row=1, padx=2, pady=2)
button1 = Button(root, text='__/', command=calculation_clear, width=5, height=2, fon=('arial', 14), bg="#F72C00", fg="white")
button1.grid(column=1, row=1, padx=1, pady=2)
button1 = Button(root, text='+', command=lambda: set_value_by_button1("+"), width=5, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(column=2, row=1, padx=2, pady=2)
button1 = Button(root, text='-', command=lambda: set_value_by_button1("-"), width=5, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(column=3, row=1, padx=1, pady=2)

button1 = Button(root, text=7, command=lambda: set_value_by_button1("7"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=0, row=2)
button1 = Button(root, text=8, command=lambda: set_value_by_button1("8"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=1, row=2)
button1 = Button(root, text=9, command=lambda: set_value_by_button1("9"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=2, row=2)
button1 = Button(root, text='*', command=lambda: set_value_by_button1("*"), width=5, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(column=3, row=2)

button1 = Button(root, text=4, command=lambda: set_value_by_button1("4"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=0, row=3)
button1 = Button(root, text=5, command=lambda: set_value_by_button1("5"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=1, row=3)
button1 = Button(root, text=6, command=lambda: set_value_by_button1("6"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=2, row=3)
button1 = Button(root, text='/', command=lambda: set_value_by_button1("/"), width=5, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(column=3, row=3)

button1 = Button(root, text=1, command=lambda: set_value_by_button1("1"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=0, row=4)
button1 = Button(root, text=2, command=lambda: set_value_by_button1("2"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=1, row=4)
button1 = Button(root, text=3, command=lambda: set_value_by_button1("3"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=2, row=4)

button1 = Button(root, text='(', command=lambda: set_value_by_button1("("), width=5, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(column=3, row=4)
button1 = Button(root, text=')', command=lambda: set_value_by_button1(")"), width=5, height=2, fon=('arial', 14), bg="#DE8708", fg="white")
button1.grid(column=3, row=5)

button1 = Button(root, text=0, command=lambda: set_value_by_button1("0"), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=0, row=5)
button1 = Button(root, text='.', command=lambda: set_value_by_button1("."), width=5, height=2, fon=('arial', 14), bg="#1A190B", fg="white")
button1.grid(column=1, row=5)

button1 = Button(root, text='=', command=calculation_eval, width=5, height=2, fon=('arial', 14), bg="#FEF400", fg="white")
button1.grid(column=2, row=5)

root.mainloop()
