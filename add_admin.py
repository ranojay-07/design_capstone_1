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
    INSERT INTO admin (a_id, f_name, l_name, dept_name, email, phone, salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (admin_id.get(), f_name.get(), l_name.get(), dept.get(), admin_id.get() + "@xim.edu.in" ,phone.get(), float(salary.get()))

    cursor.execute(query, values)

    connection.commit()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='xim'
    )
    cursor = connection.cursor()
    
    query = f"""
    INSERT INTO login (id, password, changing_permission)
    VALUES (%s, "Password@123", 1)
    """

    values = admin_id.get()

    cursor.execute(query, admin_id.get())

    connection.commit()

    img = Image.open ( "upload\\" + profile_picture.get() )
    if not os.path.exists ( f"images/photos/{admin_id.get()}.png" ):
        img.save ( f"images/photos/{admin_id.get()}.png" )

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
    427.43861389160156,
    93.31240844726562,
    image=entry_image_1
)
admin_id = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
admin_id.place(
    x=258.0,
    y=77.0,
    width=338.8772277832031,
    height=30.62481689453125
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_2 = canvas.create_image(
    427.43861389160156,
    150.31241607666016,
    image=entry_image_2
)
f_name = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
f_name.place(
    x=258.0,
    y=134.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_3 = canvas.create_image(
    427.43861389160156,
    206.31241607666016,
    image=entry_image_3
)
l_name = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
l_name.place(
    x=258.0,
    y=190.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_4 = canvas.create_image(
    427.23377990722656,
    264.98828887939453,
    image=entry_image_4
)
dept = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
dept.place(
    x=257.795166015625,
    y=248.67587280273438,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_5 = canvas.create_image(
    427.43861389160156,
    322.31241607666016,
    image=entry_image_5
)
phone = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
phone.place(
    x=258.0,
    y=306.0,
    width=338.8772277832031,
    height=30.624832153320312
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_6 = canvas.create_image(
    427.5,
    428.0,
    image=entry_image_6
)
profile_picture = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
profile_picture.place(
    x=258.0,
    y=413.0,
    width=339.0,
    height=28.0
)

canvas.create_text(
    141.0,
    87.0,
    anchor="nw",
    text="Admin Id:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    128.0,
    142.0,
    anchor="nw",
    text="First Name:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    130.0,
    199.0,
    anchor="nw",
    text="Last Name:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    167.0,
    313.0,
    anchor="nw",
    text="Phone:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("add_admin_entry.png"))
entry_bg_7 = canvas.create_image(
    427.43861389160156,
    378.3124141693115,
    image=entry_image_7
)
salary = Entry(
    bd=0,
    bg="#89C2D9",
    fg="#000716",
    highlightthickness=0
)
salary.place(
    x=258.0,
    y=362.0,
    width=338.8772277832031,
    height=30.624828338623047
)

canvas.create_text(
    164.0,
    369.0,
    anchor="nw",
    text="Salary:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    56.0,
    255.0,
    anchor="nw",
    text="Department Name:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    88.0,
    417.0,
    anchor="nw",
    text="Profile Picture:",
    fill="#000000",
    font=("Georgia", 21 * -1)
)

canvas.create_text(
    270.0,
    3.0,
    anchor="nw",
    text="Add New Admin",
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
    x=353.0,
    y=452.0,
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