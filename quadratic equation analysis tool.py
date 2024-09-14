from tkinter import *
from tkinter import messagebox as m_box
import os
import cmath
os.system('cls')

root = Tk()
root.title('Quadratics Solver')
root.geometry("800x400")
root.attributes('-toolwindow', True)

a = IntVar()
b = IntVar()
c = IntVar()

label = Label(root, text='QUADRATIC SOLVER', fg='black',font=('Consolas',24))
label.grid(row=0, column=1, padx=50, pady=40, sticky=W)

labelA = Label(root,text='Enter A value: ', fg='blue',font=('Consolas',15))
labelA.grid(row=1, column=0, padx=20, pady=10)
textboxA = Entry(root, textvariable=a, fg='black', font=('Consolas',14))
textboxA.grid(row=1, column=1, sticky=W)

labelB = Label(root,text='Enter B value: ', fg='blue',font=('Consolas',15))
labelB.grid(row=2, column=0, padx=20, pady=10)
textboxB = Entry(root, textvariable=b, fg='black', font=('Consolas',14))
textboxB.grid(row=2, column=1, sticky=W)

labelC = Label(root,text='Enter C value: ', fg='blue',font=('Consolas',15))
labelC.grid(row=3, column=0, padx=20, pady=10)
textboxC = Entry(root, textvariable=c, fg='black', font=('Consolas',14))
textboxC.grid(row=3, column=1, sticky=W)

answerLabel = Label(root,fg='green', font=('Consolas',14))
answerLabel.grid(row=5, column=1, sticky=W, pady=10)

rootLabel = Label(root, fg='blue', font=('Consolas', 14))
rootLabel.grid(row=6, column=1, sticky=W, pady=10)


def quadratic():
    try:
        d = (b.get()**2) - (4*a.get()*c.get())

        sol1 = (-b.get()-cmath.sqrt(d))/(2*a.get())
        sol1_round = round(sol1.real, 2) + round(sol1.imag, 2) * 1j
        sol2 = (-b.get()+cmath.sqrt(d))/(2*a.get())
        sol2_round = round(sol2.real, 2) + round(sol2.imag, 2) * 1j

        answerLabel.config(text='The solutions are x1={0} and x2={1}' .format(sol1_round, sol2_round))
    except ZeroDivisionError:
        m_box.showerror('ZeroDivisionError:', 'The A value cannot be 0')

def rootCheck():
    d = (b.get()**2) - (4*a.get()*c.get())

    if a.get() == 0:
        rootLabel.config(text='')
    elif d > 0:
        rootLabel.config(text='Real and different roots')
    elif d == 0:
        rootLabel.config(text='Real and same roots')
    else:
        rootLabel.config(text='Complex roots')

def intCheck():
    try:
        int(a.get())
        int(b.get())
        int(c.get())
    except TclError:
        m_box.showerror('TclError: Invalid Integer', 'Enter a number, not a letter or a special character.')


calcButton = Button(root, command=lambda:[intCheck(), quadratic(), rootCheck()], text='Calculate', fg='red', font=('Consolas',14))
calcButton.grid (row=4, column=1, sticky=W)

closeButton = Button(root, command=lambda:[root.destroy()], text='Exit', fg='red', font=('Consolas', 14))
closeButton.grid (row=4, column=1, sticky=W, padx=130)



root.mainloop()