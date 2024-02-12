from tkinter import *
from PIL import Image, ImageTk
import mysql.connector, pickle, os, sys, importlib

def destroy_info():
    if os.path.exists("id.pickle"):
        os.remove("id.pickle")
    if os.path.exists(f"temporary/temp{id}.png"):
        os.remove(f"temporary/temp{id}.png")

def on_closing():
    destroy_info()
    root.destroy()
    sys.exit()

def loginuser():
    id = user.get()
    with open("id.pickle", "wb") as uid:
        pickle.dump(id, uid)
    password = code.get()
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='xim'
    )
    cursor = connection.cursor()
    query = "SELECT * FROM login WHERE id = %s AND password = SHA(%s)"
    cursor.execute(query, (id, password))
    results = cursor.fetchone()

    if results is not None:
        root.destroy()
        if (id[2] == "s"):
            import student
            while True:
                if os.path.exists("close.pickle"):
                    with open("close.pickle","rb") as closeid:
                        close = pickle.load(closeid)
                    if (close == "logout"):
                        if os.path.exists("close.pickle"):
                            os.remove("close.pickle")
                        break
                elif not os.path.exists("id.pickle"):
                    break
                else:
                    importlib.reload(student)
        elif (id[2] == "f"):
            import faculty
            while True:
                if os.path.exists("close.pickle"):
                    with open("close.pickle","rb") as closeid:
                        close = pickle.load(closeid)
                    if (close == "logout"):
                        if os.path.exists("close.pickle"):
                            os.remove("close.pickle")
                        break
                elif not os.path.exists("id.pickle"):
                    break
                else:
                    importlib.reload(faculty)
        else:
            import admin
            while True:
                if os.path.exists("close.pickle"):
                    with open("close.pickle","rb") as closeid:
                        close = pickle.load(closeid)
                    if (close == "logout"):
                        if os.path.exists("close.pickle"):
                            os.remove("close.pickle")
                        break
                elif not os.path.exists("id.pickle"):
                    break
                else:
                    importlib.reload(admin)
    else:
        label = Label(frame, text="Invalid Id or Password", fg='red', bg='white', font=('Microsoft YaHei UI Light', 10))
        label.place(x=110, y = 250)

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='images/login.png')

Label(root, image=img, bg='white').place(x=50,y=50)

frame = Frame(root, width=350, height=350,bg='white')
frame.place(x=500, y=70)

heading= Label(frame, text='Sign In', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)


""" id ENTRY """
def user_focus_in(e):
    user.delete(0, 'end')

def user_focus_out(e):
    name = user.get()
    if name =='':
        user.insert(0, 'id')

user = Entry(frame, width=25, fg='black', border = 0, bg='white',font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'User-id')
user.bind("<FocusIn>", user_focus_in)
user.bind("<FocusOut>",user_focus_out)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

""" PW Entry """
def code_focus_in(e):
    code.delete(0, 'end')

def code_focus_out(e):
    name = code.get()
    if name =='':
       code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border = 0, bg='white',font=('Microsoft YaHei UI Light', 11), show = "*")
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", code_focus_in)
code.bind("<FocusOut>",code_focus_out)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

""" Submit button """
Button(frame, width=39, pady=7, text='Sign In',bg='#57a1f8', fg='white', border=0, command=loginuser).place(x=35, y=204)

button_mode = True

def hide():
    global button_mode
    if not button_mode:
        eyeButton.config(image = closeeye, activebackground="white")
        code.config(show = "*")
        button_mode = True
    else:
        eyeButton.config(image = openeye, activebackground="white")
        code.config(show="")
        button_mode = False

openi = Image.open("images\show.png")
openi = openi.resize((25, 25))
openeye = ImageTk.PhotoImage(openi)

closei = Image.open("images\hide.png")
closei = closei.resize((25, 25))
closeeye = ImageTk.PhotoImage(closei)

eyeButton = Button(image = closeeye, bd = 0, command = hide)
eyeButton.place(x = 795, y = 220)

loginButton = Button(root, text = "LOGIN", width = 10, height = 1, font = ("arial", 20, "bold"), bd = 0, fg = "black",  command = loginuser)
loginButton.place (x = 570, y = 600)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()