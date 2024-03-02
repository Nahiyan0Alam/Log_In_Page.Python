from tkinter import *
from tkinter import messagebox
import sqlite3


accountsystem = Tk()
accountsystem.rowconfigure(0, weight=1)
accountsystem.columnconfigure(0, weight=1)
height = 650
width = 1240
x = (accountsystem.winfo_screenwidth()//2) -(width//2)
y = (accountsystem.winfo_screenheight()//4) -(height//4)
accountsystem.geometry('{}x{}+{}+{}'.format(width, height, x, y))


accountsystem.title('AccountSystem')

sign_in = Frame(accountsystem)
sign_up = Frame(accountsystem)

for frame in (sign_in, sign_up):
    frame.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()

show_frame(sign_up)



#############################sign up####################

# sign up text variable
FirstName = StringVar()
LastName = StringVar()
Email = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()

(sign_up.configure(bg="#525561"))


# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_image = Label(
    sign_up,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=120, y=28)

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="Your Application Name",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label2 = Label(
    bg_image,
    image=headerText_image_right,
    bg="#272A37"
)
headerText_image_label2.place(x=400, y=45)

headerText2 = Label(
    bg_image,
    anchor="nw",
    text="Your Title",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 20 * -1),
    bg="#272A37"
)
headerText2.place(x=450, y=45)

# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(
    bg_image,
    text="Create new account",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=121)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(
    bg_image,
    text="Already a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
text.place(x=75, y=187)

# ================ GO TO LOGIN ====================
switchLogin = Button(
    bg_image,
    text="LOGIN",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda : show_frame(sign_in)
)
switchLogin.place(x=230, y=185, width=50, height=35)

# ================ First Name Section ====================
firstName_image = PhotoImage(file="assets\\input_img.png")
firstName_image_Label = Label(
    bg_image,
    image=firstName_image,
    bg="#272A37"
)
firstName_image_Label.place(x=80, y=242)

firstName_text = Label(
    firstName_image_Label,
    text="First Name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(file="assets\\name_icon.png")
firstName_icon_Label = Label(
    firstName_image_Label,
    image=firstName_icon,
    bg="#3D404B"
)
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
    firstName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=FirstName

)
firstName_entry.place(x=8, y=17, width=140, height=27)


# ================ Last Name Section ====================
lastName_image = PhotoImage(file="assets\\input_img.png")
lastName_image_Label = Label(
    bg_image,
    image=lastName_image,
    bg="#272A37"
)
lastName_image_Label.place(x=293, y=242)

lastName_text = Label(
    lastName_image_Label,
    text="Last Name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
lastName_text.place(x=25, y=0)

lastName_icon = PhotoImage(file="assets\\name_icon.png")
lastName_icon_Label = Label(
    lastName_image_Label,
    image=lastName_icon,
    bg="#3D404B"
)
lastName_icon_Label.place(x=159, y=15)

lastName_entry = Entry(
    lastName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=LastName

)
lastName_entry.place(x=8, y=17, width=140, height=27)

# ================ Email Name Section ====================
emailName_image = PhotoImage(file="assets\\email.png")
emailName_image_Label = Label(
    bg_image,
    image=emailName_image,
    bg="#272A37"
)
emailName_image_Label.place(x=80, y=311)

emailName_text = Label(
    emailName_image_Label,
    text="Email Account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
emailName_text.place(x=25, y=0)

emailName_icon = PhotoImage(file="assets\\email-icon.png")
emailName_icon_Label = Label(
    emailName_image_Label,
    image=emailName_icon,
    bg="#3D404B"
)
emailName_icon_Label.place(x=370, y=15)

emailName_entry = Entry(
    emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=Email

)
emailName_entry.place(x=8, y=17, width=354, height=27)


# ================ Password Name Section ====================
passwordName_image = PhotoImage(file="assets\\input_img.png")
passwordName_image_Label = Label(
    bg_image,
    image=passwordName_image,
    bg="#272A37"
)
passwordName_image_Label.place(x=80, y=380)

passwordName_text = Label(
    passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
passwordName_icon_Label = Label(
    passwordName_image_Label,
    image=passwordName_icon,
    bg="#3D404B"
)
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
    passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=Password

)
passwordName_entry.place(x=8, y=17, width=140, height=27)


# ================ Confirm Password Name Section ====================
confirm_passwordName_image = PhotoImage(file="assets\\input_img.png")
confirm_passwordName_image_Label = Label(
    bg_image,
    image=confirm_passwordName_image,
    bg="#272A37"
)
confirm_passwordName_image_Label.place(x=293, y=380)

confirm_passwordName_text = Label(
    confirm_passwordName_image_Label,
    text="Confirm Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
confirm_passwordName_icon_Label = Label(
    confirm_passwordName_image_Label,
    image=confirm_passwordName_icon,
    bg="#3D404B"
)
confirm_passwordName_icon_Label.place(x=159, y=15)

confirm_passwordName_entry = Entry(
    confirm_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=ConfirmPassword

)
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

# =============== Submit Button ====================
submit_buttonImage = PhotoImage(
    file="assets\\button_1.png")
submit_button = Button(
    bg_image,
    image=submit_buttonImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
    command=lambda : signup()
)
submit_button .place(x=130, y=460, width=333, height=65)

# ================ Header Text Down ====================
headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label3 = Label(
    bg_image,
    image=headerText_image_down,
    bg="#272A37"
)
headerText_image_label3.place(x=650, y=530)

headerText3 = Label(
    bg_image,
    text="Made by Nahiyan Alam",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText3.place(x=700, y=530)

#clear sign up fields

def clear():
    LastName.set("")
    FirstName.set("")
    Password.set("")
    ConfirmPassword.set("")
    Email.set("")



#################Database Connection For Sign up###########



def signup():
    if FirstName.get() == "" or LastName.get() == "" or Password.get() == "" or Email.get() == "" or ConfirmPassword.get() == "":
        messagebox.showerror("Error", "All of Fields are required")

    elif Password.get() != ConfirmPassword.get():
        messagebox.showerror("Error", "Password and Confirm Password Doesn't Match")

    else:
        try:
            connection = sqlite3.connect("Database/Accountsystem.db")
            cur = connection.cursor()
            cur.execute("INSERT INTO AccountDB(FirstName, LastName, Email, Password) VALUES(?,?,?,?)",
                        (FirstName.get(), LastName.get(), Email.get(), Password.get()))
            connection.commit()
            connection.close()
            clear()
            messagebox.showinfo('Success', "New Account Created Successfully")

        except Exception as es:
            messagebox.showerror("Error", 'Something Going Wrong, Try Again')

##########################sign in######################


#Login text variables

email = StringVar()
password = StringVar()

sign_in.configure(bg="#525561")

# ================Background Image ====================
Login_backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_imageLogin = Label(
    sign_in,
    image=Login_backgroundImage,
    bg="#525561"
)
bg_imageLogin.place(x=120, y=28)

# ================ Header Text Left ====================
Login_headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
Login_headerText_image_label1 = Label(
    bg_imageLogin,
    image=Login_headerText_image_left,
    bg="#272A37"
)
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(
    bg_imageLogin,
    text="Your Application Name",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
Login_headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
Login_headerText_image_right = PhotoImage(file="assets\\headerText_image.png")
Login_headerText_image_label2 = Label(
    bg_imageLogin,
    image=Login_headerText_image_right,
    bg="#272A37"
)
Login_headerText_image_label2.place(x=400, y=45)

Login_headerText2 = Label(
    bg_imageLogin,
    anchor="nw",
    text="Your Title",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 20 * -1),
    bg="#272A37"
)
Login_headerText2.place(x=450, y=45)

# ================ LOGIN TO ACCOUNT HEADER ====================
loginAccount_header = Label(
    bg_imageLogin,
    text="Login for continue",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
loginAccount_header.place(x=75, y=121)

# ================ NOT A MEMBER TEXT ====================
loginText = Label(
    bg_imageLogin,
    text="Not a Member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
loginText.place(x=75, y=187)

# ================ GO TO SIGN UP ====================
switchSignup = Button(
    bg_imageLogin,
    text="Sign In",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda : show_frame(sign_up)
)
switchSignup.place(x=220, y=185, width=70, height=35)


# ================ Email Name Section ====================
Login_emailName_image = PhotoImage(file="assets\\email.png")
Login_emailName_image_Label = Label(
    bg_imageLogin,
    image=Login_emailName_image,
    bg="#272A37"
)
Login_emailName_image_Label.place(x=76, y=242)

Login_emailName_text = Label(
    Login_emailName_image_Label,
    text="Email Account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = PhotoImage(file="assets\\email-icon.png")
Login_emailName_icon_Label = Label(
    Login_emailName_image_Label,
    image=Login_emailName_icon,
    bg="#3D404B"
)
Login_emailName_icon_Label.place(x=370, y=15)

Login_emailName_entry = Entry(
    Login_emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=email

)
Login_emailName_entry.place(x=8, y=17, width=354, height=27)


# ================ Password Name Section ====================
Login_passwordName_image = PhotoImage(file="assets\\email.png")
Login_passwordName_image_Label = Label(
    bg_imageLogin,
    image=Login_passwordName_image,
    bg="#272A37"
)
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = Label(
    Login_passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
Login_passwordName_icon_Label = Label(
    Login_passwordName_image_Label,
    image=Login_passwordName_icon,
    bg="#3D404B"
)
Login_passwordName_icon_Label.place(x=370, y=15)

Login_passwordName_entry = Entry(
    Login_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=password

)
Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

# =============== Submit Button ====================
Login_button_image_1 = PhotoImage(
    file="assets\\button_1.png")
Login_button_1 = Button(
    bg_imageLogin,
    image=Login_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:login(),
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
)
Login_button_1.place(x=120, y=445, width=333, height=65)

# ================ Header Text Down ====================
Login_headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
Login_headerText_image_label3 = Label(
    bg_imageLogin,
    image=Login_headerText_image_down,
    bg="#272A37"
)
Login_headerText_image_label3.place(x=650, y=530)

Login_headerText3 = Label(
    bg_imageLogin,
    text="Made by Nahiyan Alam",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
Login_headerText3.place(x=700, y=530)

#Clear lofin fields

def clear_login():
    email.set()
    password.set()

#Database Connection

def login():
    conn = sqlite3.connect("./Database/Accountsystem.db")
    cursor = conn.cursor()
    find_user = 'SELECT * FROM AccountDB WHERE Email = ? and Password = ?'
    cursor.execute(find_user, [(Login_emailName_entry.get()), (Login_passwordName_entry.get())])

    result = cursor.fetchall()

    if result:
        messagebox.showinfo("Success", 'Log in Successfully')
    else:
        messagebox.showerror("Failed", "Sorry, Can't Login. Try again")

# ================ Forgot Password ====================
forgotPassword = Button(
    bg_imageLogin,
    text="Forget password",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    activebackground="#272A37",
    activeforeground="#ffffff",
    cursor="hand2",
    command=lambda: forgot_password(),
)
forgotPassword.place(x=210, y=400, width=150, height=35)


def forgot_password():

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    # win.iconbitmap('images\\aa.ico')
    win.configure(background='#272A37')
    win.resizable(False, False)

    # ====== Email ====================
    email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                         bd=0)
    email_entry3.place(x=40, y=80, width=256, height=50)
    email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 11, 'bold'))
    email_label3.place(x=40, y=50)

    # ====  New Password ==================
    new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                               bd=0)
    new_password_entry.place(x=40, y=180, width=256, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=150)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                         command=lambda: change_password())
    update_pass.place(x=40, y=260, width=256, height=45)

    def exit_window():
        win.destroy()

    #Database connection for forget password

    def change_password():
        if email_entry3.get() == "" or new_password_entry.get() == "":
            messagebox.showerror("Error", "Email or Password is vault" )

        else:
            db= sqlite3.connect("./Database/Accountsystem.db")
            cursor = db.cursor()
            query = 'select * from AccountDB where Email=?'
            cursor.execute(query, [(email_entry3.get())])
            row = cursor.fetchone()
            if row == None :
                messagebox.showerror("Error", "Email Doesn't exists")
                exit_window()

            else:
                query = '''update AccountDB set Password=? where Email=?'''
                cursor.execute(query, [new_password_entry.get(), email_entry3.get(),])
                db.commit()
                db.close()
                messagebox.showinfo('Congratulations', "Changed Password Successfully")
                exit_window()


accountsystem.resizable(False,False)
accountsystem.mainloop()