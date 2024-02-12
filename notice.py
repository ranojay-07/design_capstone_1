import mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def removeSeparator(a):
    temp = ""
    f_temp = ""
    for i in range (len(a)):
        if (a[i] != "ṇ"):
            temp = temp + a[i]
        else:
            if (f_temp == ""):
                f_temp = temp
            else:
                f_temp = f_temp + "\n" + temp
            temp = ""

    if (temp != "" ):
        f_temp = f_temp + "\n" + temp

    return (f_temp)

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rootroot',
    database='xim'
)

cursor = connection.cursor()

query = "Select * from notice where n_id = 1"

cursor.execute(query)
result = cursor.fetchall()[0]
date = result[1]
head = result[2]
content = removeSeparator(result[3])
fromW = result[4]
desi = result[5] 

connection.commit()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("800x625")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 625,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.17142868041992188,
    800.0,
    625.1714286804199,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    347,
    113.17142868041992,
    anchor="nw",
    text="NOTICE",
    fill="#000000",
    font=("Georgia", 26 * -1,"bold")
)

canvas.create_text(
    37.0,
    153.84867477416992,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("Georgia", 16 * -1,"bold")
)

canvas.create_text(
    88.47013854980469,
    153.17142868041992,
    anchor="nw",
    text=date,
    fill="#000000",
    font=("Georgia", 16 * -1,"bold")
)

canvas.create_text(
    405-(len(head)//2)*11.875,
    181.17142868041992,
    anchor="nw",
    text=head,
    fill="#000000",
    font=("Georgia", 20 * -1,"bold")
)

canvas.create_text(
    37.0,
    534.171459197998,
    anchor="nw",
    text=fromW + ",",
    fill="#000000",
    font=("Georgia", 16 * -1,"bold")
)

canvas.create_text(
    37.0,
    554.171459197998,
    anchor="nw",
    text="(" + desi + ")",
    fill="#000000",
    font=("Georgia", 11 * -1)
)

canvas.create_text(
    37.0,
    230,
    anchor="nw",
    text=content,
    fill="#000000",
    font=("Helvetica", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("xim.png"))
image_1 = canvas.create_image(
    405.0,
    61.17142868041992,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()