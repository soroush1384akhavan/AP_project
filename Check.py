import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Page Switcher")
        self.geometry("600x400")
        
        self.container = tk.Frame(self)
        self.container.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(relx=1, rely=0, relwidth=1, relheight=1)  # Initially place the frame off-screen to the right

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        self.slide_in(frame)

    def slide_in(self, frame):
        for other_frame in self.frames.values():
            other_frame.place_forget()
        
        frame.place(relx=1, rely=0, relwidth=1, relheight=1)  # Place the new frame off-screen to the right
        
        def update_position(x):
            frame.place_configure(relx=x)
            self.update()

        steps = 20
        duration = 100  # Total duration in milliseconds
        delay = duration // steps
        
        for i in range(steps):
            x = 1 - (i + 1) / steps
            self.after(delay * i, update_position, x)
        
        # Ensure the final position is set
        self.after(duration, frame.place_configure, {'relx': 0})

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Start Page", font=("Verdana", 24))
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page One", font=("Verdana", 24))
        label.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Go back to Start Page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
