from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import bgcolor
from PIL import Image,ImageTk
from help import Help
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System ")
        self.root.wm_iconbitmap("favicon.ico")

        # 1 
        img=Image.open(r"college_images\attendance.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # 2
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # 3
        img2=Image.open(r"college_images\images.jpg")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # Bg
        # 3
        img3=Image.open(r"college_images\bg1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Time
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="Blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # Student button
        img4=Image.open(r"college_images\studentimg.jpg")
        img4=img4.resize((220,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face
        img5=Image.open(r"college_images\face_detector.jpg")
        img5=img5.resize((220,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Attendace button
        img6=Image.open(r"college_images\attendance.jpg")
        img6=img6.resize((220,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attandance Details",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help button
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((220,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        # Train button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((220,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Image",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        # Photos face button
        img9=Image.open(r"college_images\photo.jpg")
        img9=img9.resize((220,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        # Developer button
        img10=Image.open(r"college_images\developer (2).jpg")
        img10=img10.resize((220,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_info)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_info,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

       # Exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Exit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit This Project",parent=self.root)
        if self.Exit >0:
            self.root.destroy()
        else:
            return 


    # ============Function Buttons================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
  
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
  
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
  




     
if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()  