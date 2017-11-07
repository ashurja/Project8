# Jamshed Ashurov
# 11/07/2017
# calculator.py
# This program makes a calculator


import tkinter
import math

root = tkinter.Tk()
root.title("Jamshed's Calculator: Thrive toward perfection")


def zero():
    """
    This function takes the value from the form and adds zero
    :return:
    """
    variable = anything.get()
    variable = variable + "0"
    anything.set(variable)


def one():
    """
    This function takes the value from the form and adds one
    :return:
    """
    variable = anything.get()
    variable = variable + "1"
    anything.set(variable)


def two():
    """
    This function takes the value from the form and adds two
    :return:
    """
    variable = anything.get()
    variable = variable + "2"
    anything.set(variable)


def three():
    """
    This function takes the value from the form and adds three
    :return:
    """
    variable = anything.get()
    variable = variable + "3"
    anything.set(variable)


def four():
    """
    This function takes the value from the form and adds four
    :return:
    """
    variable = anything.get()
    variable = variable + "4"
    anything.set(variable)


def five():
    """
    This function takes the value from the form and adds five
    :return:
    """
    variable = anything.get()
    variable = variable + "5"
    anything.set(variable)


def six():
    """
    This function takes the value from the form and adds six
    :return:
    """
    variable = anything.get()
    variable = variable + "6"
    anything.set(variable)


def seven():
    """
    This function takes the value from the form and adds seven
    :return:
    """
    variable = anything.get()
    variable = variable + "7"
    anything.set(variable)


def eight():
    """
    This function takes the value from the form and adds eight
    :return:
    """
    variable = anything.get()
    variable = variable + "8"
    anything.set(variable)


def nine():
    """
    This function takes the value from the form and adds nine
    :return:
    """
    variable = anything.get()
    variable = variable + "9"
    anything.set(variable)


def plus():
    """
    This function takes the value from the form and adds the plus sign to the value
    :return:
    """
    variable = anything.get()
    addition = variable + "+"
    anything.set(addition)


def minus():
    """
     This function takes the value from the form and adds the minus sign to the value
    :return:
    """
    variable = anything.get()
    addition = variable + "-"
    anything.set(addition)


def multiply():
    """
     This function takes the value from the form and adds the multiplication sign to the value
    :return:
    """
    variable = anything.get()
    addition = variable + "*"
    anything.set(addition)


def divide():
    """
     This function takes the value from the form and adds the division sign to the value
    :return:
    """
    variable = anything.get()
    addition = variable + "/"
    anything.set(addition)


def equal():
    """
     This function takes the value from the form and calculates the operation
    :return:
    """
    variable = anything.get()
    result = str(eval(variable))
    anything.set(result)


def log():
    """
     This function takes the value from the form finds its logarithm with the base 10
    :return:
    """
    variable = anything.get()
    logarithm = math.log10(float(variable))
    anything.set(str(logarithm))


def square():
    """
    This function takes the value from the form and squares it
    :return:
    """
    variable = anything.get()
    squa = (float(variable)) ** 2
    anything.set(squa)


def clear():
    """
     This function takes the value from the form and sets it to blank form
    :return:
    """
    anything.set("")

anything = tkinter.StringVar()
windowEntry = tkinter.Entry(root, width=15, textvariable=anything)
windowEntry.grid(row=1, column=1)

buttonFrame = tkinter.Frame(root)
buttonFrame.grid(row=2, column=1, columnspan=1)

square = tkinter.Button(buttonFrame, text="x^2", width=2, command=square)
square.grid(row=2, column=1)

log = tkinter.Button(buttonFrame, text="log", width=2, command=log)
log.grid(row=2, column=2)

multiply_button = tkinter.Button(buttonFrame, text="*", width=2, command=multiply)
multiply_button.grid(row=2, column=3)

plus_button = tkinter.Button(buttonFrame, text="+", width=2, command=plus)
plus_button.grid(row=2, column=4)

buttonFrame1 = tkinter.Frame(root)
buttonFrame1.grid(row=3, column=1, columnspan=1)

one_button = tkinter.Button(buttonFrame1, text="1", width=2, command=one)
one_button.grid(row=3, column=1)

two_button = tkinter.Button(buttonFrame1, text="2", width=2, command=two)
two_button.grid(row=3, column=2)

three_button = tkinter.Button(buttonFrame1, text="3", width=2, command=three)
three_button.grid(row=3, column=3)

minus_button = tkinter.Button(buttonFrame1, text="-", width=2, command=minus)
minus_button.grid(row=3, column=4)

buttonFrame2 = tkinter.Frame(root)
buttonFrame2.grid(row=4, column=1, columnspan=1)

four_button = tkinter.Button(buttonFrame2, text="4", width=2, command=four)
four_button.grid(row=4, column=1)

five_button = tkinter.Button(buttonFrame2, text="5", width=2, command=five)
five_button.grid(row=4, column=2)

six_button = tkinter.Button(buttonFrame2, text="6", width=2, command=six)
six_button.grid(row=4, column=3)

divide_button = tkinter.Button(buttonFrame2, text="/", width=2, command=divide)
divide_button.grid(row=4, column=4)

buttonFrame3 = tkinter.Frame(root)
buttonFrame3.grid(row=5, column=1, sticky="W")

nine_button = tkinter.Button(buttonFrame3, text="9", width=2, command=nine)
nine_button.grid(row=5, column=1)

eight_button = tkinter.Button(buttonFrame3, text="8", width=2, command=eight)
eight_button.grid(row=5, column=2)

seven_button = tkinter.Button(buttonFrame3, text="7", width=2, command=seven)
seven_button.grid(row=5, column=3)

equal_button = tkinter.Button(buttonFrame3, text="=", width=2, command=equal)
equal_button.grid(row=5, column=4)

buttonFrame4 = tkinter.Frame(root)
buttonFrame4.grid(row=6, column=1, sticky="W")

zero_button = tkinter.Button(buttonFrame4, text="0", width=2, command=zero)
zero_button.grid(row=6, column=1)

clear = tkinter.Button(buttonFrame4, text="clear", width=12, command=clear)
clear.grid(row=6, column=2)

root.bind("<Return>", lambda e: equal())

root.mainloop()
