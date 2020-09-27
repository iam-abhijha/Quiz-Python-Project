from tkinter import *
from math import *

window=Tk()
window.geometry("230x400")
window.minsize(230,400)
window.maxsize(230,400)
window.title("Calculator")

txt=StringVar()
expression=""
def sqroot():
    add=sqrt(int(expression))
    txt.set(add)

def click(num):
    global expression
    expression=expression + str(num)
    txt.set(expression)

def equal():
    try:
        global expression
        add=str(eval(expression))
        txt.set(add)

        expression=""
    except:
        txt.set("Error")
        expression=""

def clr():
    global expression
    length=len(txt.get())
    e1.delete(length-1,'end')

def clearall():
    global expression
    expression=""
    txt.set("")

f1=Frame(window,width=390,height=100,bg="white")
f1.grid(row=0,column=0)
#f1.pack(side=TOP)
f2=Frame(window,width=390,height=368,bg="grey")
f2.grid(row=1,column=0)
#f2.pack(side=BOTTOM)

l1=Label(f1,text="My Calculator",font=("Arial Bold",20))
l1.pack(side=TOP,expand=YES)

e1=Entry(f1,textvariable=txt,width=23,bd=10,font=("Arial Bold",12),
         fg="black",bg="light grey",relief=RIDGE,justify=RIGHT)

e1.pack(side=TOP)
e1.insert(0,"0")

button_1=Button(f2,text="1",padx=20,pady=20,command=lambda:click(1))
button_2=Button(f2,text="2",padx=20,pady=20,command=lambda:click(2))
button_3=Button(f2,text="3",padx=20,pady=20,command=lambda:click(3))
button_4=Button(f2,text="4",padx=20,pady=20,command=lambda:click(4))
button_5=Button(f2,text="5",padx=20,pady=20,command=lambda:click(5))
button_6=Button(f2,text="6",padx=20,pady=20,command=lambda:click(6))
button_7=Button(f2,text="7",padx=20,pady=20,command=lambda:click(7))
button_8=Button(f2,text="8",padx=20,pady=20,command=lambda:click(8))
button_9=Button(f2,text="9",padx=20,pady=20,command=lambda:click(9))
button_0=Button(f2,text="0",padx=20,pady=20,command=lambda:click(0))

button_clr=Button(f2,text="clr",padx=17,pady=20,command=clr)
button_clrall=Button(f2,text="clr/all",padx=8,pady=20,command=clearall)
button_equal=Button(f2,text="=",padx=20,pady=20,command=equal)
#button_clr=Button(f2,text="clr",padx=80,pady=20,command=clr)

button_add=Button(f2,text="+",padx=20,pady=20,command=lambda:click("+"))
button_sub=Button(f2,text="-",padx=20,pady=20,command=lambda:click("-"))
button_mul=Button(f2,text="*",padx=20,pady=20,command=lambda:click("*"))
button_div=Button(f2,text="/",padx=20,pady=20,command=lambda:click("/"))
button_dot=Button(f2,text=".",padx=20,pady=20,command=lambda:click("."))
button_pow=Button(f2,text="^",padx=20,pady=20,command=lambda:click("**"))
button_sqrot=Button(f2,text="√",padx=20,pady=20,command=sqroot)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add.grid(row=3,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=1,column=3)
button_div.grid(row=0,column=3)
button_dot.grid(row=4,column=2)
button_pow.grid(row=0,column=1)
button_sqrot.grid(row=0,column=2)


button_0.grid(row=4,column=1)
button_clr.grid(row=0,column=0)
button_equal.grid(row=4,column=3)
button_clrall.grid(row=4,column=0)

def Calculator():
    window.mainloop()