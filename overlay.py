import tkinter as tk

class OverlayMessage:
    def __init__(self, messages):
        self.root = tk.Tk()
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.85)
        self.root.overrideredirect(True)
        self.root.configure(bg='black')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height, bg='black', highlightthickness=0)
        self.canvas.pack()
        self.messages = messages
        self.step = 0
        self.show_message()
        self.root.bind("<Return>", self.next_message)
        self.root.bind("<Button-1>", self.next_message)  # Also allow mouse click
        self.root.mainloop()

    def show_message(self):
        self.canvas.delete("all")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        text = self.messages[self.step]
        self.canvas.create_text(
            screen_width // 2, screen_height // 2,
            text=text,
            fill='white',
            font=('Arial', 32, 'bold'),
            anchor='center',
            justify='center'
        )
        self.canvas.create_text(
            screen_width // 2, screen_height // 2 + 120,
            text="Press Enter or click to continue...",
            fill='yellow',
            font=('Arial', 20, 'italic'),
            anchor='center'
        )

    def next_message(self, event=None):
        self.step += 1
        if self.step < len(self.messages):
            self.show_message()
        else:
            self.root.destroy()
