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
root = Tk()
root.geometry("1050x700")
root.title("ENCODE RLE")
global  message
global username
global password
username = StringVar()
password = StringVar()
message=StringVar()
#advantage menu list command
# choose encode algorithm
frame1 = Frame(root, highlightbackground="#7EC8E3", highlightthickness=3)
frame1.grid(row=4,column=1)

#frame 2
row2=10
col2=1
frame2 = Frame(root, highlightbackground="#5CD85A", highlightthickness=3)
frame2.grid(row=row2,column=col2,pady=20)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def showimage_en():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Lựa chọn ảnh cần mã hóa",
    filetypes = (
        ('img files', '*.png'),
        ('All files', '*.*')
    ))
    if fln!='':
        title1=Label(root,text="Ảnh Gốc", highlightbackground="#7EC8E3", highlightthickness=3,fg="red")
        title1.grid(row=1,column=5) 
        lbl=Label(root,highlightbackground="#7EC8E3", highlightthickness=3)
        lbl.grid(row=2,column=5) 
        print(fln)
        img=Image.open(fln)
        resize_image = img.resize((200, 200))
        img=ImageTk.PhotoImage(resize_image)
    
        lbl.config(image = img)
        lbl.image=img
        #dir_image.insert('fln')
        dir_image.insert('1.0',fln)
def showimage_de():
    
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Lựa chọn ảnh cần mã hóa",
    filetypes = (
        ('img files', '*.png'),
        ('All files', '*.*')
    ))
    if fln!='':
        title1=Label(root,text="Ảnh Đã Giấu Tin", highlightbackground="#7EC8E3", highlightthickness=3,fg="red")
        title1.grid(row=1,column=7,padx=20) 
        lbl=Label(root,highlightbackground="#7EC8E3", highlightthickness=3)
        lbl.grid(row=2,column=7,padx=20) 
        print(fln)
        img=Image.open(fln)
        resize_image = img.resize((200, 200))
        img=ImageTk.PhotoImage(resize_image)
    
        lbl.config(image = img)
        lbl.image=img
def open_text_file():
    """ # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = filedialog.askopenfile(initialdir=os.getcwd(),title="Lựa chọn tập tin thông điệp",filetypes=filetypes)
    # read the text file and show its content on the Text
    f=open(f,'r')
    data=f.read()

    signal.delete('1.0', END)
    signal.insert('1.0', data)

    dir_image_1.delete('1.0',END)
    dir_image_1.insert('1.0',f) """
    tf = filedialog.askopenfilename(
        initialdir=os.getcwd(),title="Lựa chọn tập tin thông điệp"
        , 
        filetypes=(("Text Files", "*.txt"),)
        )
    signal.delete('1.0', END)
    dir_image_1.delete('1.0',END)
    dir_image_1.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    signal.insert(END, data)
    tf.close()

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
def sel_hash():
   selection = "You selected the option " + str(var1.get())
   label1.config(text = selection)

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
btn_open = Button(root,width=10, text="...", fg="red",activebackground = "red",command=showimage_en)  
btn_open.grid(row=1,column=3)
#thong diep
l3 = Label(root, text="Thông Điệp ", bg="#f2f2f2",fg="black",font="(Arial)")
l3.grid(row=2,column=0,pady=50,padx=40)
signal=Text(root,width=30,height=5)
signal.grid(row=2,column=1)
#select file
l4 = Label(root, text="Chọn Tệp ", bg="#f2f2f2",fg="black",font="(Arial)")
l4.grid(row=3,column=0,pady=10)
dir_image_1=Text(root,width=30,height=1)
dir_image_1.grid(row=3,column=1)
btn_open = Button(root,width=10, text="...", fg="red",activebackground = "red",command=open_text_file)  
btn_open.grid(row=3,column=3)


#encryption Algorithms
l5 = Label(root, text="Encryption Algorithms", bg="#f2f2f2",fg="red",font="(Arial)",anchor="w",bd=1,relief="solid")
l5.grid(row=4,column=1)


var = IntVar()
R1 = Radiobutton(root, text="1.RC2", variable=var, value=1,
                  command=sel)
R1.grid(row=5,column=0)

R2 = Radiobutton(root, text="2.RC4", variable=var, value=2,
                  command=sel)
R2.grid(row=5,column=1)

R3 = Radiobutton(root, text="3.DES", variable=var, value=3,
                  command=sel)
R3.grid(row=5,column=2)
R4 = Radiobutton(root, text="4.Triple DES", variable=var, value=4,
                  command=sel)
R4.grid(row=5,column=3)

label = Label(root,bg="#f2f2f2",fg="red")
label.grid(row=6,column=1)
#hasing Algorithms
l6 = Label(root, text="Hashing Algorithms", bg="red",fg="white",font="(Arial)",bd=1,relief="solid")
l6.grid(row=row2,column=1)
var1 = IntVar()
R5 = Radiobutton(root, text="1.MD2", variable=var1, value=1,
                  command=sel_hash)
R5.grid(row=row2+1,column=0,padx=10)

R6 = Radiobutton(root, text="2.MD4", variable=var1, value=2,
                  command=sel_hash)
R6.grid(row=row2+1,column=1)

R7 = Radiobutton(root, text="3.MD5", variable=var1, value=3,
                  command=sel_hash)
R7.grid(row=row2+1,column=2)
R8 = Radiobutton(root, text="4.SHA", variable=var1, value=4,
                  command=sel_hash)
R8.grid(row=row2+1,column=3,padx=10)
label1 = Label(root,bg="#f2f2f2",fg="red")
label1.grid(row=row2+2,column=1) 

#password
l8 = Label(root, text="Mật Khẩu  ", bg="#f2f2f2",fg="black",font="(Arial)")
l8.grid(row=14,column=0,pady=10)
Entry(root, textvariable=password ,show="*",relief='flat',
                          highlightthickness=1, highlightbackground="black",bd=2,selectbackground="yellow",  
                          highlightcolor='#4584F1',width=30).grid(row=14,column=1)


""" dir_image=Text(root,width=30,height=1)
dir_image.grid(row=14,column=1) """
btn_open = Button(root,width=10, text="Finish", fg="red",activebackground = "red")  
btn_open.grid(row=14,column=3)

#save folders
l9 = Label(root, text="Tên Ảnh ", bg="#f2f2f2",fg="black",font="(Arial)")
l9.grid(row=16,column=0,pady=10)
dir_image_save=Text(root,width=30,height=1)
dir_image_save.grid(row=16,column=1)
btn_open_save_image = Button(root,width=10, text="Save", fg="red",activebackground = "red",command=showimage_de)  
btn_open_save_image.grid(row=16,column=3)

#footer
load= Image.open("footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10,y=600)

root.mainloop()