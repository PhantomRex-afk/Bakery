from tkinter import *
from tkinter import messagebox
import random

P=Tk()
P.title("Bakery")
P.geometry("400x250")
P.resizable(False, False)
label = Label(P, text="This window cannot be resized!", font=("Arial", 14))
img=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\bakery.png")
P.iconphoto(False,img)
image=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\imagdh design.png")
my_label = Label(P, image=image)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


a=Label(P,text='Username : ',bg='#f5be0a', fg="#000000", font=("Arial", 10))
a.pack(pady=5)
User=Entry(P)
User.pack(pady=2)
b=Label(P,text='Password : ',bg='#f5be0a', fg="#000000", font=("Arial", 10))
b.pack(pady=5)
Pass=Entry(P,show=('*'))
Pass.pack(pady=2)
account={}
# To enter username and password

def L():
    username=User.get()
    password=Pass.get()
    if username in account and account[username]==password:
        P3=Toplevel()
        P3.geometry("400x250")
        P3.title('Verification')
        P3.resizable(False, False)
        img=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\bakery.png")
        P3.iconphoto(False,img)
        image=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\imagdh design.png")
        my_label = Label(P3, image=image)
        my_label.image = image
        my_label.place(x=0, y=0, relwidth=1, relheight=1)
        Label(P3,text="Who's logging in?",bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
        def V():
            messagebox.showinfo('Verification','Login was successful <3')
            P3.destroy()
            customer_page()

        def V1():
            P4=Toplevel()
            P4.geometry("400x250")
            P4.title('Verification')
            P4.resizable(False, False)
            img=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\bakery.png")
            P4.iconphoto(False,img)
            image=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\imagdh design.png")
            my_label = Label(P4, image=image)
            my_label.image = image
            my_label.place(x=0, y=0, relwidth=1, relheight=1)
            Label(P4,text="Enter PIN :",bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
            pin=Entry(P4)
            pin.pack(pady=4)
            P3.destroy()
            def Pin():
                if pin.get() == '12345':
                    messagebox.showinfo('Verification','Login was successful <3')
                    P.destroy()
                    P4.destroy()
                    employee_page()


                else:
                    messagebox.showerror('Verification','Invalid PIN </3')
            Enter=Button(P4,text='Enter',command=Pin,bg='#f5be0a', fg="#000000", font=("Arial", 10))
            Enter.pack(pady=4)
        Customer=Button(P3,text='Customer',command=V,bg='#f5be0a', fg="#000000", font=("Arial", 10))
        Customer.pack(pady=4)
        Employee=Button(P3,text='Employee',command=V1,bg='#f5be0a', fg="#000000", font=("Arial", 10))
        Employee.pack(pady=4)
        
    elif username == "" or password == "":
        messagebox.showerror('Login','Please enter both username and password [:')
    else:
        messagebox.showerror('Login','Entered username or password was incorrect')
Log=Button(P,text="Login",command=L, bg='#f5be0a', fg="#000000", font=("Arial", 10))
Log.pack(pady=6)
# For logging in

s=IntVar()
def S():
    if  s.get() == 1:
        Pass.config(show="")
    else:
        Pass.config(show="*")
see=Checkbutton(P,text='Show',command=S,variable=s, bg='#f5cb42', fg="#000000", font=("Arial", 10))
see.place(x=270,y=85)
# For letting the user see the password they enter

def R():
    P1=Toplevel()
    P1.geometry("500x300")
    P1.title('Registration')
    P1.resizable(False, False)
    img=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\bakery.png")
    P1.iconphoto(False,img)
    image=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\imagdh design.png")
    my_label = Label(P1, image=image)
    my_label.image = image
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    f=Label(P1,text='First Name :',bg='#f5be0a', fg="#000000", font=("Arial", 10))
    f.pack(pady=4)
    FName=Entry(P1)
    FName.pack(pady=1)
    l=Label(P1,text='Last Name :',bg='#f5be0a', fg="#000000", font=("Arial", 10))
    l.pack(pady=4)
    LName=Entry(P1)
    LName.pack(pady=1)
    u=Label(P1,text='Username :',bg='#f5be0a', fg="#000000", font=("Arial", 10))
    u.pack(pady=4)
    RUser=Entry(P1)
    RUser.pack(pady=1)
    p=Label(P1,text='Password :',bg='#f5be0a', fg="#000000", font=("Arial", 10))
    p.pack(pady=4)
    RPass=Entry(P1)
    RPass.pack(pady=1)
    cp=Label(P1,text='Confirm Password :',bg='#f5be0a', fg="#000000", font=("Arial", 10))
    cp.pack(pady=4)
    CPass=Entry(P1)
    CPass.pack(pady=1)
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
            P2.geometry("500x300")
            P2.title('Security Questions')
            P2.resizable(False, False)
            img=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\bakery.png")
            P2.iconphoto(False,img)
            image=PhotoImage(file="C:\\Users\\ASUS\\Downloads\\imagdh design.png")
            my_label = Label(P2, image=image)
            my_label.image = image
            my_label.place(x=0, y=0, relwidth=1, relheight=1)

            Label(P2,text='Please answer the following security questions :',bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack()
            Label(P2,text='1. What is your favorite food?',bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
            global ff
            ff=Entry(P2)
            ff.pack(pady=1)
            Label(P2,text='2. What is your favorite animal?',bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
            global fa
            fa=Entry(P2)
            fa.pack(pady=1)
            Label(P2,text='3. What is your favorite color?',bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
            global fc
            fc=Entry(P2)
            fc.pack(pady=1)
            Label(P2,text='Note : These questions help us identify you incase you forget your password.',bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
            def complete():
                if ff.get()=="" or fa.get()=="" or fc.get()=="":
                    messagebox.showerror('Please answer all the questions [:')
                else:
                    messagebox.showinfo('Register','Registration was successful <3')
                    P2.destroy()
            Done=Button(P2,text='Done',bg='#f5be0a', fg="#000000", font=("Arial", 10),command=complete).pack(pady=4)
            # For security questions

    Register=Button(P1,text='Register',command=r, bg='#f5be0a', fg="#000000", font=("Arial", 10)).pack(pady=4)
c=Label(P,text="Don't have an account?",bg='#f5cb42', fg="#000000", font=("Arial", 10))
c.pack(pady=5)
Register=Button(P,text="Register Now!",command=R, bg='#f5be0a', fg="#000000", font=("Arial", 10))
Register.place(x=280,y=150)
# Make a new account
# Create a Customer page
def customer_page():
    customer_win = Tk()
    customer_win.geometry("600x600")
    customer_win.title("Bakery products")
    products = [
        {'name': 'Pancake', 'price': 200},
        {'name': 'Strawberry Cake', 'price': 500},
        {'name': 'Chocolate Cake', 'price': 1000},
        {'name': 'Fruit cake', 'price': 200},
        {'name': 'Cupcake', 'price': 300},
    ]
    cart = []
    def add_to_cart(product):
        for item in cart:
            if item['name'] == product['name']:
                item['quantity'] += 1
                update_cart()
                return
        cart.append({'name': product['name'], 'price': product['price'], 'quantity': 1})
        update_cart()
    def update_cart():
        for widget in cart_list.winfo_children():
            widget.destroy()
            total=0
        for item in cart:
            item_label = Label(cart_list, text=f"{item['name']} - {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}")
            item_label.pack(side=BOTTOM)
            total += item['quantity'] * item['price']
        total_label.config(text=f"Total: ${total}")
    def buy():
        if cart:
            total = sum(item['price'] for item in cart)
            messagebox.showinfo("Buy", f"Total: ${total}")
            cart.clear()
            update_cart() 
        else:
            messagebox.showwarning("Empty Cart", "Please add items.")
    def clear_cart():
        cart.clear()
        update_cart()
    product_list_frame = Frame(customer_win)
    product_list_frame.pack()
    for i, product in enumerate(products):
        product_frame = Frame(product_list_frame)
        product_frame.grid(row=0, column=i, padx=10) 
        product_lbl = Label(product_frame, text=f"{product['name']} - ${product['price']}")
        product_lbl.pack(side=TOP)
        add_button = Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
        add_button.pack(side=BOTTOM)
    cart_frame = Frame(customer_win, bd=2, relief="solid", padx=10, pady=10)
    cart_frame.pack(pady=20, fill="both", expand=True)
    cart_label =Label(cart_frame, text="Your Cart", font=("Arial", 16, "bold"))
    cart_label.pack()
    cart_list =Frame(cart_frame)
    cart_list.pack(pady=10, fill="both", expand=True)
    clear_cart_button =Button(customer_win, text="Clear Cart", command=clear_cart)
    clear_cart_button.pack(side=BOTTOM, pady=10)
    buy_button = Button(customer_win, text="Buy", command=buy)
    buy_button.pack(side=BOTTOM, pady=10)
    total_label = Label(customer_win, text="Total: $0", font=("Arial", 14))
    total_label.pack(side=BOTTOM, pady=10)
    customer_win.mainloop()

    

# Create an Employee page
def employee_page():
    employee_win = Toplevel()
    employee_win.geometry("400x250")
    employee_win.title("Employee Page")
    Label(employee_win, text="Welcome to the Employee Page!", font=("Arial", 14)).pack(pady=30)
    Button(employee_win, text="Logout", command=employee_win.destroy).pack()

mainloop()