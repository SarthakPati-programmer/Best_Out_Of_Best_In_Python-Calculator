from tkinter import *
from math import *
def btnclick(nums):
    try:
        global operator
        operator = operator + str(nums)
        text_input.set(operator)
    except Exception:
        text_input.set("Input Error!!!")
# This function will allow users to click on a button and it will display that on screen of calculator.
# text_input is a variable being used to print values on calculator screen.
# Operator is an empty variable being used to assign new values.
def btncleardis():
    global operator
    try:
        operator = ""
        text_input.set("")
    except Exception:
        text_input.set("Input Error!!!")
# This function clears the display.
def btndecimal():
    global operator
    try:
        s="."
        operator=operator+str(s)
        text_input.set(operator)
    except Exception:
        text_input.set("Input Error!!!")
#This will implement the decimal button.
def square():
    global operator
    try:
        o="**2"
        operator=str(round(eval(operator+o),5))
        text_input.set(operator)
    except Exception:
        text_input.set("Input Error!!!")
# This will do square of numbers.
def power():
    global operator
    try:
        po="**"
        operator=operator+po
        text_input.set("^")
    except Exception:
        text_input.set("Input Error!!!")
# This will set the power/exponent.
def sqroot():
    global operator
    try:
        so="**(1/2)"
        operator=operator+so
        text_input.set("√")
    except Exception:
        text_input.set("Input Error!!!")
# This is for square root button.
def percent():
    global operator
    try:
        mn="/100"
        operator=operator+mn
        text_input.set("%")
    except Exception:
        text_input.set("Input Error!!!")
# Percentage button`s function.
def tenpow():
    global operator
    try:
        mno="*(10)**"
        operator=operator+mno
        text_input.set("*10^x")
    except Exception:
        text_input.set("Input Error!!!")
# This is for scientific *10 to the power n.
def facto():
    global operator, op
    try:
        a=1
        for i in range(1,(int(operator)+1)):
            if operator==0:
                a=1
            else:
                a=a*i
        sumup=a
        if int(operator)>=0:
            text_input.set(sumup)
            op=sumup
        else:
            text_input.set("Input Error!!!")
    except Exception:
        text_input.set("Input Error!!!")
    operator=""
# Factorial button will use this function.
def pie():
    global operator
    import math
    try:
        operator=operator+str(math.pi)
        text_input.set("π")
    except Exception:
        text_input.set("Input Error!!!")
# It is used to obtain π
def tpie():
    global operator
    import math
    try:
        operator=operator+str(2*math.pi)
        text_input.set("2π")
    except Exception:
        text_input.set("Input Error!!!")
# This will give 2π
def eul():
    global operator
    import math
    try:
        operator=operator+str(math.e)
        text_input.set("e")
    except Exception:
        text_input.set("Input Error!!!")
# This function gives euler`s number e
def sine():
    global operator,op
    import math
    try:
        sumup=str(round(sin(radians(int(operator))),5))
        op=sumup
        text_input.set(sumup)
    except Exception:
        text_input.set("Input Error!!!")
    operator=""
# Returns Sine of an angle
def cosine():
    global operator,op
    import math
    try:
        sumup=str(round(cos(radians(int(operator))),5))
        op=sumup
        text_input.set(sumup)
    except Exception:
        text_input.set("Input Error!!!")
    operator=""
# Returns Cosine of an angle
def tangent():
    global operator,op
    import math
    try:
        sumup=str(round(tan(radians(int(operator))),5))
        op=sumup
        text_input.set(sumup)
    except Exception:
        text_input.set("Input Error!!!")
    operator=""
# Returns Tangent of an angle
def croot():
    global operator,op
    try:
        sumup=str(round(eval(operator+"**(1/3)"),5))
        op=sumup
        text_input.set(sumup)
    except Exception:
        text_input.set("Input Error!!!")
# Returns cube root of a number
def btnEqualsInput():
        global operator,op
        try:
            sumup =str(round(eval(operator),5))
            text_input.set(sumup)
            op=sumup
        except Exception:
            text_input.set("Input Error!!!")
        operator = ""
# Equal to operator is being assingned.
# Round function will round up the answer to desired places of decimal.
# Try..Except prevents calculation error in strings and division by zero.
def His():
    global op, operator
    try:
        operator=operator+str(op)
        text_input.set(operator)
    except Exception:
        text_input.set("Input Error!!!")
