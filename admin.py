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
    import admin_info
    while True:
        if os.path.exists("close.pickle"):
            with open("close.pickle","rb") as closeid:
                close = pickle.load(closeid)
            if (close == "close"):
                if os.path.exists("close.pickle"):
                    os.remove("close.pickle")
            break
        else:
            importlib.reload(admin_info)

def show_add_edit ( ):
    window.destroy()
    import add_edit
    while True:
        if os.path.exists("close.pickle"):
            with open("close.pickle","rb") as closeid:
                close = pickle.load(closeid)
            if (close == "close"):
                if os.path.exists("close.pickle"):
                    os.remove("close.pickle")
            break
        else:
            importlib.reload(add_edit)

def show_add_notice ( ):
    window.destroy()
    import add_notice
    while True:
        if os.path.exists("close.pickle"):
            with open("close.pickle","rb") as closeid:
                close = pickle.load(closeid)
            if (close == "close"):
                if os.path.exists("close.pickle"):
                    os.remove("close.pickle")
            break
        else:
            importlib.reload(add_notice)
            

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
    fill="#2F6690",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    284.9444274902344,
    464.0,
    fill="#16425B",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("a_logout.png"))
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
    file=relative_to_assets("a_info.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_info(),
    relief="flat"
)
button_2.place(
    x=381.0,
    y=180.0,
    width=185.08334350585938,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("a_add_edit.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_add_edit(),
    relief="flat"
)
button_3.place(
    x=634.4888916015625,
    y=180.0,
    width=185.4888916015625,
    height=49.05142593383789
)

button_image_4 = PhotoImage(
    file=relative_to_assets("a_add_notice.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_add_notice(),
    relief="flat"
)
button_4.place(
    x=381.4888916015625,
    y=306.0,
    width=188.0,
    height=52.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("a_view_noticeboard.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=637.4888916015625,
    y=308.0,
    width=185.42596435546875,
    height=50.365692138671875
)

canvas.create_text(
    483.0,
    86.0,
    anchor="nw",
    text="WELCOME",
    fill="#0D3B66",
    font=("SofiaSansRoman ExtraBold", 40 * -1)
)

canvas.create_text(
    88.0,
    334.0,
    anchor="nw",
    text=id.upper(),
    fill="#FFFFFF",
    font=("InriaSans Bold", 24 * -1)
)

canvas.create_text(
    117.0,
    361.0,
    anchor="nw",
    text="Admin",
    fill="#FFFFFF",
    font=("InriaSans Bold", 16 * -1)
)

img = Image.open ( relative_to_assets ( f"photos/{id}.png" ) )
img = img.resize ( ( 234 , 234 ) )
if not os.path.exists ( f"temporary/temp{id}).png" ):
    img.save ( f"temporary/temp{id}.png" )

admin_profile_image = PhotoImage( 
    file = ( f"temporary/temp{id}.png" ) )

image_1 = canvas.create_image(
    142.0,
    194.0,
    image=admin_profile_image
)

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()