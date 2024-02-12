from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"images/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

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
canvas.create_rectangle(
    0.0,
    0.0,
    929.7979125976562,
    92.09426879882812,
    fill="#335C67",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("notice_button_admin.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=210.0,
    y=149.0,
    width=500.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("notice_button_admin.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=210.0,
    y=238.0,
    width=500.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("a_back_4.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=35.0,
    y=31.0,
    width=37.8560791015625,
    height=33.64982604980469
)

button_image_4 = PhotoImage(
    file=relative_to_assets("a_logout_2.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=807.0,
    y=31.0,
    width=90.0,
    height=30.0
)

canvas.create_text(
    343.0,
    25.0,
    anchor="nw",
    text="View Notice",
    fill="#FCE0B7",
    font=("HammersmithOne Regular", 42 * -1)
)
window.resizable(False, False)
window.mainloop()