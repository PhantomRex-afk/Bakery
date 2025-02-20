from tkinter import *
from tkinter import messagebox
import random

P=Tk()
P.geometry("400x250")
P.title("Login and Registration")


a=Label(P,text='Username : ')
a.pack()
User=Entry(P)
User.pack()
b=Label(P,text='Password : ')
b.pack()
Pass=Entry(P,show=('*'))
Pass.pack()
account={}
# To enter username and password

def L():
    username=User.get()
    password=Pass.get()
    if username in account and account[username]==password:
        messagebox.showinfo('Login','Login was successful <3')
    elif username == "" or password == "":
        messagebox.showerror('Login','Please enter both username and password [:')
    else:
        messagebox.showerror('Login','Entered username or password was incorrect </3')
Log=Button(P,text="Login",command=L)
Log.pack()
# For logging in

s=IntVar()
def S():
    if  s.get() == 1:
        Pass.config(show="")
    else:
        Pass.config(show="*")
see=Checkbutton(P,text='Show',command=S,variable=s)
see.place(x=270,y=63)
# For letting the user see the password they enter

def R():
    P1=Toplevel()
    P1.geometry("400x250")
    P1.title('Registration')
    f=Label(P1,text='First Name :')
    f.pack()
    FName=Entry(P1)
    FName.pack()
    l=Label(P1,text='Last Name :')
    l.pack()
    LName=Entry(P1)
    LName.pack()
    u=Label(P1,text='Username :')
    u.pack()
    RUser=Entry(P1)
    RUser.pack()
    p=Label(P1,text='Password :')
    p.pack()
    RPass=Entry(P1)
    RPass.pack()
    cp=Label(P1,text='Confirm Password :')
    cp.pack()
    CPass=Entry(P1)
    CPass.pack()
    def r():
        if CPass.get() != RPass.get():
            messagebox.showerror('Register',"The two entered passwords must be same [:")
        elif FName.get()=="" or LName.get()=="" or RUser.get()=="" or RPass.get()=="" or CPass.get()=="":
            messagebox.showerror('Register','Please fill all the credentials [:')
        elif RUser.get() in account and account[RUser.get()]==RPass.get():
            messagebox.showerror('Register','Account already exists [:')
        else:
            account[RUser.get()]= RPass.get()
            P1.destroy()
        # For registration

            P2=Toplevel()
            P2.geometry("400x250")
            P2.title('Security Questions')
            Label(P2,text='Please answer the following security questions :').pack()
            Label(P2,text='1. What is your favorite food?').pack()
            global ff
            ff=Entry(P2)
            ff.pack()
            Label(P2,text='2. What is your favorite animal?').pack()
            global fa
            fa=Entry(P2)
            fa.pack()
            Label(P2,text='3. What is your favorite color?').pack()
            global fc
            fc=Entry(P2)
            fc.pack()
            Label(P2,text='Note : These security questions help us identify you incase you forget your password or decide to change it so please answer carefully <3').pack()
            def complete():
                if ff.get()=="" or fa.get()=="" or fc.get()=="":
                    messagebox.showerror('Please answer all the questions [:')
                else:
                    messagebox.showinfo('Register','Registration was successful <3')
                    P2.destroy()
            Done=Button(P2,text='Done',command=complete).pack()
            # For security questions

    Register=Button(P1,text='Register',command=r).pack()
c=Label(P,text="Don't have an account?")
c.pack()
Register=Button(P,text="Register Now!",command=R)
Register.place(x=263,y=103)
# Make a new account

def F():
    P3=Toplevel()
    P3.geometry("400x250")
    P3.title('Change Password')
    rand=random.randint(1,3)
    if rand == 1:
        Label(P3,text='-> What is your favorite food?').pack()
    elif rand == 2:
        Label(P3,text='-> What is your favorite animal?').pack()
    else:
        Label(P3,text='-> What is your favorite color?').pack()
    e=Entry(P3)
    e.pack()
    def Done():
        if e.get()==ff.get() or e.get()==fa.get() or e.get()==fc.get():
            P3.destroy()
            messagebox.showinfo('Verification Complete')
            P4=Toplevel()
            Label(P4,text='Reset Password').pack()
            Rp=Entry(P4)
            Rp.pack()
            Label(P4,text='Confirm Password').pack()
            Cp=Entry(P4)
            Cp.pack()
            def Done1():
                if Rp.get()==Cp.get():
                    messagebox.showinfo('Password changed successfully <3')
                    P4.destroy()
                else:
                    messagebox.showerror('Please enter the same password [:')
            Done1=Button(P4,text='Done',command=Done1).pack()
        else:
            messagebox.showerror('Incorrect answer. Try again </3')
    Done=Button(P3,text='Done',command=Done).pack()   
Forgot=Button(P,text="Forgot Password?",command=F)
Forgot.place(x=270,y=80)
mainloop()