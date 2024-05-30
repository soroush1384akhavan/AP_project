from tkinter import *
from customtkinter import *

# Constants
BG_COLOR_BACK = "#FBE5B6"
FONT_LABEL = ('Kaisei Opi', 75)
FONT_STYLE_ENTRY = ('Kdam Thmor', 28.13)
FONT_BUTTON = ('Kdam Thmor', 28.13)
TEXT_COLOR_ENTRY = "#BDB7B4"
BG_COLOR_ENTRY = "#F3EBE8"
LOG_IN_BUTTON_COLOR_OFF = "#F3EBE8"
LOG_IN_BUTTON_COLOR_ON = "#D5CCC8"
LOG_IN_BUTTON_COLOR_CLICK = "#B5ACA9"
SIGN_IN_BUTTON_COLOR_ON = "#C0AC6F"
SIGN_IN_BUTTON_COLOR_OFF = "#E6CD80"
SIGN_IN_BUTTON_COLOR_CLICK = "#9A8A57"

class Signup(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)

        self.setup_ui()
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="back_ground.png")
        self.canvas = Canvas(width=1201, height=800, highlightthickness=0, bg=BG_COLOR_BACK)
        self.canvas.create_image(550, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)
        
if __name__ == "__main__":
    app = Signup()
    app.mainloop()