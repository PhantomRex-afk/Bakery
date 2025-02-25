from tkinter import *
from tkinter import messagebox

P = Tk()
P.geometry("400x250")
P.title("Login and Registration")
a = Label(P, text='Username : ')
a.pack()
User = Entry(P)
User.pack()
b = Label(P, text='Password : ')
b.pack()
Pass = Entry(P, show=('*'))
Pass.pack()
account = {}
# To enter username and password
def L():
    username = User.get()
    password = Pass.get()
    if username in account and account[username] == password:
        # Create a new window (Toplevel) for login success
        P3 = Toplevel()
        P3.geometry("400x250")
        P3.title('Verification')
        Label(P3, text="Who's logging in?").pack()

        def V():
            messagebox.showinfo('Verification', 'Login was successful <3')
            P3.destroy()
            customer_page()  # Open customer page after successful login

        def V1():
            P4 = Toplevel()
            P4.geometry("400x250")
            P4.title('Verification')
            Label(P4, text="Enter PIN :").pack()
            pin = Entry(P4)
            pin.pack()

            def Pin():
                if pin.get() == '12345':
                    messagebox.showinfo('Verification', 'Login was successful <3')
                    P4.destroy()
                    employee_page()  # Open employee page after successful PIN entry
                else:
                    messagebox.showerror('Verification', 'Invalid PIN </3')

            Enter = Button(P4, text='Enter', command=Pin)
            Enter.pack()

        Customer = Button(P3, text='Customer', command=V)
        Customer.pack()
        Employee = Button(P3, text='Employee', command=V1)
        Employee.pack()

    elif username == "" or password == "":
        messagebox.showerror('Login', 'Please enter both username and password [:')
    else:
        messagebox.showerror('Login', 'Entered username or password was incorrect </3')

Log = Button(P, text="Login", command=L)
Log.pack()
# For logging in

s = IntVar()
def S():
    if s.get() == 1:
        Pass.config(show="")
    else:
        Pass.config(show="*")
see = Checkbutton(P, text='Show', command=S, variable=s)
see.place(x=270, y=63)
# For letting the user see the password they enter

def R():
    P1 = Toplevel()
    P1.geometry("400x250")
    P1.title('Registration')
    f = Label(P1, text='First Name :')
    f.pack()
    FName = Entry(P1)
    FName.pack()
    l = Label(P1, text='Last Name :')
    l.pack()
    LName = Entry(P1)
    LName.pack()
    u = Label(P1, text='Username :')
    u.pack()
    RUser = Entry(P1)
    RUser.pack()
    p = Label(P1, text='Password :')
    p.pack()
    RPass = Entry(P1)
    RPass.pack()
    cp = Label(P1, text='Confirm Password :')
    cp.pack()
    CPass = Entry(P1)
    CPass.pack()

    def r():
        if CPass.get() != RPass.get():
            messagebox.showerror('Register', "The two entered passwords must be same [:")
        elif FName.get() == "" or LName.get() == "" or RUser.get() == "" or RPass.get() == "" or CPass.get() == "":
            messagebox.showerror('Register', 'Please fill all the credentials [:')
        elif RUser.get() in account and account[RUser.get()] == RPass.get():
            messagebox.showerror('Register', 'Account already exists [:')
        else:
            account[RUser.get()] = RPass.get()
            P1.destroy()

            # Security Questions page
            P2 = Toplevel()
            P2.geometry("400x250")
            P2.title('Security Questions')
            Label(P2, text='Please answer the following security questions :').pack()
            Label(P2, text='1. What is your favorite food?').pack()
            global ff
            ff = Entry(P2)
            ff.pack()
            Label(P2, text='2. What is your favorite animal?').pack()
            global fa
            fa = Entry(P2)
            fa.pack()
            Label(P2, text='3. What is your favorite color?').pack()
            global fc
            fc = Entry(P2)
            fc.pack()
            Label(P2, text='Note: These security questions help us identify you incase you forget your password or decide to change it so please answer carefully <3').pack()

            def complete():
                if ff.get() == "" or fa.get() == "" or fc.get() == "":
                    messagebox.showerror('Please answer all the questions [:')
                else:
                    messagebox.showinfo('Register', 'Registration was successful <3')
                    P2.destroy()

            Done = Button(P2, text='Done', command=complete).pack()
            # For security questions

    Register = Button(P1, text='Register', command=r).pack()

c = Label(P, text="Don't have an account?")
c.pack()
Register = Button(P, text="Register Now!", command=R)
Register.place(x=263, y=103)
# Make a new account


