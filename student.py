import os, pickle, sys, importlib
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

def show_info ( ):
    window.destroy()
    import student_info
    while True:
        if os.path.exists("close.pickle"):
            with open("close.pickle","rb") as closeid:
                close = pickle.load(closeid)
            if (close == "close"):
                if os.path.exists("close.pickle"):
                    os.remove("close.pickle")
            break
        else:
            importlib.reload(student_info)

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
    file=relative_to_assets("s_info.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_info(),
    relief="flat"
)
button_2.place(
    x=370.0,
    y=185.0,
    width=185.08334350585938,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("s_view_grades.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=623.0,
    y=185.0,
    width=185.4888916015625,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("s_courses.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=368.0,
    y=312.0,
    width=187.59445190429688,
    height=52.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("s_view_noticeboard.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=623.0,
    y=312.0,
    width=185.0,
    height=50.365692138671875
)

canvas.create_text(
    493.0,
    91.0,
    anchor="nw",
    text="Welcome",
    fill="#3B28CC",
    font=("Graduate Regular", 40 * -1)
)

canvas.create_text(
    97.0,
    337.0,
    anchor="nw",
    text = id.upper() ,
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

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()