from tkinter import *
import doArithmetic

expr = ""
clr = True
input_field = None

def createLayout(w):
    #Create Input
    global equation
    global input_field
    input_field = Entry(w, textvariable=equation)
    input_field.grid(columnspan=5,sticky=E+W,padx=10)
    equation.set("Enter expression")
    
    # Create Num Buttons
    
    button1 = Button(w, text="1", fg="#000",
                command=lambda: press(1), height=1, width=5)
    
    button1.grid(row=2, column=0)
    
    button2 = Button(w, text="2", fg="#000",
                command=lambda: press(2), height=1, width=5)
    
    button2.grid(row=2, column=1)
    
    button3 = Button(w, text="3", fg="#000",
                command=lambda: press(3), height=1, width=5)
    
    button3.grid(row=2, column=2)
    
    button4 = Button(w, text="4", fg="#000",
                command=lambda: press(4), height=1, width=5)
    
    button4.grid(row=3, column=0)
    
    button5 = Button(w, text="5", fg="#000",
                command=lambda: press(5), height=1, width=5)
    
    button5.grid(row=3, column=1)
    
    button6 = Button(w, text="6", fg="#000",
                command=lambda: press(6), height=1, width=5)
    
    button6.grid(row=3, column=2)
    
    button7 = Button(w, text="7", fg="#000",
                command=lambda: press(7), height=1, width=5)
    
    button7.grid(row=4, column=0)
    
    button8 = Button(w, text="8", fg="#000",
                command=lambda: press(8), height=1, width=5)
    
    button8.grid(row=4, column=1)
    
    button9 = Button(w, text="9", fg="#000",
                command=lambda: press(9), height=1, width=5)
    
    button9.grid(row=4, column=2)
    
    button0 = Button(w, text="0", fg="#000",
                command=lambda: press(0), height=1, width=5)
    
    button0.grid(row=5, column=1)
    
    buttondec = Button(w, text=".", fg="#000",
                command=lambda: press("."), height=1, width=5)
    
    buttondec.grid(row=5, column=0)
    
    buttondec = Button(w, text="=", fg="#000",
                command=lambda: press("="), height=1, width=5)
    
    buttondec.grid(row=5, column=2)
    
    
    buttonmul = Button(w, text="x", fg="#000",
                command=lambda: press("x"), height=1, width=5)
    
    buttonmul.grid(row=2, column=4)
    
    buttonsub = Button(w, text="-", fg="#000",
                command=lambda: press("-"), height=1, width=5)
    
    buttonsub.grid(row=3, column=4)
    
    buttondec = Button(w, text="+", fg="#000",
                command=lambda: press("+"), height=1, width=5)
    
    buttondec.grid(row=4, column=4)
    
    buttondec = Button(w, text="/", fg="#000",
                command=lambda: press("/"), height=1, width=5)
    
    buttondec.grid(row=5, column=4)
    
def press(n):
    global expr #ref to global var
    global clr
    numBuf = 0.0 #buffer to support values of 10+, decimals, etc
    
    if clr:
        clr = False
        expr = ""
        
    if (n=="="):
        expr = doArithmetic.parseArithmetic(equation.get())
        clr = True
    else:
        expr = expr + str(n)
    
    equation.set(expr)

## Main

#Create new master
window = Tk()

#Instantiate equation for global use
equation = StringVar()

#Set title, create window
window.title("Simple Calc")
createLayout(window)

## Main Loop
window.mainloop()
