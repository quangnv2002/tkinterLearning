from tkinter import *
from PIL import ImageTk
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        frame_login = Frame(self.root,bg="white")
        frame_login.place(x=150,y=150,height=340,width=500)

        title = Label(frame_login,text="Login Here",font=("Impact",35,"bold")).place(x=90,y=30)
        desc = Label(frame_login,text="Account Employee Login Area",font=("Goudy old style",15,"bold")).place(x=90,y=100)

        label_user = Label(frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray").place(x=90,y=140)
        self.txt_user = Entry(frame_login,font=("times new roman",15),bg="light gray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        forget = Button(frame_login,text="forget password?",bg="white",bd=0,fg="#d77337",font=("times new roman",12)).place(x=90,y=280)

        login_btn = Button(self.root,text="Login",bg="#d77337",fg="white",font=("times new roman",15)).place(x=330,y=470)


root= Tk()
obj=login(root)
root.mainloop()