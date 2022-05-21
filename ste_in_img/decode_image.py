import string
from Crypto.Hash import *
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
import class1
from test3 import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os

path = "C:/Users/Dell/Desktop/Hiding_information_using_ML/ste_in_img/"
root = Tk()

import codecs
from des import DesKey
from Crypto.Cipher import DES
from Crypto.Cipher import AES
import base64
from tkinter.filedialog import asksaveasfile

def save():
    fln=filedialog.asksaveasfilename(initialdir="/",
                                                   title="lựa chọn file lưu txt",
                                                   filetypes=(("Text files", "*.txt*"),
    
                                                             ("all files", "*.*")))

    open(fln, "w").close()                                                          
    file = open(fln,'a+')
    file.write(signal_en.get() + '\n')
    file.close() 
    dir_image_1.insert('1.0',fln)
    messagebox.showinfo("","Xuất File text thành công")    








x="superhero"
root = ttk.Window(themename=x)

root.geometry("1050x700")

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
    try:
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Lựa chọn ảnh cần giải mã",
    filetypes = (
        ('img files', '*.png'),
        ('All files', '*.*')
    ))
   
        if fln!='':
            title1=Label(root,text="Ảnh Đã Bị Giấu Tin", highlightbackground="#7EC8E3", highlightthickness=3,fg="red")
        title1.grid(row=1,column=5) 
        lbl=Label(root,highlightbackground="#7EC8E3", highlightthickness=3)
        lbl.grid(row=2,column=5) 
        
        img=Image.open(fln)
        resize_image = img.resize((200, 200))
        img=ImageTk.PhotoImage(resize_image)
    
        lbl.config(image = img)
        lbl.image=img
        
       
        dir_image.insert('1.0',fln)
        rb = class1.RLEBitmap()
        rb.open_png(fln)
        fs =open('output\golfcourse.rle','w')
        rb.write_rle_tostream(fs)
    except:
       messagebox.showinfo("","Ảnh Không Hợp Lệ")    
       lbl.config(image = '')  
    text = password.get()
    signal1=signal_en.get()
    
   
    
    if (int(str(var.get()))==1):
            signal1=decode('encode_bg20.png','')
            decoded_signature = bytes.fromhex(signal1)
            des = DES.new(text.encode('utf8'), DES.MODE_ECB)
            
            cipher_text = base64.b32decode(decoded_signature)
            decrypted_string = des.decrypt(cipher_text)
            print("The decrypted string is : ",decrypted_string.decode())
            signal.insert(0,decrypted_string.decode())
            

def sel():
   if(int(str(var.get()))==1):
        selection = "Bạn đã chọn mã hóa DES"
   if(int(str(var.get()))==2):
        selection = "Bạn đã chọn mã hóa AES"
   label.config(text = selection)


    


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

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)
#finish encode
def print_selection():
    if (var1.get() == 1) :
       messagebox.showinfo("","Đã chọn mã hóa ảnh ")
       root.destroy()
       call(["python","encode_image.py"])
    

        
    #label_error.destroy()

l1 = Label(root, text="Tách Tin Trong File Ảnh RLE ", bg="#f2f2f2",fg="red",font="(Arial)")
l1.grid(row=0,column=1)
var1 = ttk.IntVar()
w= ttk.Checkbutton(root, bootstyle="danger-round-toggle",command=print_selection,onvalue=1, offvalue=0,variable=var1)
w.grid(row=0,column=3)
#select image
l2 = Label(root, text="Chọn Ảnh ", bg="#f2f2f2",fg="black",font="(Arial)")
l2.grid(row=1,column=0,pady=10)
def retrieve_input():
    dir_image_value=dir_image.get("1.0","end-1c")
    print(dir_image_value)
dir_image=Text(root,width=30,height=1)
dir_image.grid(row=1,column=1)
btn_open = ttk.Button(root,width=10, text="Finish",bootstyle=(SUCCESS, OUTLINE),command=showimage_en)  
btn_open.grid(row=1,column=3)
#thong diep
l3 = Label(root, text="Thông Điệp ", bg="#f2f2f2",fg="black",font="(Arial)")
l3.grid(row=2,column=0,pady=50,padx=40)
signal_en = StringVar()
signal=Entry(root,width=30,textvariable=signal_en)
signal.grid(row=2,column=1)
#select file
l4 = Label(root, text="Chọn Tệp ", bg="#f2f2f2",fg="black",font="(Arial)")
l4.grid(row=3,column=0,pady=10)
dir_image_1=Text(root,width=30,height=1)
dir_image_1.grid(row=3,column=1)
btn_open = ttk.Button(root,width=10, text="...", bootstyle=(DANGER, OUTLINE),command = lambda : save())  
btn_open.grid(row=3,column=3)


#encryption Algorithms
l5 = Label(root, text="Encryption Algorithms", bg="#f2f2f2",fg="red",font="(Arial)",anchor="w",bd=1,relief="solid")
l5.grid(row=4,column=1)


var = IntVar()


R3 = ttk.Radiobutton(root, text="1.DES", variable=var, value=1,bootstyle="danger",
                  command=sel)
R3.grid(row=5,column=0)

label = Label(root,bg="#f2f2f2",fg="red")
label.grid(row=6,column=1)


#password
l8 = Label(root, text="Mật Khẩu  ", bg="#f2f2f2",fg="black",font="(Arial)")
l8.grid(row=14,column=0,pady=10)
# Create widgets
password = StringVar()
password_en=Entry(root, textvariable=password ,show="*",relief='flat',
                          highlightthickness=1, highlightbackground="black",bd=2,selectbackground="yellow",  
                          highlightcolor='#4584F1',width=30).grid(row=14,column=1)















































#footer
load= Image.open(path + "footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10,y=600)

root.mainloop()