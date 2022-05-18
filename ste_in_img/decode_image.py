from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import ImageTk,Image
from matplotlib import image
from matplotlib.pyplot import title
import mysql.connector
from subprocess import  call
from PIL import ImageTk,Image
import easygui
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from pyparsing import col
from tkinter import  filedialog
from setuptools import Command
from function_main import *
import os
path = "C:/Users/Dell/Desktop/Hiding_information_using_ML/ste_in_img/"
root = Tk()
root.geometry("1050x700")
root.title("DECODE RLE")
global  message
global username
global password
username = StringVar()
password = StringVar()
message=StringVar()
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
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

editmenu.add_command(label="PSNR", command=donothing)
editmenu.add_command(label="Camera", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

l1 = Label(root, text="Tách Tin Trong File Ảnh RLE ", bg="#f2f2f2",fg="red",font="(Arial)")
l1.grid(row=0,column=4,padx=350)
#footer
load= Image.open(path + "footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10,y=600)

root.mainloop()