# Create a Customer page
cart=[]
def customer_page():
    customer_win = Tk()
    customer_win.geometry("600x600")
    customer_win.title("Bakery products")
    global cart
    products = [
        {'name': 'Pancake', 'price': 200, 'quantity': 1},
        {'name': 'Strawberry Cake', 'price': 500, 'quantity': 1},
        {'name': 'Chocolate Cake', 'price': 1000, 'quantity': 1},
        {'name': 'Fruit cake', 'price': 200, 'quantity': 1}  
    ]   
    def add_to_cart(product):
        global cart
        for item in cart:
            if item['name'] == product['name']:
                item['quantity'] += product['quantity']
                update_cart()
                return
        cart.append({'name': product['name'], 'price': product['price'], 'quantity': product['quantity']})
        update_cart()
    def update_cart():
        for widget in cart_list.winfo_children():
            widget.destroy()
        total = 0
        for item in cart:
            item_label = Label(cart_list, text=f"{item['name']} - {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}")
            item_label.pack(side=BOTTOM)
            total += item['quantity'] * item['price']
        total_label.config(text=f"Total: ${total}")
    def change_quantity(product, delta):
        if product['quantity'] + delta >= 0:
            product['quantity'] += delta
            update_product_list()
    def update_product_list():
        for i, product in enumerate(products):
            product_lbl = product_labels[i]
            product_lbl.config(text=f"{product['name']} - ${product['price']} | Quantity: {product['quantity']}")
    def buy():
        global cart
        if cart:
            total = sum(item['price'] * item['quantity'] for item in cart)
            messagebox.showinfo("Buy", f"Total: ${total}")
            cart.clear()
            update_cart()
        else:
            messagebox.showwarning("Empty Cart", "Please add items.")
    def clear_cart():
        global cart
        cart.clear()
        update_cart()
    product_list_frame = Frame(customer_win)
    product_list_frame.pack()
    product_labels = []
    for i, product in enumerate(products):
        product_frame = Frame(product_list_frame)
        product_frame.grid(row=0, column=i, padx=10)
        product_lbl = Label(product_frame, text=f"{product['name']} - ${product['price']} | Quantity:{product['quantity']}")
        product_lbl.pack(side=TOP)
        increase_button = Button(product_frame, text="+", command=lambda p=product: change_quantity(p, 1), bg="#f5be0a")
        increase_button.pack(side=LEFT, padx=5)
        decrease_button = Button(product_frame, text="-", command=lambda p=product: change_quantity(p, -1), bg="#f5be0a")
        decrease_button.pack(side=LEFT, padx=5)
        add_button = Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p), bg="#f5be0a")
        add_button.pack(side=LEFT, padx=5)
        product_labels.append(product_lbl)
    cart_frame = Frame(customer_win, bd=2, relief="solid", padx=10, pady=10)
    cart_frame.pack(pady=20, fill="both", expand=True)
    cart_label = Label(cart_frame, text="Your Cart", font=("Arial", 16, "bold"))
    cart_label.pack()
    cart_list = Frame(cart_frame)
    cart_list.pack(pady=10, fill="both", expand=True)
    clear_cart_button = Button(customer_win, text="Clear Cart", command=clear_cart)
    clear_cart_button.pack(side=BOTTOM, pady=10)
    buy_button = Button(customer_win, text="Buy", command=buy)
    buy_button.pack(side=BOTTOM, pady=10)
    total_label = Label(customer_win, text="Total: $0", font=("Arial", 14))
    total_label.pack(side=BOTTOM, pady=10)

    

# Create an Employee page
def employee_page():
    employee_win = Toplevel()
    employee_win.geometry("400x250")
    employee_win.title("Employee Page")
    Label(employee_win, text="Customer's Purchase Details", font=("Arial", 16, "bold")).pack(pady=10)
    if cart:
        total_cost = 0
        for item in cart:
            item_label = Label(employee_win, text=f"{item['name']} - {item['quantity']} x ${item['price']} = ${item['quantity'] * item['price']}")
            item_label.pack(pady=5)
            total_cost += item['quantity'] * item['price']
        total_label = Label(employee_win, text=f"Total: ${total_cost}", font=("Arial", 14, "bold"))
        total_label.pack(pady=10)
    else:
        Label(employee_win, text="No items purchased yet.", font=("Arial", 12)).pack(pady=10)
    
    Button(employee_win, text="Logout", command=employee_win.destroy).pack()

mainloop()
