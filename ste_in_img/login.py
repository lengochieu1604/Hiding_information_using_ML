from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
from subprocess import  call

#defining login function
def login():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="steganography")
    mysqlcursor=mysqldb.cursor()
    #getting form data
    uname=username.get()
    pwd=password.get()
    sql='select *from user where username=%s and password=%s'
    #applying empty validation
    mysqlcursor.execute(sql,[uname,pwd])
    results=mysqlcursor.fetchall()

    if results:
        messagebox.showinfo("","login success")
        login_screen.destroy()
        call(["python","Menu_main.py"])
        return True
    else:
         messagebox.showinfo("","Incorrect username or password")
         return False
#defining loginf orm function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Giao Diện Đăng Nhập")
    #setting height and width of screen
    login_screen.geometry("800x500")
    #declaring variable
    global  message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
	#Creating layout of login form
    Label(login_screen,width="300", text="Học Viện Công Nghệ Bưu Chính Viễn Thông", bg="#f2f2f2",fg="red",font="(Arial)").pack()
    # Read the Image
    image = Image.open("logo.png")
 
# Resize the image using resize() method
    resize_image = image.resize((100, 100))
 
    img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.pack(pady=30)
    #Username Label
    Label(login_screen, text="Tên Đăng Nhập").place(x=250,y=200)
    #Username textbox
    Entry(login_screen, textvariable=username, bg="white", bd=2, relief='flat', 
                          highlightthickness=1, 
                          highlightbackground="black", 
                          selectbackground="yellow", 
                          highlightcolor='#4584F1').place(x=350,y=200)
    #Password Labe
    Label(login_screen, text="Mật Khẩu  ").place(x=250,y=250)
    #Password textbox0
    Entry(login_screen, textvariable=password ,show="*",relief='flat',
                          highlightthickness=1, highlightbackground="black",bd=2,selectbackground="yellow",  
                          highlightcolor='#4584F1').place(x=350,y=250)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=280)
    #Login button
    image = Image.open("login.png")
    
# Resize the image using resize() method
    resize_image = image.resize((100, 100))
   
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=350,y=300)
    Button(login_screen, text="Register",foreground ="red", width=10, height=1, bg="white",command=login).place(x=350,y=330)
    Label(login_screen, text="Forget Your Password ? Click Here",foreground="blue").place(x=300,y=360)

    load= Image.open("footer.png")
    render = ImageTk.PhotoImage(load)
    img = Label(login_screen, image=render)
    img.place(x=-10, y=400)

    login_screen.mainloop()
#calling function Loginform
Loginform()