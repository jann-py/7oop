from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

tk = Tk()
tk.title("Login Screen")
tk.geometry("800x600") # W x H
canvas = Canvas(tk, width=800, height=600)
canvas.pack()

tk2 = Toplevel()
tk2.title("Another Screen")
tk2.geometry("800x600")
tk2.withdraw() # hide by default
canvas2 = Canvas(tk2, width=800, height=600)
canvas2.pack()

def c_Arrow():
    tk.config(cursor="arrow")
    tk2.config(cursor="arrow")

def c_Hand2():
    tk.config(cursor="hand2")
    tk2.config(cursor="hand2")

conn = sqlite3.connect('System_Files.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE User_Credentials (
                  username text,
                  password text
                  )""")
except:
    print("A table already exists.")

conn.commit()
conn.close()

#Login Icon Widget
iconImg = Image.open("tkinter GUI images/1-LoginIcon.png")
iconImgResize = iconImg.resize((200, 200))
iconImage = ImageTk.PhotoImage(iconImgResize)
canvas.create_image(290, 30, anchor="nw", image=iconImage)

#Username Entry Widget
userImg = Image.open("tkinter GUI images/1-Username.png")
userImgResize = userImg.resize((374, 50))
userImage = ImageTk.PhotoImage(userImgResize)
canvas.create_image(200, 250, anchor="nw", image=userImage, tags="hintLogin")

userEmptyImg = Image.open("tkinter GUI images/3-EmptyLogin.png")
userEmptyImgResize = userEmptyImg.resize((374, 50))
userEmptyImage = ImageTk.PhotoImage(userEmptyImgResize)
canvas.create_image(200, 250, anchor="nw", image=userEmptyImage, tags="emptyLogin")
canvas.itemconfig("emptyLogin", state='hidden')

userInput = Entry(tk, width=27, bd=0, bg=tk["bg"], highlightthickness=0, font=("Roboto Slab", 15))
canvas.create_window(370, 275, window=userInput, tags="userEntry")
canvas.itemconfig("userEntry", state='hidden')

def flipUser(e):
    canvas.itemconfig("hintLogin", state='hidden')
    canvas.itemconfig("emptyLogin", state='normal')
    canvas.itemconfig("userEntry", state='normal')

def flipUserBack(e):
    if tk.focus_get() == userInput or userInput.get() != '':
        return
    else:
        canvas.itemconfig("hintLogin", state='normal')
        canvas.itemconfig("emptyLogin", state='hidden')
        canvas.itemconfig("userEntry", state='hidden')

canvas.tag_bind("hintLogin", "<Enter>", flipUser)
canvas.tag_bind("emptyLogin", "<Leave>", flipUserBack)

#Error Text Username
canvas.create_text(230, 306, text="Input can only contain letters, underscores, and numbers.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="notAllowed")
canvas.itemconfig("notAllowed", state='hidden')
canvas.create_text(230, 306, text="* This is a required field and cannot be left empty.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="noEmpty")
canvas.itemconfig("noEmpty", state='hidden')
canvas.create_text(230, 374, text="* This is a required field and cannot be left empty.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="noEmptyPass")
canvas.itemconfig("noEmptyPass", state='hidden')

def errTextUser():
    notAllowed = [' ', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '\\', '|', ';', ':', '\'', '"', ',', '.', '>', '<', '/', '?']
    n = len(notAllowed)

    input = userInput.get()
    inputP = passInput.get()
    passValue = 0

    if '' == input:
        canvas.itemconfig("noEmpty", state='normal')
        canvas.itemconfig("notAllowed", state='hidden')
        if '' == inputP:
            canvas.itemconfig("noEmptyPass", state='normal')
        return 2

    for i in range(n):
        if notAllowed[i] in input:
            canvas.itemconfig("notAllowed", state='normal')
            canvas.itemconfig("noEmpty", state='hidden')
            return 1

    if passValue != 1:
        print(passValue)
        canvas.itemconfig("notAllowed", state='hidden')
        canvas.itemconfig("noEmpty", state='hidden')
        return 0

#Password Entry Widget
passImg = Image.open("tkinter GUI images/2-Password.png")
passImgResize = passImg.resize((374, 50))
passImage = ImageTk.PhotoImage(passImgResize)
canvas.create_image(200, 318, anchor="nw", image=passImage, tags="hintPass")

passEmptyImg = Image.open("tkinter GUI images/3-EmptyPassword.png")
passEmptyImgResize = passEmptyImg.resize((374, 50))
passEmptyImage = ImageTk.PhotoImage(passEmptyImgResize)
canvas.create_image(200, 318, anchor="nw", image=passEmptyImage, tags="emptyPass")
canvas.itemconfig("emptyPass", state='hidden')

passInput = Entry(tk, width=27, bd=0, bg=tk["bg"], highlightthickness=0, font=("Roboto Slab", 15), show="•")
canvas.create_window(370, 343, window=passInput, tags="passEntry")
canvas.itemconfig("passEntry", state='hidden')

def flipPass(e):
    canvas.itemconfig("hintPass", state='hidden')
    canvas.itemconfig("emptyPass", state='normal')
    canvas.itemconfig("passEntry", state='normal')

def flipPassBack(e):
    if tk.focus_get() == passInput or passInput.get() != '':
        return
    else:
        canvas.itemconfig("hintPass", state='normal')
        canvas.itemconfig("emptyPass", state='hidden')
        canvas.itemconfig("passEntry", state='hidden')

canvas.tag_bind("hintPass", "<Enter>", flipPass)
canvas.tag_bind("emptyPass", "<Leave>", flipPassBack)

#Error Text Password
canvas.create_text(230, 374, text="A password must have at least 8 characters.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="errSignPass")
canvas.itemconfig("errSignPass", state='hidden')

canvas.create_text(230, 374, text="Username or password input is incorrect.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="errInputPass")
canvas.itemconfig("errInputPass", state='hidden')

#Remember Me Button and Forgot Password
style = ttk.Style()
style.configure('RM.TCheckbutton', font=("Roboto Slab", 9))
rememberMe = ttk.Checkbutton(tk, text="Remember Me", takefocus=0, cursor="hand2", style='RM.TCheckbutton')
canvas.create_window(282, 395, window=rememberMe, tags="remCButton")

canvas.create_text(542, 395, text="Forgot password?", font=("Roboto Slab", 9), justify="right", anchor="e", tags="forgotPass")

#Forgot Password Key Entry Widget
forgotPassImg = Image.open("tkinter GUI images/6-ForgotPassKey.png")
forgotPassImgResize = forgotPassImg.resize((374, 50))
forgotPassImage = ImageTk.PhotoImage(forgotPassImgResize)
canvas.create_image(200, 386, anchor="nw", image=forgotPassImage, tags="hintForgotPass")
canvas.itemconfig("hintForgotPass", state='hidden')

forgotPassEmptyImg = Image.open("tkinter GUI images/6-ForgotPassKeyEmpty.png")
forgotPassEmptyImgResize = forgotPassEmptyImg.resize((374, 50))
forgotPassEmptyImage = ImageTk.PhotoImage(forgotPassEmptyImgResize)
canvas.create_image(200, 386, anchor="nw", image=forgotPassEmptyImage, tags="emptyForgotPass")
canvas.itemconfig("emptyForgotPass", state='hidden')

forgotPassInput = Entry(tk, width=27, bd=0, bg=tk["bg"], highlightthickness=0, font=("Roboto Slab", 15), show="•")
canvas.create_window(370, 411, window=forgotPassInput, tags="forgotPassEntry")
canvas.itemconfig("forgotPassEntry", state='hidden')

def flipForgotPass(e):
    canvas.itemconfig("hintForgotPass", state='hidden')
    canvas.itemconfig("emptyForgotPass", state='normal')
    canvas.itemconfig("forgotPassEntry", state='normal')

def flipForgotPassBack(e):
    if tk.focus_get() == forgotPassInput or forgotPassInput.get() != '':
        return
    else:
        canvas.itemconfig("hintForgotPass", state='normal')
        canvas.itemconfig("emptyForgotPass", state='hidden')
        canvas.itemconfig("forgotPassEntry", state='hidden')

canvas.tag_bind("hintForgotPass", "<Enter>", flipForgotPass)
canvas.tag_bind("emptyForgotPass", "<Leave>", flipForgotPassBack)

#Sign up Button
signUpImg = Image.open("tkinter GUI images/5-Signup.png")
signUpImgResize = signUpImg.resize((374, 50))
signUpImage = ImageTk.PhotoImage(signUpImgResize)
canvas.create_image(200, 450, anchor="nw", image=signUpImage, tags="signUp")
canvas.itemconfig("signUp", state='hidden')

signUpHoverImg = Image.open("tkinter GUI images/5-SignupHover.png")
signUpHoverImgResize = signUpHoverImg.resize((374, 50))
signUpHoverImage = ImageTk.PhotoImage(signUpHoverImgResize)
canvas.create_image(200, 450, anchor="nw", image=signUpHoverImage, tags="signUpHover")
canvas.itemconfig("signUpHover", state='hidden')

def flipSButton(e):
    c_Hand2()
    canvas.itemconfig("signUp", state='hidden')
    canvas.itemconfig("signUpHover", state='normal')

def flipSButtonBack(e):
    c_Arrow()
    canvas.itemconfig("signUp", state='normal')
    canvas.itemconfig("signUpHover", state='hidden')

#Log in Button
loginImg = Image.open("tkinter GUI images/4-Login.png")
loginImgResize = loginImg.resize((374, 50))
loginImage = ImageTk.PhotoImage(loginImgResize)
canvas.create_image(200, 450, anchor="nw", image=loginImage, tags="login")

loginHoverImg = Image.open("tkinter GUI images/4-LoginHover.png")
loginHoverImgResize = loginHoverImg.resize((374, 50))
loginHoverImage = ImageTk.PhotoImage(loginHoverImgResize)
canvas.create_image(200, 450, anchor="nw", image=loginHoverImage, tags="loginHover")
canvas.itemconfig("loginHover", state='hidden')

def flipLButton(e):
    c_Hand2()
    canvas.itemconfig("login", state='hidden')
    canvas.itemconfig("loginHover", state='normal')

def flipLButtonBack(e):
    c_Arrow()
    canvas.itemconfig("login", state='normal')
    canvas.itemconfig("loginHover", state='hidden')

#Database Functions
def signUp(e):
    c_Hand2()
    conn = sqlite3.connect('System_Files.db')
    c = conn.cursor()

    if errTextUser() == 0:
        c.execute("INSERT INTO User_Credentials VALUES (:userInput, :passInput)",
                {
                    'userInput': userInput.get(),
                    'passInput': passInput.get()
                })

        c.execute("SELECT *, oid FROM User_Credentials")
        records = c.fetchall()
        print(records)

        printRecords = ''
        for record in records[0]:
            printRecords += str(record) + "\n"

        conn.commit()
        conn.close()

        userInput.delete(0, END)
        passInput.delete(0, END)

        canvas.itemconfig("signUp", state='hidden')
        canvas.itemconfig("goLogIn", state='hidden')
        canvas.itemconfig("hintForgotPass", state='hidden')
        canvas.itemconfig("login", state='normal')
        canvas.itemconfig("goSignUp", state='normal')
        canvas.itemconfig("remCButton", state='normal')
        canvas.itemconfig("forgotPass", state='normal')
        tk.title("Login Screen")

canvas.tag_bind("signUp", "<Enter>", flipSButton)
canvas.tag_bind("signUpHover", "<Leave>", flipSButtonBack)
canvas.tag_bind("signUpHover", "<Button-1>", signUp)

def secondScreen():
    tk.withdraw()
    tk2.deiconify()

def returnScreen():
    tk.deiconify()
    tk2.withdraw()

def checkIfExists():
    conn = sqlite3.connect('System_Files.db')
    c = conn.cursor()

    c.execute("SELECT username FROM User_Credentials WHERE username = ? AND password = ?", (userInput.get(), passInput.get()))
    exists = c.fetchone()

    conn.commit()
    conn.close()

    if exists:
        print("It exists")
        canvas.itemconfig("errP", state='hidden')
        return 1
    else:
        print("Does not exist")
        canvas.itemconfig("errP", state='normal')
        return 0

def login(e):
    c_Hand2()
    
    if checkIfExists() == 0:
        input = userInput.get()
        inputP = passInput.get()

        if '' == input or '' == inputP:
            canvas.itemconfig("notAllowed", state='hidden')
            if '' == input:
                canvas.itemconfig("noEmpty", state='normal')
            else:
                canvas.itemconfig("noEmpty", state='hidden')
            if '' == inputP:
                canvas.itemconfig("noEmptyPass", state='normal')
            else:
                canvas.itemconfig("noEmptyPass", state='hidden')
        else:
            canvas.itemconfig("errInputPass", state='normal')
            canvas.itemconfig("noEmpty", state='hidden')
            canvas.itemconfig("noEmptyPass", state='hidden')
    else:
        canvas.itemconfig("errInputPass", state='hidden')
        secondScreen()
        Button(tk2, text="Exit", command=returnScreen).pack()    

canvas.tag_bind("login", "<Enter>", flipLButton)
canvas.tag_bind("loginHover", "<Leave>", flipLButtonBack)
canvas.tag_bind("loginHover", "<Button-1>", login)

#Login Text
canvas.create_text(230, 510, text="Already have an account? Log in", font=("Roboto Slab", 9), justify="left", anchor="w", tags="goLogIn")
canvas.itemconfig("goLogIn", state='hidden')
def loginScreen(e):
    canvas.itemconfig("signUp", state='hidden')
    canvas.itemconfig("goLogIn", state='hidden')
    canvas.itemconfig("hintForgotPass", state='hidden')
    canvas.itemconfig("login", state='normal')
    canvas.itemconfig("goSignUp", state='normal')
    canvas.itemconfig("remCButton", state='normal')
    canvas.itemconfig("forgotPass", state='normal')
    tk.title("Login Screen")

def loginCursor(e):
    c_Hand2()
    
def loginBack(e):
    c_Arrow()

canvas.tag_bind("goLogIn", "<Enter>", loginCursor)
canvas.tag_bind("goLogIn", "<Leave>", loginBack)
canvas.tag_bind("goLogIn", "<Button-1>", loginScreen)

#Sign up Text
canvas.create_text(230, 510, text="Don't have an account? Sign up", font=("Roboto Slab", 9), justify="left", anchor="w", tags="goSignUp")
def signUpScreen(e):
    canvas.itemconfig("signUp", state='normal')
    canvas.itemconfig("goLogIn", state='normal')
    canvas.itemconfig("hintForgotPass", state='normal')
    canvas.itemconfig("errInputPass", state='hidden')
    canvas.itemconfig("noEmptyPass", state='hidden')
    canvas.itemconfig("noEmpty", state='hidden')
    canvas.itemconfig("login", state='hidden')
    canvas.itemconfig("goSignUp", state='hidden')
    canvas.itemconfig("remCButton", state='hidden')
    canvas.itemconfig("forgotPass", state='hidden')
    tk.title("Sign Up Screen")

def signUpCursor(e):
    c_Hand2()
    
def signUpBack(e):
    c_Arrow()

canvas.tag_bind("goSignUp", "<Enter>", signUpCursor)
canvas.tag_bind("goSignUp", "<Leave>", signUpBack)
canvas.tag_bind("goSignUp", "<Button-1>", signUpScreen)

tk2.mainloop()
tk.mainloop()
