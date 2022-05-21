
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import mysql.connector
from subprocess import  call
import os

path=os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.geometry("600x600")
root.title("Giao Diện Menu Chính")

def image_en():
   messagebox.showinfo("","Đã chọn mã hóa với ảnh ")
   root.destroy()
   call(["python","encode_image.py"])

def audio_en():
   messagebox.showinfo("Thông báo","Đã chọn mã hóa với Audio ")
   root.destroy()
   call(["python","./ste_in_audio/encode_audio.py"])

 #display menu
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

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Home", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
 

l1 = Label(root,width="40", text="Chọn Chức Năng Thực Hiện Chương Trình ", bg="#f2f2f2",fg="red",font="(Arial)")
l1.grid(row = 0, column = 2,  pady = 0)



image=Image.open("decode.png")
resize_image = image.resize((200,200))

encode_iamge=ImageTk.PhotoImage(resize_image )
image=Image.open("encode.png")
resize_image = image.resize((200, 200))
decode_iamge=ImageTk.PhotoImage(resize_image )

# button widget
b1 = Button(root, text = "AUDIO",image=encode_iamge,height=200, width=200,bd=2, 
                          highlightcolor='#4584F1', command=audio_en)
b2 = Button(root, text = "IMAGE",image=decode_iamge,height=200, width=200,bd=2, relief='flat', 
                          highlightthickness=1, 
                          highlightbackground="black", 
                         
                          highlightcolor='#4584F1',command=image_en)



load= Image.open("footer.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=-10, y=500)
b1.grid(row = 1, column = 2,pady = 15,padx=200)
b2.grid(row = 5, column = 2,pady = 0,padx=200) 


root.mainloop()