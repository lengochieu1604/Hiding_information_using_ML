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
from Crypto.Util.Padding import pad, unpad

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



from des import DesKey
from Crypto.Cipher import DES
from Crypto.Cipher import AES
import base64
import codecs
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from math import log10, sqrt
import cv2
import re
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import numpy as np









x="superhero"
root = ttk.Window(themename=x)

root.geometry("1070x700")

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
def print_selection():
    if (var1.get() == 1) :
       messagebox.showinfo("","Đã chọn giải mã ảnh ")
       root.destroy()
       call(["python","decode_image.py"])
def donothing1():
       messagebox.showinfo("Thông Báo","Đã Chọn Quay Về Home ")
       root.destroy()
       call(["python","Menu_main.py"])    
#frame 2
row2=10
col2=1
frame2 = Frame(root, highlightbackground="#5CD85A", highlightthickness=3)
frame2.grid(row=row2,column=col2,pady=20)
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def showimage_en():
    
    try:
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
    signal=signal_en.get()
    
    try: 
     
        if (int(str(var.get()))==1):
          
            des = DES.new(text.encode('utf8'), DES.MODE_ECB)
                        
            plain_text = pad1(signal)
            ciphertext = des.encrypt(plain_text.encode())
            encode_string= base64.b32encode(ciphertext)  
            print(encode_string)

            decrypted_string = des.decrypt(ciphertext)
            print("The decrypted string is : ",decrypted_string.decode())
            print(" is : ",encode_string.hex())
    except:
        messagebox.showinfo(""," Sai độ dài khóa des")   
    encode(fln,encode_string.hex(),'encode_bg20.png')    
    original = cv2.imread(fln)
    compressed = cv2.imread('encode_bg20.png', 1)
    value = PSNR(original, compressed)
    title2=Label(root,text="PNSR là"+str(value), highlightbackground="#7EC8E3", highlightthickness=3,fg="red")
    title2.grid(row=3,column=5) 
    title1=Label(root,text="Ảnh Đã Giấu Tin", highlightbackground="#7EC8E3", highlightthickness=3,fg="red")
    title1.grid(row=1,column=7,padx=20) 
    lbl=Label(root,highlightbackground="#7EC8E3", highlightthickness=3)
    lbl.grid(row=2,column=7,padx=20) 
    img=Image.open('encode_bg20.png')
    resize_image = img.resize((200, 200))
    img=ImageTk.PhotoImage(resize_image)
    
    lbl.config(image = img)
    lbl.image=img
    messagebox.showinfo("","Đã lưu vào ảnh mã hóa vào  :D:\python_hide_information\Hiding_information_using_ML\ste_in_img\encode_bg20.png") 
    
    #decode('encode_bg20.png','')
def showimage_de():
    
    fln=filedialog.askdirectory()
    
    if fln!='':
        title1=Label(root,text="Ảnh Đã Giấu Tin", highlightbackground="#7EC8E3", highlightthickness=3,fg="red")
        title1.grid(row=1,column=7,padx=20) 
        lbl=Label(root,highlightbackground="#7EC8E3", highlightthickness=3)
        lbl.grid(row=2,column=7,padx=20) 
        img=Image.open(fln+'\image1.png')
        resize_image = img.resize((200, 200))
        img=ImageTk.PhotoImage(resize_image)
    
        lbl.config(image = img)
        lbl.image=img
        rb =class1.RLEBitmap()
        fs = open('output\golfcourse.rle','r')
        rb.read_rle_fromstream(fs)
        fs.close()
        rb.write_memory_tofile(fln)
        dir_image_save.insert('1.0',fln)
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
    """ signal.delete('1.0', END)
    dir_image_1.delete('1.0',END) """
    dir_image_1.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    signal.insert(END, data)
    tf.close()
   #write rle to an existing file stream

def sel():
   if(int(str(var.get()))==1):
        selection = "Bạn đã chọn mã hóa DES"
   """ if(int(str(var.get()))==2):
        selection = "Bạn đã chọn mã hóa AES" """
   label.config(text = selection)

""" def sel_hash():
   if(int(str(var1.get()))==1):
        selection = "Bạn đã chọn SHA1"
   if(int(str(var1.get()))==2):
        selection = "Bạn đã chọn SHA256"
   if(int(str(var1.get()))==3):
        selection = "Bạn đã chọn MD5"
   if(int(str(var1.get()))==4):
        selection = "Bạn đã chọn SHA512"    
   label1.config(text = selection) """
    


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Home", command=donothing1)
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
def pad1(text):
    while(len(text) % 8 != 0):
        text += ' '
    return text

l1 = Label(root, text="Giấu Tin Trong File Ảnh RLE ", bg="#f2f2f2",fg="red",font="(Arial)")
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
btn_open = ttk.Button(root,width=10, text="finish",bootstyle=(SUCCESS, OUTLINE),command=showimage_en)  
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
btn_open = ttk.Button(root,width=10, text="...", bootstyle=(DANGER, OUTLINE),command=open_text_file)  
btn_open.grid(row=3,column=3)


#encryption Algorithms
l5 = Label(root, text="Encryption Algorithms", bg="#f2f2f2",fg="red",font="(Arial)",anchor="w",bd=1,relief="solid")
l5.grid(row=4,column=1)


var = IntVar()


R3 = ttk.Radiobutton(root, text="1.DES", variable=var, value=1,bootstyle="danger",
                  command=sel)
R3.grid(row=5,column=3)
""" R4 = ttk.Radiobutton(root, text="2.AES", variable=var, value=2,bootstyle="danger",
                  command=sel)
R4.grid(row=5,column=2) """

label = Label(root,bg="#f2f2f2",fg="red")
label.grid(row=6,column=1)
""" #hasing Algorithms
l6 = Label(root, text="Hashing Algorithms", bg="red",fg="white",font="(Arial)",bd=1,relief="solid")
l6.grid(row=row2,column=1)
var1 = IntVar()
R5 = ttk.Radiobutton(root, text="1.SHA1", variable=var1, value=1,bootstyle="warning",
                  command=sel_hash)
R5.grid(row=row2+1,column=0,padx=10)

R6 = ttk.Radiobutton(root, text="2.SHA256", variable=var1, value=2,bootstyle="warning",
                  command=sel_hash)
R6.grid(row=row2+1,column=1)

R7 = ttk.Radiobutton(root, text="3.MD5", variable=var1, value=3,bootstyle="warning",
                  command=sel_hash)
R7.grid(row=row2+1,column=2)
R8 = ttk.Radiobutton(root, text="4.SHA512", variable=var1, value=4,bootstyle="warning",
                  command=sel_hash)
R8.grid(row=row2+1,column=3,padx=10)
label1 = Label(root,bg="#f2f2f2",fg="red")
label1.grid(row=row2+2,column=1)  """

#password
l8 = Label(root, text="Mật Khẩu  ", bg="#f2f2f2",fg="black",font="(Arial)")
l8.grid(row=14,column=0,pady=10)
# Create widgets
password = StringVar()
password_en=Entry(root, textvariable=password ,show="*",relief='flat',
                          highlightthickness=1, highlightbackground="black",bd=2,selectbackground="yellow",  
                          highlightcolor='#4584F1',width=30).grid(row=14,column=1)







#footer
load= Image.open("footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10,y=620)

root.mainloop()