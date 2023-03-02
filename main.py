from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log

window = Tk()
screenSize = "279x442"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calcualtor")
#function
def about():
    messagebox.showinfo('About',"\n \n \n   tugas kalkulator   \n \n \n")

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def expand():
    if screenSize=="279x500":
        window.geometry("279x555")
    else:
        window.geometry("279x555")
def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)
#menubar
menubar = Menu(window,bg="black",fg="white")
filemenu = Menu(menubar, tearoff=0,bg="black",fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0,bg="black",fg="white")
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

expression = ""
inputText = StringVar()

inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="gray",
                    highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0,
                    justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack()

ac = PhotoImage(file = r"images\ac.png")
acimage = ac.subsample(4,4)
ac = Button(mainFrame, text="AC", fg="black", image=acimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clearAll()).grid(row=0, column=0, padx=1, pady=1)

clear = PhotoImage(file = r"images\clear.png")
clearimage = clear.subsample(4,4)
clear = Button(mainFrame, text="AC", fg="black", image=clearimage, bd=0, bg="black", cursor="hand1",
               command=lambda: clearButton()).grid(row=0, column=1, padx=1, pady=1)

divide = PhotoImage(file = r"images\divide.png")
divideimage = divide.subsample(4,4)
divide = Button(mainFrame, text="/", fg="white",image=divideimage, bd=0, bg="black", cursor="hand2",
                command=lambda: clickButton("/")).grid(row=0, column=2, padx=1, pady=1)


seven = PhotoImage(file = r"images\seven.png")
sevenimage = seven.subsample(4,4)
seven = Button(mainFrame, text="7", fg="black", image=sevenimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(7)).grid(row=1, column=0, padx=1, pady=1)

eight = PhotoImage(file = r"images\eight.png")
eightimage = eight.subsample(4,4)
eight = Button(mainFrame, text="8", fg="black", image=eightimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(8)).grid(row=1, column=1, padx=1, pady=1)

nine = PhotoImage(file = r"images\nine.png")
nineimage = nine.subsample(4,4)
nine = Button(mainFrame, text="9", fg="black", image=nineimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(9)).grid(row=1, column=2, padx=1, pady=1)

multi = PhotoImage(file = r"images\multi.png")
multiimage = multi.subsample(4,4)
multiply = Button(mainFrame, text="*", fg="white",image=multiimage, bd=0, bg="black", cursor="hand2",
                  command=lambda: clickButton("*")).grid(row=0, column=3, padx=1, pady=1)

four = PhotoImage(file = r"images\four.png")
fourimage = four.subsample(4,4)
four = Button(mainFrame, text="4", fg="black", image=fourimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(4)).grid(row=2, column=0, padx=1, pady=1)

five = PhotoImage(file = r"images\five.png")
fiveimage = five.subsample(4,4)
five = Button(mainFrame, text="5", fg="black", image=fiveimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(5)).grid(row=2, column=1, padx=1, pady=1)

six = PhotoImage(file = r"images\six.png")
siximage = six.subsample(4,4)
six = Button(mainFrame, text="6", fg="black", image=siximage, bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(6)).grid(row=2, column=2, padx=1, pady=1)

minus = PhotoImage(file = r"images\minus.png")
minusimage = minus.subsample(4,4)
minus = Button(mainFrame, text="-", fg="white",image=minusimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton("-")).grid(row=1, column=3, padx=1, pady=1)

one = PhotoImage(file = r"images\one.png")
oneimage = one.subsample(4,4)
one = Button(mainFrame, text="1", fg="black", image=oneimage,bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(1)).grid(row=3, column=0, padx=1, pady=1)

two = PhotoImage(file = r"images\two.png")
twoimage = two.subsample(4,4)
two = Button(mainFrame, text="2", fg="black",image=twoimage, bd=0, bg="black", cursor="hand2",
             command=lambda: clickButton(2)).grid(row=3, column=1, padx=1, pady=1)

three = PhotoImage(file = r"images\three.png")
threeimage = three.subsample(4,4)
three = Button(mainFrame, text="3", fg="black",image=threeimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(3)).grid(row=3, column=2, padx=1, pady=1)

plus = PhotoImage(file = r"images\plus.png")
plusimage = plus.subsample(4,4)
plus = Button(mainFrame, text="+", fg="white",image=plusimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton("+")).grid(row=2, column=3, padx=1, pady=1)


zero = PhotoImage(file = r"images\0.png")
zeroimage = zero.subsample(4,4)
zero = Button(mainFrame, text="0", fg="black",image=zeroimage, bd=0, bg="black", cursor="hand2",
              command=lambda: clickButton(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = PhotoImage(file = r"images\point.png")
pointimage = point.subsample(4,4)
point = Button(mainFrame, text=".", fg="black",image=pointimage, bd=0, bg="black", cursor="hand2",
               command=lambda: clickButton(".")).grid(row=4, column=3, padx=1, pady=1)


equal = PhotoImage(file = r"images\equal.png")
equalimage = equal.subsample(4,4)
equals = Button(mainFrame, text="=", image=equalimage, fg="white", bd=0, bg="black", cursor="hand2",
                command=lambda: equalButton()).grid(row=3, column=3, padx=1, pady=1)

window.iconbitmap("images\icon.ico")
window.config(bg="black",menu=menubar)
window.mainloop()