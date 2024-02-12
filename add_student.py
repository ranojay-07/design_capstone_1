import os, pickle, sys, importlib, mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image

with open("id.pickle","rb") as uid:
    id = pickle.load(uid)

def on_closing():
    destroy_info()
    window.destroy()
    sys.exit()

def back_to_add():
    window.destroy ()
    with open("close.pickle", "wb") as closeid:
        pickle.dump("close", closeid)

def destroy_info():
    if os.path.exists("id.pickle"):
        os.remove("id.pickle")
    if os.path.exists(f"temporary/temp{id}.png"):
        os.remove(f"temporary/temp{id}.png")

def submit ():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='xim'
    )
    cursor = connection.cursor()
    
    query = f"""
    INSERT INTO student (s_id, f_name, l_name, dept_name, email, phone)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (student_id.get(), f_name.get(), l_name.get(), dept.get(), student_id.get() + "@xim.edu.in" , phone.get())

    cursor.execute(query, values)

    connection.commit()

    img = Image.open ( "upload\\" + profile_picture.get() )
    if not os.path.exists ( f"images/photos/{student_id.get()}.png" ):
        img.save ( f"images/photos/{student_id.get()}.png" )

    back_to_add()

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
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_1 = canvas.create_image(
    429.43861389160156,
    114.31240844726562,
    image=entry_image_1
)
student_id = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
student_id.place(
    x=260.0,
    y=98.0,
    width=338.8772277832031,
    height=30.62481689453125
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_2 = canvas.create_image(
    429.43861389160156,
    169.31241607666016,
    image=entry_image_2
)
f_name = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
f_name.place(
    x=260.0,
    y=153.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_3 = canvas.create_image(
    429.43861389160156,
    225.31241607666016,
    image=entry_image_3
)
l_name = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
l_name.place(
    x=260.0,
    y=209.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_4 = canvas.create_image(
    429.23377990722656,
    283.98828887939453,
    image=entry_image_4
)
dept = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
dept.place(
    x=259.795166015625,
    y=267.6758728027344,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_5 = canvas.create_image(
    429.43861389160156,
    341.3124141693115,
    image=entry_image_5
)
phone = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
phone.place(
    x=260.0,
    y=325.0,
    width=338.8772277832031,
    height=30.624828338623047
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_6 = canvas.create_image(
    428.5,
    397.0,
    image=entry_image_6
)
profile_picture = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
profile_picture.place(
    x=259.0,
    y=382.0,
    width=339.0,
    height=28.0
)

canvas.create_text(
    137.0,
    106.0,
    anchor="nw",
    text="Student Id:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    130.0,
    161.0,
    anchor="nw",
    text="First Name:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    132.0,
    218.0,
    anchor="nw",
    text="Last Name:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    171.0,
    332.0,
    anchor="nw",
    text="Phone:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    63.0,
    274.0,
    anchor="nw",
    text="Department Name:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    97.0,
    386.0,
    anchor="nw",
    text="Profile Picture:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    277.0,
    3.0,
    anchor="nw",
    text="Add New Student",
    fill="#FEFAE0",
    font=("Bookman Old Style", 37 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("add_admin_submit.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit(),
    relief="flat"
)
button_1.place(
    x=355.0,
    y=442.0,
    width=148.5,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("a_back_3.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_add(),
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