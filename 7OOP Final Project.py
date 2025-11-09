from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

tk = Tk()
tk.title("Okay")
tk.geometry("800x600") # W x H

canvas = Canvas(tk, width=800, height=600)
canvas.pack()

#Login Icon Widget
iconImg = Image.open("tkinter GUI images/1-LoginIcon.png")
iconImgResize = iconImg.resize((200, 200))
iconImage = ImageTk.PhotoImage(iconImgResize)
canvas.create_image(290, 30, anchor="nw", image=iconImage)

userImg = Image.open("tkinter GUI images/1-Username.png")
userImgResize = userImg.resize((374, 50))
userImage = ImageTk.PhotoImage(userImgResize)
canvas.create_image(200, 250, anchor="nw", image=userImage, tags="hintLogin")

userEmptyImg = Image.open("tkinter GUI images/3-EmptyLogin.png")
userEmptyImgResize = userEmptyImg.resize((374, 50))
userEmptyImage = ImageTk.PhotoImage(userEmptyImgResize)
canvas.create_image(200, 250, anchor="nw", image=userEmptyImage, tags="emptyLogin")

userInput = Entry(tk, width=27, bd=0, bg=tk["bg"], highlightthickness=0, font=("Roboto Slab", 15))
canvas.create_window(370, 275, window=userInput, tags="userEntry")

canvas.itemconfig("emptyLogin", state='hidden')
canvas.itemconfig("userEntry", state='hidden')

def flip(e):
    canvas.itemconfig("hintLogin", state='hidden')
    canvas.itemconfig("emptyLogin", state='normal')
    canvas.itemconfig("userEntry", state='normal')

def flipBack(e):
    if tk.focus_get() == userInput or userInput.get() != '':
        return
    else:
        canvas.itemconfig("hintLogin", state='normal')
        canvas.itemconfig("emptyLogin", state='hidden')
        canvas.itemconfig("userEntry", state='hidden')

canvas.tag_bind("hintLogin", "<Enter>", flip)
canvas.tag_bind("emptyLogin", "<Leave>", flipBack)

#Error Text User
canvas.create_text(230, 306, text="Input can only contain letters, underscores, and numbers.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="notAllowed")
canvas.itemconfig("notAllowed", state='hidden')
canvas.create_text(230, 306, text="* This is a required field and cannot be left empty.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="noEmpty")
canvas.itemconfig("noEmpty", state='hidden')

def errTextUser():
    notAllowed = [' ', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '\\', '|', ';', ':', '\'', '"', ',', '.', '>', '<', '/', '?']
    n = len(notAllowed)

    input = userInput.get()
    passValue = 0

    if '' == input:
        canvas.itemconfig("noEmpty", state='normal')
        canvas.itemconfig("notAllowed", state='hidden')
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

passInput = Entry(tk, width=27, bd=0, bg=tk["bg"], highlightthickness=0, font=("Roboto Slab", 15), show="•")
canvas.create_window(370, 343, window=passInput, tags="passEntry")

canvas.itemconfig("emptyPass", state='hidden')
canvas.itemconfig("passEntry", state='hidden')

def flip(e):
    canvas.itemconfig("hintPass", state='hidden')
    canvas.itemconfig("emptyPass", state='normal')
    canvas.itemconfig("passEntry", state='normal')

def flipBack(e):
    if tk.focus_get() == passInput or passInput.get() != '':
        return
    else:
        canvas.itemconfig("hintPass", state='normal')
        canvas.itemconfig("emptyPass", state='hidden')
        canvas.itemconfig("passEntry", state='hidden')

canvas.tag_bind("hintPass", "<Enter>", flip)
canvas.tag_bind("emptyPass", "<Leave>", flipBack)

#Error Text Pass
canvas.create_text(230, 374, text="Username or password input is incorrect.", font=("Roboto Slab", 9), fill="#af4c49", justify="left", anchor="w", tags="errP")
canvas.itemconfig("errP", state='hidden')
# alt text: A password must have at least 8 characters.

#Remember Me Button and Forgot Password
style = ttk.Style()
style.configure('RM.TCheckbutton', font=("Roboto Slab", 9))
rememberMe = ttk.Checkbutton(tk, text="Remember Me", takefocus=0, cursor="hand2", style='RM.TCheckbutton')
canvas.create_window(282, 395, window=rememberMe)

canvas.create_text(542, 395, text="Forgot password?", font=("Roboto Slab", 9), justify="right", anchor="e")

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

def flipLog(e):
    tk.config(cursor="hand2")
    canvas.itemconfig("login", state='hidden')
    canvas.itemconfig("loginHover", state='normal')

def flipLogBack(e):
    tk.config(cursor="arrow")
    canvas.itemconfig("login", state='normal')
    canvas.itemconfig("loginHover", state='hidden')

def submitLog(e):
    tk.config(cursor="hand2")
    errTextUser()
    print(passInput.get())

#Database Functions
def submit(e):
    tk.config(cursor="hand2")
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

canvas.tag_bind("login", "<Enter>", flipLog)
canvas.tag_bind("loginHover", "<Leave>", flipLogBack)
canvas.tag_bind("loginHover", "<Button-1>", submit)

#Sign up Text
canvas.create_text(230, 510, text="Don't have an account? Sign up", font=("Roboto Slab", 9), justify="left", anchor="w")

Button(tk, text="Sample", command=errTextUser).pack()

tk.mainloop()