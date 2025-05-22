import tkinter as tk

class OverlayGuide:
    def __init__(self, steps):
        self.root = tk.Tk()
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.7)
        self.root.overrideredirect(True)
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(),
                                height=self.root.winfo_screenheight(), bg='black')
        self.canvas.pack()
        self.steps = steps
        self.step = 0
        self.draw_step()
        self.root.bind("<Return>", self.next_step)
        # NO threading here! Tkinter must run in the main thread.
        self.root.mainloop()

    def draw_arrow(self, x, y, text):
        self.canvas.delete("all")
        self.canvas.create_line(x, y, x+100, y-100, arrow=tk.LAST, width=8, fill='yellow')

        # Place text according to step
        if self.step == 0:
            # First arrow: text left of arrow
            self.canvas.create_text(x-30, y-30, text=text, fill='white', font=('Arial', 24, 'bold'), anchor='ne')
        elif self.step == 1:
            # Second arrow: text right of arrow
            self.canvas.create_text(x+130, y-30, text=text, fill='white', font=('Arial', 24, 'bold'), anchor='nw')
        elif self.step == 2:
            # Third arrow: text below arrow
            self.canvas.create_text(x+50, y+40, text=text, fill='white', font=('Arial', 24, 'bold'), anchor='n')

    def draw_step(self):
        if self.step < len(self.steps):
            x, y, text = self.steps[self.step]
            self.draw_arrow(x, y, text)
        else:
            self.canvas.delete("all")
            self.canvas.create_text(self.root.winfo_screenwidth()//2,
                                   self.root.winfo_screenheight()//2,
                                   text="Done!", fill='lime', font=('Arial', 48, 'bold'), anchor='center')
            self.root.after(2000, self.root.destroy)

    def next_step(self, event=None):
        self.step += 1
        self.draw_step()
