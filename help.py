from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Help:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("")
        self.root.wm_iconbitmap("favicon.ico")
    
        title_lbl=Label(self.root,text="Help Desk ",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        img3=Image.open(r"college_images\help.jpeg")
        img3=img3.resize((1540,750),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1540,height=750)
 
        dev_label=Label(bg_img,text="Email:shruti.h.kapse1@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=550,y=220)



if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()  