from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Developer:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("")
        self.root.wm_iconbitmap("favicon.ico")

        title_lbl=Label(self.root,text="Developer ",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        img3=Image.open(r"college_images\dev.jpg")
        img3=img3.resize((1540,750),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1540,height=750)

        # Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=400)

        img_profile=Image.open(r"college_images\ProfileImage.png")
        img_profile=img_profile.resize((200,200),Image.ANTIALIAS)
        self.photoimg_profile=ImageTk.PhotoImage(img_profile)

        bg_img=Label(main_frame,image=self.photoimg_profile)
        bg_img.place(x=150,y=10,width=200,height=200)

        # devepoper
        dev_label=Label(main_frame,text="Hello Myself Shruti H Kapse",font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=90,y=230)

        dev_label=Label(main_frame,text="I am student of Cummins College of Engineering, Pune",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=0,y=260)

        dev_label=Label(main_frame,text="A passinate coder and love to develope new things",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=10,y=290)






        



if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()  