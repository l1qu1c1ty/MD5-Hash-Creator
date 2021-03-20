# Python Tkinter,Text to MD5 Converter GUI Tool
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
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
root.geometry("330x330")
root.configure(background='#314169')
root.title("MD5 Encryption")
root.resizable(width=False, height=False)

title_lbl2 = Label(root, text="Text:",fg="white",bg="#314169")
title_lbl2.pack()
        
entry = Entry(root)
entry.pack(ipadx=50)
        
space2 = Label(text="",bg="#314169")
space2.pack()

title_lbl3 = Label(root, text="MD5 Hash:",fg="white",bg="#314169")
title_lbl3.pack()

entry2 = Entry(root)
entry2.pack(ipadx=50)

space3 = Label(text="",bg="#314169")
space3.pack()
        
button1 = Button(root, text="Encrypt",fg="blue",command=convert).pack()
spc1 = Label(root,text="",bg="#314169").pack()
button2 = Button(root, text="Clear",fg="gray", command = clear).pack()
spc2 = Label(root,text="",bg="#314169").pack()
button3 = Button(root, text="Save",fg="green",command=save).pack()
spc3 = Label(root,text="",bg="#314169").pack()
button4 = Button(root, text="Quit",fg="red",command=root.destroy).pack()
spc4 = Label(root,text="",bg="#314169").pack()

mainloop()
