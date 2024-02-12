import os, pickle, sys, importlib, mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from PIL import Image

def clear_content():
   content.delete(0, 'end')

with open("id.pickle","rb") as uid:
    id = pickle.load(uid)

def seperator (strings):
    final_string = ""
    clear_content()
    previous_sentence = ""
    sentence = ""
    
    word = ""
    c = 0

    for i in range ( len ( strings ) ) :
        if ( strings[i] != " " ):
            word = word + strings[i]
            c = c + 1

        else:
            if c > 107:
                if (final_string == "" ):
                    final_string = previous_sentence
                else:
                    final_string = final_string + "ṇ" + previous_sentence
                sentence = ""
                c = len (word)

            if (sentence == "" ):
                sentence = word

            else:
                sentence = sentence + " " + word
                c = c + 1

            word = ""
            previous_sentence = sentence

    if ( (len(sentence) + len (word) + 1) > 108 ):
        final_string = final_string + "ṇ" + sentence + "ṇ" + word
    else:
        final_string = final_string + "ṇ" + sentence + " " + word
    
    if final_string[0] == "ṇ":
        final_string = final_string [1:]
    
    if not os.path.exists("notice.pickle"):
        with open("notice.pickle", "wb") as ns:
            pickle.dump(final_string, ns)
    else:
        with open("notice.pickle","rb") as ns:
            newFinalString = pickle.load(ns)
        newFinalString = newFinalString + "ṇṇ" +  final_string
        os.remove("notice.pickle")
        with open("notice.pickle", "wb") as ns:
            pickle.dump(newFinalString, ns)

def newPara ():
    strings = content.get()
    if len(strings) > 0:
        s_seperator = seperator(strings)

def submit ():
    newPara()
    with open("notice.pickle","rb") as ns:
        newFinalString = pickle.load(ns)

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootroot',
        database='xim'
    )
    cursor = connection.cursor()
    
    query = f"""
    INSERT INTO notice (n_date, n_heading, n_content, n_from, n_designation)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (date.get(), heading.get(), newFinalString, fromWhom.get(), designation.get())

    cursor.execute(query, values)

    connection.commit()

    if os.path.exists("notice.pickle"):
        os.remove("notice.pickle")
    
    back_to_mainDB()

def destroy_info():
    if os.path.exists("id.pickle"):
        os.remove("id.pickle")
    if os.path.exists(f"temporary/temp{id}.png"):
        os.remove(f"temporary/temp{id}.png")

def on_closing():
    destroy_info()
    window.destroy()
    sys.exit()

def back_to_mainDB():
    window.destroy ()
    with open("close.pickle", "wb") as closeid:
        pickle.dump("close", closeid)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

final_s = ""

window.geometry("929x526")
window.configure(bg = "#FFF3B0")


canvas = Canvas(
    window,
    bg = "#FFF3B0",
    height = 526,
    width = 929,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    180.646484375,
    143,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("HammersmithOne Regular", 24 * -1)
)

canvas.create_text(
    139.9124755859375,
    191.27272033691406,
    anchor="nw",
    text="Heading:",
    fill="#000000",
    font=("HammersmithOne Regular", 24 * -1)
)

canvas.create_text(
    142,
    244.40403747558594,
    anchor="nw",
    text="Content:",
    fill="#000000",
    font=("HammersmithOne Regular", 24 * -1)
)

canvas.create_text(
    172,
    289,
    anchor="nw",
    text="From:",
    fill="#000000",
    font=("HammersmithOne Regular", 24 * -1)
)

canvas.create_text(
   97,340,
    anchor="nw",
    text="Designation:",
    fill="#000000",
    font=("HammersmithOne Regular", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("new_para.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: newPara(),
    relief="flat"
)
button_1.place(
    x=706.646484375,
    y=247.94610595703125,
    width=104.4915771484375,
    height=26.760040283203125
)

canvas.create_rectangle(
    268.5036687850952,
    165.78314876556396,
    675.2608337402344,
    170.02020263671875,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    268.5036687850952,
    217.1434087753296,
    675.2608337402344,
    221.38046264648438,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    268.5036687850952,
    270.27472591400146,
    675.2608337402344,
    274.51177978515625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    268.5036687850952,
    319.86392879486084,
    675.2608337402344,
    324.1009826660156,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    268.5036687850952,
    367.6821355819702,
    675.2608337402344,
    371.919189453125,
    fill="#000000",
    outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("notice_submit.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit(),
    relief="flat"
)
button_2.place(
    x=400.2558898925781,
    y=421.5084228515625,
    width=148.76766967773438,
    height=47.81817626953125
)

canvas.create_rectangle(
    0.0,
    0.0,
    929.7979125976562,
    92.09426879882812,
    fill="#335C67",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("notice_back.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back_to_mainDB(),
    relief="flat"
)
button_3.place(
    x=35.4208984375,
    y=26.565658569335938,
    width=37.8560791015625,
    height=33.64982604980469
)

canvas.create_text(
    347.12457275390625,
    26.565658569335938,
    anchor="nw",
    text="Add Notice",
    fill="#FCE0B7",
    font=("HammersmithOne Regular", 42 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_1 = canvas.create_image(
    472.86866760253906,
    144.34006118774414,
    image=entry_image_1
)
date = Entry(
    bd=0,
    bg="#FFF3B0",
    fg="#000716",
    highlightthickness=0
)
date.place(
    x=272.74072265625,
    y=125.74410247802734,
    width=400.2558898925781,
    height=35.191917419433594
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_2 = canvas.create_image(
    472.86866760253906,
    195.70031356811523,
    image=entry_image_2
)
heading = Entry(
    bd=0,
    bg="#FFF3B0",
    fg="#000716",
    highlightthickness=0
)
heading.place(
    x=272.74072265625,
    y=177.10435485839844,
    width=400.2558898925781,
    height=35.191917419433594
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_3 = canvas.create_image(
    472.86866760253906,
    248.83164596557617,
    image=entry_image_3
)
content = Entry(
    bd=0,
    bg="#FFF3B0",
    fg="#000716",
    highlightthickness=0
)
content.place(
    x=272.74072265625,
    y=230.23568725585938,
    width=400.2558898925781,
    height=35.191917419433594
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_4 = canvas.create_image(
    472.86866760253906,
    300.1919059753418,
    image=entry_image_4
)
fromWhom = Entry(
    bd=0,
    bg="#FFF3B0",
    fg="#000716",
    highlightthickness=0
)
fromWhom.place(
    x=272.74072265625,
    y=281.595947265625,
    width=400.2558898925781,
    height=35.191917419433594
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry.png"))
entry_bg_5 = canvas.create_image(
    472.86866760253906,
    348.01011657714844,
    image=entry_image_5
)
designation = Entry(
    bd=0,
    bg="#FFF3B0",
    fg="#000716",
    highlightthickness=0
)
designation.place(
    x=272.74072265625,
    y=329.4141540527344,
    width=400.2558898925781,
    height=35.191925048828125
)

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()