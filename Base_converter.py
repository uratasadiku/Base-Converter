from tkinter import *
from tkinter import messagebox # TODO: Remove this as it is imported
from converter_functions import *

root = Tk()

label_1 = Label(root, text="Enter value: ")
label_1.grid(row=0, sticky=W)

label_space = Label(root, text=" ")
label_space.grid(row=0, column=1)

entry = Entry(root, bd=3)
entry.grid(row=0, column=1, columnspan=2, ipadx=30, ipady=10)

def reset():
    entry.delete(0, END)
    entry.insert(0, "")

    label_space1 = Label(root, text="                   ")
    label_space1.grid(row=9, column=2)

    for i in range(4):
        var_a[i].set(0)
        var_b[i].set(0)


label_space.grid(row=0, column=3)

button_reset = Button(root, text="RESET", bd=5, relief="groove", bg="cyan",width=15, command=reset)
button_reset.grid(row=0, column=4)

label_space.grid(row=1)

label_2 = Label(root, text="Convert Base From:")
label_2.grid(row=2)

label_3 = Label(root, text="Convert Base To:")
label_3.grid(row=2, column=2)


# CONVERTING FUNCTIONS 

def convert():
    filename = "history.txt"
    label_space: Label = Label(root, text="                   ")
    if entry.get() == "":
        messagebox.showinfo("EMPTY", "Please enter value.")

    elif (var_a[0].get() == 1):
        if (var_b[0].get() == 1): # TODO: try nested conditions
            try:
                label_answer = Label(root, text=bin_to_bin(entry.get())[2:])
                label_space.grid(row=9, column=2)
                label_answer.grid(row=9, column=2)
                file = open(filename,"a")
                file.write("Binary To Binary: "+str(entry.get())+" => "+str(bin_to_bin(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")

        elif var_b[1].get() == 1:
            try:
                label_answer = Label(root, text=bin_to_dec(entry.get()))
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Binary To Decimal: " + str(entry.get()) + " => " + str(bin_to_dec(entry.get()))+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")

        elif var_b[2].get() == 1:
            try:
                label_answer = Label(root, text=bin_to_oct(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Binary To Octal: " + str(entry.get()) + " => " + str(bin_to_oct(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")
        elif var_b[3].get() == 1:
            try:
                label_answer = Label(root, text=bin_to_hex(entry.get()).upper()[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Binary To Hexa Decimal: " + str(entry.get()) + " => " + str(bin_to_hex(entry.get()).upper()[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")

    elif var_a[1].get() == 1: 
        if var_b[0].get() == 1:
            try:
                label_answer = Label(root, text=dec_to_bin(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Decimal To Binary: " + str(entry.get()) + " => " + str(dec_to_bin(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")

        elif var_b[1].get() == 1:
            try:
                label_answer = Label(root, text=dec_to_dec(entry.get()))
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Decimal To Decimal: " + str(entry.get()) + " => " + str(dec_to_dec(entry.get()))+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")

        elif var_b[2].get() == 1:
            try:
                label_answer = Label(root, text=dec_to_oct(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Decimal To Octal: " + str(entry.get()) + " => " + str(dec_to_oct(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted")

        elif var_b[3].get() == 1:
            try:
                label_answer = Label(root, text=dec_to_hex(entry.get()).upper()[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Decimal To Hexa Decimal: " + str(entry.get()) + " => " + str(dec_to_hex(entry.get()).upper()[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")

    elif var_a[2].get() == 1: 
        if var_b[0].get() == 1:
            try:
                label_answer = Label(root, text=oct_to_bin(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Octal To Binary: " + str(entry.get()) + " => " + str(oct_to_bin(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

        elif var_b[1].get() == 1:
            try:
                label_answer = Label(root, text=oct_to_dec(entry.get()))
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Octal To Decimal: " + str(entry.get()) + " => " + str(oct_to_dec(entry.get()))+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

        elif var_b[2].get() == 1:
            try:
                label_answer = Label(root, text=oct_to_oct(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Octal To Ocatl: " + str(entry.get()) + " => " + str(oct_to_oct(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

        elif var_b[3].get() == 1:
            try:
                label_answer = Label(root, text=oct_to_hex(entry.get()).upper()[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Octal To Hexa Decimal: " + str(entry.get()) + " => " + str(oct_to_hex(entry.get()).upper()[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")

    elif var_a[3].get() == 1: 
        if var_b[0].get() == 1:
            try:
                label_answer = Label(root, text=hex_to_bin(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Hexa Decimal To Binary: " + str(entry.get()) + " => " + str(hex_to_bin(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT",
                                    "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

        elif var_b[1].get() == 1:
            try:
                label_answer = Label(root, text=hex_to_dec(entry.get()))
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Hexa Decimal To Decimal: " + str(entry.get()) + " => " + str(hex_to_dec(entry.get()))+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT",
                                    "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

        elif var_b[2].get() == 1:
            try:
                label_answer = Label(root, text=hex_to_oct(entry.get())[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Hexa Decimal To Octal: " + str(entry.get()) + " => " + str(hex_to_oct(entry.get())[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT",
                                    "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

        elif var_b[3].get() == 1:
            try:
                label_answer = Label(root, text=hex_to_hex(entry.get()).upper()[2:])
                label_answer.grid(row=9, column=2)
                file = open(filename, "a")
                file.write("Hexa Decimal To Hexa Decimal: " + str(entry.get()) + " => " + str(hex_to_hex(entry.get()).upper()[2:])+"\n")
                file.close()
            except:
                messagebox.showinfo("ERROR INPUT","You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")

    else:
        messagebox.showinfo("REQUIREMENT", "Choose options on the both side")


now_a = None
buttons_a = None
var_a1 = IntVar()
var_a2 = IntVar()
var_a3 = IntVar()
var_a4 = IntVar()

var_a = [var_a1, var_a2, var_a3, var_a4]

def select_function():
    global now_a, buttons_a
    if None != now_a:
        buttons_a[now_a].deselect()
    vals_a = [var_a[i].get() for i in range(4)]
    try:
        now_a = vals_a.index(1)
    except ValueError:
        now_a = None


x_a = ["Binary", "Decimal", "Octal", "Hexa Decimal"]
y_a = 3
buttons_a = [Checkbutton(root, text=x_a[i], variable=var_a[i], command=select_function) for i in range(4)]
for b in buttons_a:
    b.grid(row=y_a, sticky=W)
    y_a = y_a + 1


now_b = None
buttons_b = None
var_a1 = IntVar()
var_a2 = IntVar()
var_a3 = IntVar()
var_a4 = IntVar()

var_b = [var_a1, var_a2, var_a3, var_a4]


def deselekt_function():
    global now_b, buttons_b
    if None != now_b:
        buttons_b[now_b].deselect()
    vals_b = [var_b[i].get() for i in range(4)]
    try:
        now_b = vals_b.index(1)
    except ValueError:
        now_b = None


x_b = ["Binary", "Decimal", "Octal", "Hexa Decimal"]
y_b = 3
buttons_b = [Checkbutton(root, text=x_b[i], variable=var_b[i], command=deselekt_function) for i in range(4)]
for b in buttons_b:
    b.grid(row=y_b, column=2, sticky=W)
    y_b = y_b + 1


button_convert = Button(root, text="CONVERT", bd=5, relief="groove", bg="#0BD72D", width=15,  command=convert)
button_convert.grid(row=7, columnspan=3)

def history():
    try:
        filename = "history.txt"
        file = open(filename, "r")
        data = file.readlines()
        m = ""
        for i in data:
            m = m + str(i) + "\n"
        messagebox.showinfo("HISTORY", str(m))
        file.close()
    except:
        messagebox.showinfo("EMPTY","There are no histoty recorded.")


btn_history = Button(root, text="HISTORY", bd=5, width=15, bg="grey", relief="groove", command=history)
btn_history.grid(row=1, column=4)

label_space.grid(row=8)

l_bin = Label(root, text="Answer: ")
l_bin.grid(row=9, sticky=W)
l_bin_ans = Label(root, text="                                  ", borderwidth=3, height=2, relief="groove")
l_bin_ans.grid(row=9, column=2)

root.title("Base Converter")

def exit():
    if messagebox.askyesno('Exit','Do you really want to Exit'):
        root.destroy()

btn_exit = Button(root, text="EXIT", bd=5, width=15,bg="red", relief="groove", command=exit)
btn_exit.grid(row=2, column=4)

root.mainloop()
