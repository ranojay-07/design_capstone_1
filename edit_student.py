import os, pickle, sys, importlib, mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image

def back_to_edit():
    window.destroy ()
    with open("close.pickle", "wb") as closeid:
        pickle.dump("close", closeid)

def destroy_info():
    if os.path.exists("id.pickle"):
        os.remove("id.pickle")
    if os.path.exists(f"temporary/temp{id}.png"):
        os.remove(f"temporary/temp{id}.png")

def on_closing():
    destroy_info()
    window.destroy()
    sys.exit()

with open("id.pickle","rb") as uid:
    id = pickle.load(uid)

with open("eid.pickle","rb") as uid:
    eid = pickle.load(uid)
if os.path.exists("eid.pickle"):
        os.remove("eid.pickle")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rootroot',
    database='xim'
)
cursor = connection.cursor()
query = f"SELECT * FROM student WHERE s_id = \"{eid}\""
cursor.execute(query)
result = cursor.fetchall()
result = result[0]

def edit_button():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='xim'
    )
    cursor = connection.cursor()
    query = f"UPDATE student SET f_name=\"{f_name.get()}\", l_name=\"{l_name.get()}\", dept_name=\"{dept.get()}\",phone=\"{phone.get()}\" WHERE s_id=\"{eid}\";"
    cursor.execute(query)
    connection.commit()
    if ( profile_picture.get() != f"photos/{eid}.png" ) :
        if os.path.exists(f"photos/{eid}.png"):
            os.remove(f"photos/{eid}.png")
        img = Image.open ( profile_picture.get())
        img.save ( relative_to_assets( f"photos/{eid}.png") )
    
    back_to_edit()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("780x500")
window.configure(bg = "#FEFAE0")

canvas = Canvas(
    window,
    bg = "#FEFAE0",
    height = 500,
    width = 780,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    780.0,
    55.777923583984375,
    fill="#2F6690",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("edit_admin_entry.png"))
entry_bg_1 = canvas.create_image(
    422.43861389160156,
    120.31240844726562,
    image=entry_image_1
)
f_name = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
f_name.place(
    x=253.0,
    y=104.0,
    width=338.8772277832031,
    height=30.62481689453125
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("edit_admin_entry.png"))
entry_bg_2 = canvas.create_image(
    422.43861389160156,
    176.31241607666016,
    image=entry_image_2
)
l_name = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
l_name.place(
    x=253.0,
    y=160.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("edit_admin_entry.png"))
entry_bg_3 = canvas.create_image(
    422.23377990722656,
    234.98828887939453,
    image=entry_image_3
)
dept = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
dept.place(
    x=252.795166015625,
    y=218.67587280273438,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("edit_admin_entry.png"))
entry_bg_4 = canvas.create_image(
    422.43861389160156,
    292.31241607666016,
    image=entry_image_4
)
phone = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
phone.place(
    x=253.0,
    y=276.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("edit_admin_entry.png"))
entry_bg_5 = canvas.create_image(
    421.5,
    348.0,
    image=entry_image_5
)
profile_picture = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
profile_picture.place(
    x=252.0,
    y=333.0,
    width=339.0,
    height=28.0
)

canvas.create_text(
    123.0,
    112.0,
    anchor="nw",
    text="First Name:",
    fill="#000000",
    font=("Kurale Regular", 21 * -1)
)

canvas.create_text(
    125.0,
    169.0,
    anchor="nw",
    text="Last Name:",
    fill="#000000",
    font=("Kurale Regular", 21 * -1)
)

canvas.create_text(
    164.0,
    283.0,
    anchor="nw",
    text="Phone:",
    fill="#000000",
    font=("Kurale Regular", 21 * -1)
)

canvas.create_text(
    51.0,
    225.0,
    anchor="nw",
    text="Department Name:",
    fill="#000000",
    font=("Kurale Regular", 21 * -1)
)

canvas.create_text(
    82.0,
    337.0,
    anchor="nw",
    text="Profile Picture:",
    fill="#000000",
    font=("Kurale Regular", 21 * -1)
)

canvas.create_text(
    270.0,
    3.0,
    anchor="nw",
    text="Edit New Student",
    fill="#FEFAE0",
    font=("Kurale Regular", 37 * -1)
)

f_name.insert(0, result[1])
l_name.insert(0, result[2])
dept.insert(0, result[3])
phone.insert(0, result[5])
profile_picture.insert(0, f"photos/{eid}.png")

button_image_1 = PhotoImage(
    file=relative_to_assets("edit_button.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: edit_button(),
    relief="flat"
)
button_1.place(
    x=365.0,
    y=398.0,
    width=114.23076629638672,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("edit_back.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_edit(),
    relief="flat"
)
button_2.place(
    x=11.0,
    y=12.0,
    width=39.0,
    height=34.0
)
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()