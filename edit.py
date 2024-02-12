import os, pickle, sys, importlib, mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from PIL import Image

with open("id.pickle","rb") as uid:
    id = pickle.load(uid)

def destroy_info():
    if os.path.exists("id.pickle"):
        os.remove("id.pickle")
    if os.path.exists(f"temporary/temp{id}.png"):
        os.remove(f"temporary/temp{id}.png")

def on_closing():
    destroy_info()
    window.destroy()
    sys.exit()

def back_to_login():
    destroy_info()
    window.destroy()
    with open("close.pickle", "wb") as closeid:
        pickle.dump("logout", closeid)

def back_to_add_edit():
    window.destroy ()
    with open("close.pickle", "wb") as closeid:
        pickle.dump("close", closeid)

def id_detect():
    a = entry_1.get().lower()
    if a != "":
        b = a[2]
        if b == "s":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='rootroot',
                database='xim'
            )
            cursor = connection.cursor()
            query = f"SELECT s_id FROM student"
            cursor.execute(query)
            result = cursor.fetchall()
            all_ids = []
            for i in result:
                all_ids.append(i[0])
            if a in all_ids:
                with open("eid.pickle", "wb") as uid:
                    pickle.dump(a, uid)
                window.destroy()
                import edit_student
                while True:
                    if os.path.exists("close.pickle"):
                        with open("close.pickle","rb") as closeid:
                            close = pickle.load(closeid)
                        if (close == "close"):
                            if os.path.exists("close.pickle"):
                                os.remove("close.pickle")
                        break
                    else:
                        importlib.reload(edit_student)
            else:
                label = Label(window, text="Id not present in the database", fg='Red', bg='#FFF3B0', font=('Microsoft YaHei UI Light', 10))
                label.place(x=365, y = 235)
            connection.commit()
        elif b == "f":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='rootroot',
                database='xim'
            )
            cursor = connection.cursor()
            query = f"SELECT i_id FROM instructor"
            cursor.execute(query)
            result = cursor.fetchall()
            all_ids = []
            for i in result:
                all_ids.append(i[0])
            if a in all_ids:
                with open("eid.pickle", "wb") as uid:
                    pickle.dump(a, uid)
                window.destroy()
                import edit_faculty
                while True:
                    if os.path.exists("close.pickle"):
                        with open("close.pickle","rb") as closeid:
                            close = pickle.load(closeid)
                        if (close == "close"):
                            if os.path.exists("close.pickle"):
                                os.remove("close.pickle")
                        break
                    else:
                        importlib.reload(edit_faculty)
            else:
                label = Label(window, text="Id not present in the database", fg='Red', bg='#FFF3B0', font=('Microsoft YaHei UI Light', 10))
                label.place(x=365, y = 235)
            connection.commit()
        elif b == "a":
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='rootroot',
                database='xim'
            )
            cursor = connection.cursor()
            query = f"SELECT a_id FROM admin"
            cursor.execute(query)
            result = cursor.fetchall()
            all_ids = []
            for i in result:
                all_ids.append(i[0])
            if a in all_ids:
                with open("eid.pickle", "wb") as uid:
                    pickle.dump(a, uid)
                window.destroy()
                import edit_admin
                while True:
                    if os.path.exists("close.pickle"):
                        with open("close.pickle","rb") as closeid:
                            close = pickle.load(closeid)
                        if (close == "close"):
                            if os.path.exists("close.pickle"):
                                os.remove("close.pickle")
                        break
                    else:
                        importlib.reload(edit_admin)
            else:
                label = Label(window, text="Id not present in the database", fg='Red', bg='#FFF3B0', font=('Microsoft YaHei UI Light', 10))
                label.place(x=365, y = 235)
            connection.commit()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("924x450")
window.configure(bg = "#FFF3B0")

canvas = Canvas(
    window,
    bg = "#FFF3B0",
    height = 450,
    width = 924,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    924.494873046875,
    91.56901550292969,
    fill="#335C67",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("edit.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: id_detect(),
    relief="flat"
)
button_1.place(
    x=388.76995849609375,
    y=261.5,
    width=147.919189453125,
    height=47.54545211791992
)

button_image_2 = PhotoImage(
    file=relative_to_assets("a_back_5.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_add_edit(),
    relief="flat"
)
button_2.place(
    x=43.0,
    y=27.0,
    width=37.64013671875,
    height=33.457916259765625
)

button_image_3 = PhotoImage(
    file=relative_to_assets("a_logout_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_login(),
    relief="flat"
)
button_3.place(
    x=795.0,
    y=27.0,
    width=89.4866943359375,
    height=34.800384521484375
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_1 = canvas.create_image(
    462.1444854736328,
    207.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFF3B0",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=313.0,
    y=187.0,
    width=298.2889709472656,
    height=38.0
)

canvas.create_text(
    410.6445007324219,
    135.22433471679688,
    anchor="nw",
    text="Enter Id:",
    fill="#000000",
    font=("HammersmithOne Regular", 23 * -1)
)

canvas.create_rectangle(
    310.22054076194763,
    231.67110228538513,
    611.4924011230469,
    234.65399169921875,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()