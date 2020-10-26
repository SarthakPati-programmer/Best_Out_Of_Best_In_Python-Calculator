from tkinter import *
from math import *
def btnclick(nums):
    global operator
    operator = operator + str(nums)
    text_input.set(operator)
# This function will allow users to click on a button and it will display that on screen of calculator.
# text_input is a variable being used to print values on calculator screen(see line 67).
# Operator is an empty variable being used to assign new values(see line 65).
def btncleardis():
    global operator
    operator = ""
    text_input.set("")
# This function clears the display(see line 95).
def btndecimal():
    s="."
    global operator
    operator=operator+str(s)
    text_input.set(operator)
#This will implement the decimal button(see line 92).
def square():
    o="**2"
    global operator
    operator=operator+o
    text_input.set(operator)
# This will do square of numbers(see line 101).
def power():
    po="**"
    global operator
    operator=operator+po
    text_input.set("^")
# This will set the power/exponent(see line 99).
def sqroot():
    so="**(1/2)"
    global operator
    operator=operator+so
    text_input.set("√")
# This is for square root button(see line 100).
def percent():
    mn="/100"
    global operator
    operator=operator+mn
    text_input.set("%")
# Percentage button`s function(see line 93).
def tenpow():
    mno="*(10)**"
    global operator
    operator=operator+mno
    text_input.set("*10^x")
# This is for scientific *10 to the power n(see line 102).
def btnEqualsInput():
        global operator
        try:
            sumup =str(round(eval(operator),5))
            text_input.set(sumup)
        except Exception:
            text_input.set("Input Error!!!")
        operator = ""
# Equal to operator is being assingned(see line 66).
# Round function will round up the answer to desired places of decimal(see line 62).
# Try..Except prevents calculation error in strings and division by zero.
cal = Tk()
cal.title("Calculator")
# Tiltle is being given
operator = ""
# Empty operator
text_input = StringVar()
# It will hold the display value.
txtDisplay=Entry(cal,font=('aerial',20,'bold'),textvariable=text_input,bd=30,fg="red",insertwidth=1,bg="Light green",width=50,justify='right').grid(columnspan=16)
# This will be used to show display.
# fg=textcolour of output
# Font`ll show font size, style etc.
# textvariable is the input command where text_input is assigned.
# bd=display box size
# insert width determines the width of the outer box(excluding display)
# bg=Background colour
# justify is set as right
# columnspan=width of display box
btn1=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="0",bg='Yellow',command=lambda:btnclick(0)).grid(row=1,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="1",bg='Yellow',command=lambda:btnclick(1)).grid(row=1,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="2",bg='Yellow',command=lambda:btnclick(2)).grid(row=1,column=2)
btn4=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="+",bg='Yellow',command=lambda:btnclick("+")).grid(row=1,column=3)
btn5=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="3",bg='Yellow',command=lambda:btnclick(3)).grid(row=2,column=0)
btn6=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="4",bg='Yellow',command=lambda:btnclick(4)).grid(row=2,column=1)
btn7=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="5",bg='Yellow',command=lambda:btnclick(5)).grid(row=2,column=2)
btn8=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="-",bg='Yellow',command=lambda:btnclick("-")).grid(row=2,column=3)
btn9=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="6",bg='Yellow',command=lambda:btnclick(6)).grid(row=3,column=0)
btn10=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="7",bg='Yellow',command=lambda:btnclick(7)).grid(row=3,column=1)
btn11=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="8",bg='Yellow',command=lambda:btnclick(8)).grid(row=3,column=2)
btn12=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="*",bg='Yellow',command=lambda:btnclick("*")).grid(row=3,column=3)
btn13=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="9",bg='Yellow',command=lambda:btnclick(9)).grid(row=4,column=0)
btn14=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text=".",bg='Yellow',command=lambda:btndecimal()).grid(row=4,column=1)
btn15=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="%",bg='Yellow',command=lambda:percent()).grid(row=4,column=2)
btn16=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="/",bg='Yellow',command=lambda:btnclick("/")).grid(row=4,column=3)
btn17=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="C",bg='Yellow',command=lambda:btncleardis()).grid(row=1,column=4)
btn18=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="=",bg='Yellow',command=lambda:btnEqualsInput()).grid(row=2,column=4)
btn19=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="(",bg='Yellow',command=lambda:btnclick("(" )).grid(row=3,column=4)
btn20=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text=")",bg='Yellow',command=lambda:btnclick(")")).grid(row=4,column=4)
btn21=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="^",bg='Yellow',command=lambda:power()).grid(row=1,column=5)
btn22=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="2√",bg='Yellow',command=lambda:sqroot()).grid(row=2,column=5)
btn23=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="^2",bg='Yellow',command=lambda:square()).grid(row=3,column=5)
btn24=Button(cal,padx=16,pady=16,bd=8,fg='blue',font=('aerial',20,'bold'),text="*10^x",bg='Yellow',command=lambda:tenpow()).grid(row=4,column=5)
# padx=length of button in its x axis and pady=length of button in its y axis
# text shows the value in its corresponding button
# command gives a command to the calculator when that button is pressed
# grid is used to make buttons of the desired size
cal.mainloop()
# mainloop is made to run and calculator does its work.