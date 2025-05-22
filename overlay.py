import tkinter as tk
import threading

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
        threading.Thread(target=self.root.mainloop, daemon=True).start()

    def draw_arrow(self, x, y, text):
        self.canvas.delete("all")
        self.canvas.create_line(x, y, x+100, y-100, arrow=tk.LAST, width=8, fill='yellow')
        self.canvas.create_text(x+120, y-120, text=text, fill='white', font=('Arial', 24, 'bold'), anchor='nw')

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
