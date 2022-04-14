from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import ImageTk,Image
import mysql.connector
from subprocess import  call
from PIL import ImageTk,Image
import easygui
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from pyparsing import col

from setuptools import Command

root = Tk()
root.geometry("900x700")
root.title("ENCODE RLE")

#advantage menu list command
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing) 

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)



l1 = Label(root, text="Giấu Tin Trong File Ảnh RLE ", bg="#f2f2f2",fg="red",font="(Arial)")
l1.grid(row=0,column=1)
""" 
#image icon 
load= Image.open("icons8-image-64.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.pack(side=LEFT)  """
#select image
l2 = Label(root, text="Chọn Ảnh ", bg="#f2f2f2",fg="black",font="(Arial)")
l2.grid(row=1,column=0,pady=10)
dir_image=Text(root,width=30,height=1)
dir_image.grid(row=1,column=1)
btn_open = Button(root,width=10, text="...", fg="red",activebackground = "red",command=select_file)  
btn_open.grid(row=1,column=2)
#thong diep
l3 = Label(root, text="Thông Điệp ", bg="#f2f2f2",fg="black",font="(Arial)")
l3.grid(row=2,column=0,pady=50,padx=40)
signal=Text(root,width=30,height=5)
signal.grid(row=2,column=1)
#select file
l4 = Label(root, text="Chọn Tệp ", bg="#f2f2f2",fg="black",font="(Arial)")
l4.grid(row=3,column=0,pady=10)
dir_image=Text(root,width=30,height=1)
dir_image.grid(row=3,column=1)
btn_open = Button(root,width=10, text="...", fg="red",activebackground = "red",command=select_file)  
btn_open.grid(row=3,column=2)




#footer
load= Image.open("footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10,y=600)
root.mainloop()