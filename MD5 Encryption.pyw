# Python Tkinter,Text to MD5 Converter GUI Tool
# Created by Melih Can 
from tkinter import *
from tkinter import messagebox
import hashlib

def convert():
        text = entry.get()
        text2 = entry2.get()
        if not (text2 == ""):
                entry2.delete(0,END)
        if text == "":
                messagebox.showinfo('Warning', 'Text section cannot be empty!')
        if text != "":
                hash5 = hashlib.md5((text).encode("utf-8")).hexdigest()
        if not (text == ""): 
                entry2.insert(0,hash5)

def clear():
        text = entry.get()
        text2 = entry2.get()
        if (text and text2) == "":
                messagebox.showinfo('Warning', 'Text and MD5 Hash section already empty!')
        entry.delete(0,END)
        entry2.delete(0, END)

def save():
        write = entry.get()
        write2 = entry2.get()
        if not (write == ""):
                f = open("hash.txt","a+")
                f.write(write)
                f.write(" : ")
                f.write(write2)
                f.write("\n")
                f.close()
                messagebox.showinfo('Successful!', 'Saved in hash.txt file.')
        else:
                messagebox.showinfo('Warning', 'MD5 Hash section cannot be empty!')
        

root = Tk()
root.geometry("350x150")
root.configure(background='orange')
root.title("MD5 Encryption")
root.resizable(width=False, height=False)

title_lbl2 = Label(root, text="Text:",fg="white",bg="orange").place(x=10,y=10)
        
entry = Entry(root,width=40)
entry.place(x=100,y=10)
        
title_lbl3 = Label(root, text="MD5 Hash:",fg="white",bg="orange")
title_lbl3.place(x=10,y=50)

entry2 = Entry(root,width=40)
entry2.place(x=100,y=50)

button1 = Button(root, text="Encrypt",fg="blue",command=convert).place(x=5,y=120)
button2 = Button(root, text="Clear",fg="orange", command = clear).place(x=65,y=120)
button3 = Button(root, text="Save",fg="green",command=save).place(x=110,y=120)
button4 = Button(root, text="Quit",fg="red",command=root.destroy).place(x=150,y=120)

mainloop()