# It Will show the previous result obtained(History).
cal = Tk()
cal.title("Calculator")
# Tiltle is being given
operator = ""
# Empty operator
n=""
text_input = StringVar()
# It will hold the display value.
txtDisplay=Entry(cal,font=('aerial',20,'bold'),textvariable=text_input,bd=30,fg="red",insertwidth=1,bg="Indigo",width=62,justify='right').grid(columnspan=16)
# This will be used to show display.
# fg=textcolour of output
# Font`ll show font size, style etc.
# textvariable is the input command where text_input is assigned.
# bd=display box size
# insert width determines the width of the outer box(excluding display)
# bg=Background colour
# justify is set as right
# columnspan=width of display box
# Width=Width of the input box
btn1=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="0 ",bg='Dark Blue',command=lambda:btnclick(0)).grid(row=1,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="1 ",bg='Dark Blue',command=lambda:btnclick(1)).grid(row=1,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="2 ",bg='Dark Blue',command=lambda:btnclick(2)).grid(row=1,column=2)
btn4=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" + ",bg='Dark Blue',command=lambda:btnclick("+")).grid(row=1,column=3)
btn5=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="3 ",bg='Dark Blue',command=lambda:btnclick(3)).grid(row=2,column=0)
btn6=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="4 ",bg='Dark Blue',command=lambda:btnclick(4)).grid(row=2,column=1)
btn7=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="5 ",bg='Dark Blue',command=lambda:btnclick(5)).grid(row=2,column=2)
btn8=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" - ",bg='Dark Blue',command=lambda:btnclick("-")).grid(row=2,column=3)
btn9=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="6 ",bg='Dark Blue',command=lambda:btnclick(6)).grid(row=3,column=0)
btn10=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="7 ",bg='Dark Blue',command=lambda:btnclick(7)).grid(row=3,column=1)
btn11=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="8 ",bg='Dark Blue',command=lambda:btnclick(8)).grid(row=3,column=2)
btn12=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" * ",bg='Dark Blue',command=lambda:btnclick("*")).grid(row=3,column=3)
btn13=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="9 ",bg='Dark Blue',command=lambda:btnclick(9)).grid(row=4,column=0)
btn14=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" . ",bg='Dark Blue',command=lambda:btndecimal()).grid(row=4,column=2)
btn15=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="   %   ",bg='Dark Blue',command=lambda:percent()).grid(row=2,column=6)
btn16=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" / ",bg='Dark Blue',command=lambda:btnclick("/")).grid(row=4,column=3)
btn17=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" C ",bg='Dark Blue',command=lambda:btncleardis()).grid(row=1,column=4)
btn18=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" = ",bg='Dark Blue',command=lambda:btnEqualsInput()).grid(row=2,column=4)
btn19=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" ( ",bg='Dark Blue',command=lambda:btnclick("(" )).grid(row=3,column=4)
btn20=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" ) ",bg='Dark Blue',command=lambda:btnclick(")")).grid(row=4,column=4)
btn21=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" ^ ",bg='Dark Blue',command=lambda:power()).grid(row=1,column=5)
btn22=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="2√",bg='Dark Blue',command=lambda:sqroot()).grid(row=3,column=5)
btn23=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="^2",bg='Dark Blue',command=lambda:square()).grid(row=2,column=5)
btn24=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="*10^x",bg='Dark Blue',command=lambda:tenpow()).grid(row=1,column=6)
btn25=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="His",bg='Dark Blue',command=lambda:His()).grid(row=4,column=8)
btn26=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="G.I.F",bg='Dark Blue',command=lambda:btnclick("//")).grid(row=1,column=7)
btn27=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" MOD ",bg='Dark Blue',command=lambda:btnclick("%")).grid(row=3,column=6)
btn28=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text=" Fact! ",bg='Dark Blue',command=lambda:facto()).grid(row=4,column=6)
btn29=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="00",bg='Dark Blue',command=lambda:btnclick("00")).grid(row=4,column=1)
btn30=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="   π   ",bg='Dark Blue',command=lambda:pie()).grid(row=2,column=7)
btn31=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="   e   ",bg='Dark Blue',command=lambda:eul()).grid(row=3,column=7)
btn32=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="2π__",bg='Dark Blue',command=lambda:tpie()).grid(row=4,column=7)
btn33=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="sin",bg='Dark Blue',command=lambda:sine()).grid(row=1,column=8)
btn34=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="cos",bg='Dark Blue',command=lambda:cosine()).grid(row=2,column=8)
btn35=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="tan",bg='Dark Blue',command=lambda:tangent()).grid(row=3,column=8)
btn36=Button(cal,padx=16,pady=16,bd=8,fg='Red',font=('aerial',20,'bold'),text="3√",bg='Dark Blue',command=lambda:croot()).grid(row=4,column=5)
# padx=length of button in its x axis and pady=length of button in its y axis.
# text shows the value in its corresponding button.
# command gives a command to the calculator when that button is pressed.
# grid is used to make buttons of the desired size.
cal.mainloop()
# mainloop is made to run and calculator does its work.
quit(0)