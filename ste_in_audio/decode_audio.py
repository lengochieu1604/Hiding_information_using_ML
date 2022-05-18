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
import os
from hiding_audio import decoded_hiding_audio
path = "C:/Users/Dell/Desktop/Hiding_information_using_ML/ste_in_img/"
root = Tk()
root.geometry("1050x700")
root.title("DECODE RLE")

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def select_audio():
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Lựa chọn audio",
    filetypes = (
        ('img files', '*.wav'),
        ('All files', '*.*')
    ))
    if fln!='':
        dir_audio.insert('1.0',fln)
        
def select_folder():
    fln=filedialog.askdirectory(title="Select Folders")
    if fln!='':
        fln = fln + '/'
        dir_folder.insert('1.0',fln)

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
def sel_hash():
   selection = "You selected the option " + str(var1.get())
   label1.config(text = selection)

def decoded_audio():
   # Check null
    if(dir_audio.get('1.0','end').rstrip('\n') == ''):
        messagebox.showerror("Errors!","Vui lòng chọn Audio cần giấu!")
    elif (password.get() == ''):
        messagebox.showerror("Errors!","Vui lòng nhập Password!")
    elif (dir_folder.get('1.0','end').rstrip('\n') == ''):
        messagebox.showerror("Errors!","Vui lòng chọn nơi lưu!")
    elif (name_messages_save.get('1.0','end').rstrip('\n') == ''):
        messagebox.showerror("Errors!","Vui nhập tên file!")
    else:
      check = decoded_hiding_audio(dir_audio.get('1.0','end').rstrip('\n'),dir_folder.get('1.0','end').rstrip('\n')+name_messages_save.get('1.0','end').rstrip('\n'))
      if (check == True):
            messagebox.showinfo("Succesfull!","Tách tin vào Audio thành công!")
      else:
            messagebox.showerror("Errors!","Tách tin vào Audio thất bại!")
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

l1 = Label(root, text="Tách Tin Trong File Audio RLE ", bg="#f2f2f2",fg="red",font="(Arial)")
l1.grid(row=0,column=1)
#frame 2
row2=10
col2=1
frame2 = Frame(root, highlightbackground="#5CD85A", highlightthickness=3)
frame2.grid(row=row2,column=col2,pady=20)

# Select audio
l2 = Label(root, text="Chọn Audio ", bg="#f2f2f2",fg="black",font="(Arial)")
l2.grid(row=1,column=0,pady=10)
dir_audio=Text(root,width=30,height=1)
dir_audio.grid(row=1,column=1)
btn_open = Button(root,width=10, text="Chọn file", fg="red",activebackground = "red",command=select_audio)  
btn_open.grid(row=1,column=3)

# Chooses Encryption Algorithms Messages
l5 = Label(root, text="Encryption Algorithms Messages", bg="#f2f2f2",fg="red",font="(Arial)",anchor="w",bd=1,relief="solid")
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

# Chooses Hasing Algorithms Password
l6 = Label(root, text="Hashing Algorithms Password", bg="red",fg="white",font="(Arial)",bd=1,relief="solid")
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

# Enter password
l8 = Label(root, text="Nhập Mật Khẩu  ", bg="#f2f2f2",fg="black",font="(Arial)")
l8.grid(row=14,column=0,pady=10)
password = Entry(root,show="*",relief='flat',
                          highlightthickness=1, highlightbackground="black",bd=2,selectbackground="yellow",  
                          highlightcolor='#4584F1',width=30)
password.grid(row=14,column=1)

# Select folder folders
l9 = Label(root, text="Chọn nơi lưu ", bg="#f2f2f2",fg="black",font="(Arial)")
l9.grid(row=16,column=0,pady=10)
dir_folder=Text(root,width=30,height=1)
dir_folder.grid(row=16,column=1)
btn_open_save_audio = Button(root,width=10, text="Chọn folder", fg="red",activebackground = "red",command=select_folder)  
btn_open_save_audio.grid(row=16,column=3)

# Enter name output file
l10 = Label(root, text="Nhập Tên Messages Files ", bg="#f2f2f2",fg="black",font="(Arial)")
l10.grid(row=18,column=0,pady=10)
name_messages_save=Text(root,width=30,height=1)
name_messages_save.grid(row=18,column=1)

#Encoded
btn_open = Button(root,width=10, text="Decoded", fg="red",activebackground = "red", command=decoded_audio)  
btn_open.grid(row=18,column=3)
#footer
load= Image.open(path + "footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10,y=600)

root.mainloop()