import os, pickle, sys, mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
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

def back_to_mainDB():
    window.destroy ()
    with open("close.pickle", "wb") as closeid:
        pickle.dump("close", closeid)

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rootroot',
    database='xim'
)

cursor = connection.cursor()
query = f"SELECT f_name, l_name, dept_name, phone FROM student WHERE s_id = '{id}';"
cursor.execute(query)
s_info = []
for i in cursor.fetchone():
    s_info.append(i)

name = s_info[0] + " " + s_info[1]
dept = s_info[2]
phone = "+91" + s_info[3]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("892x464")
window.configure(bg = "#FEFAE0")

canvas = Canvas(
    window,
    bg = "#FEFAE0",
    height = 464,
    width = 892,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    285.0,
    0.0,
    892.0555419921875,
    58.3314208984375,
    fill="#8093F1",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    284.9444274902344,
    464.0,
    fill="#B388EB",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("s_logout.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_login(),
    relief="flat"
)
button_1.place(
    x=765.0,
    y=10.0,
    width=115.2166748046875,
    height=38.445709228515625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("s_back.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_mainDB(),
    relief="flat"
)
button_2.place(
    x=25.0,
    y=13.0,
    width=33.0,
    height=33.0
)

canvas.create_text(
    97.0,
    337.0,
    anchor="nw",
    text=id.upper(),
    fill="#000000",
    font=("InriaSans Bold", 20 * -1)
)

canvas.create_text(
    113.0,
    364.0,
    anchor="nw",
    text="Student",
    fill="#000000",
    font=("InriaSans Bold", 16 * -1)
)

img = Image.open ( relative_to_assets ( f"photos/{id}.png" ) )
img = img.resize ( ( 234 , 234 ) )
if not os.path.exists ( f"temporary/temp{id}).png" ):
    img.save ( f"temporary/temp{id}.png" )

student_profile_image = PhotoImage( 
    file = ( f"temporary/temp{id}.png" ) )

image_1 = canvas.create_image(
    142.0,
    194.0,
    image=student_profile_image
)

canvas.create_text(
    418.0,
    174.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("HammersmithOne Regular", 16 * -1)
)

canvas.create_text(
    375.0,
    218.0,
    anchor="nw",
    text="Department:",
    fill="#000000",
    font=("HammersmithOne Regular", 16 * -1)
)

canvas.create_text(
    412.0,
    266.0,
    anchor="nw",
    text="Phone:",
    fill="#000000",
    font=("HammersmithOne Regular", 16 * -1)
)

canvas.create_text(
    481.0,
    174.0,
    anchor="nw",
    text=name,
    fill="#000000",
    font=("HammersmithOne Regular", 14 * -1)
)

canvas.create_text(
    482.0,
    267.0,
    anchor="nw",
    text=phone,
    fill="#000000",
    font=("HammersmithOne Regular", 14 * -1)
)

canvas.create_text(
    483.0,
    218.0,
    anchor="nw",
    text=dept,
    fill="#000000",
    font=("HammersmithOne Regular", 14 * -1)
)

canvas.create_rectangle(
    475.0,
    235.0,
    788.0,
    238.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    479.0,
    284.0,
    792.0,
    287.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    476.0,
    193.0,
    789.0,
    196.0,
    fill="#000000",
    outline="")
window.resizable(False, False) 
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()