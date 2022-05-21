from tkinter import * 
from tkinter import filedialog as fd 
from tkinter import messagebox as ms 
from PIL import ImageTk, Image 

#  Build A Image Viewer Now
 
class Image_Viewer: 
    
    def __init__(self,master): 
        self.master = master 
        self.c_size = (700,500) 
        self.setup_gui(self.c_size) 
        self.img=None 
    
    def setup_gui(self,s): 
        Label(self.master,text='Image Viewer',pady=5,bg='white', font=('Arial',30)).pack() 
        self.canvas = Canvas(self.master,height=s[1],width=s[0], bg='Black',bd=10,relief='ridge')
        self.canvas.pack() 
        txt = '''
                                     By Shrimad Mishra 
                                          on behaf of 
                                              CodeSpeedy
                                ''' 
        self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt ,font=('',30),fill='white') 
        f=Frame(self.master,bg='white',padx=10,pady=10) 
        Button(f,text='Open Image',bd=2,fg='white',bg='black',font=('',15) ,command=self.make_image).pack(side=LEFT) 
        f.pack() 

    def make_image(self):   
        
        try: 
            File = fd.askopenfilename() 
            pilImage = Image.open(File) 
            re=self.pilImage.resize((700,500),Image.ANTIALIAS) 
            self.img = ImageTk.PhotoImage(re) 
            self.canvas.delete(ALL) 
            self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10, anchor=CENTER,image=self.img) 
            self.status['text']='Current Image:'+File 
        
        except: 
            ms.showerror('Error!','File type is unsupported.') 

root=Tk() 
root.configure(bg='white') 
root.title('Image Viewer') 
Image_Viewer(root) 
root.resizable(0,0) 
root.mainloop()