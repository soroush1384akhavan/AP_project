from tkinter import Tk, Canvas, PhotoImage, StringVar, Entry, Button, Listbox, END
import re

# Constants
BG_COLOR_BACK = "#393939"
FONT_LABEL = ('Khula', 50)
FONT_STYLE_ENTRY = ('Kdam Thmor', 28)
FONT_BUTTON = ('Kdam Thmor', 28)
TEXT_COLOR_ENTRY = "#BDB7B4"
BG_COLOR_ENTRY = "#888888"

class Signup(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)
        self.setup_ui()
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="Signup_6.png")
        self.canvas = Canvas(width=1125, height=800, highlightthickness=0, bg=BG_COLOR_BACK)
        self.canvas.create_image(562, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)
        
        self.city_var = StringVar()
        
        self.city_entry = Entry(
            master=self,
            font=FONT_STYLE_ENTRY,
            width=40,
            textvariable=self.city_var
        )
        self.city_entry.place(x=400, y=200)
        self.city_entry.bind("<KeyRelease>", self.show_suggestions)
        
        self.suggestion_listbox = Listbox(
            master=self,
            font=FONT_STYLE_ENTRY,
            width=40,
            height=4
        )
        self.suggestion_listbox.bind("<<ListboxSelect>>", self.insert_suggestion)
        
    def show_suggestions(self, event):
        typed_text = self.city_var.get().lower()
        suggestions = ["New York", "London", "Paris", "Tokyo"]  # Or any other list of suggestions
        matched_cities = [city for city in suggestions if typed_text in city.lower()]
        self.suggestion_listbox.delete(0, END)
        for city in matched_cities:
            self.suggestion_listbox.insert(END, city)
        if matched_cities:
            self.suggestion_listbox.place(x=400, y=240)  # Adjust the position as needed
        else:
            self.suggestion_listbox.place_forget()
        
    def insert_suggestion(self, event):
        selected_index = self.suggestion_listbox.curselection()
        if selected_index:
            selected_suggestion = self.suggestion_listbox.get(selected_index)
            self.city_entry.delete(0, END)
            self.city_entry.insert(0, selected_suggestion)
            self.suggestion_listbox.place_forget()

def start():
    app = Signup()
    app.mainloop()

if __name__ == "__main__":
    start()
