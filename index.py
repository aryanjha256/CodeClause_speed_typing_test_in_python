import tkinter as tk
import time
import random
import threading


class TypeSpeedGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Type Speed Test")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.texts = open("texts.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root, bg="cyan")

        self.sample_label = tk.Label(self.frame, text=random.choice(
            self.texts), font=("Arial", 18), bg="black", fg="white")
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=(
            "Arial", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(
            self.frame, text="Speed: 0 WPM", font=("Arial", 14), bg="black", fg="white")
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", font=(
            "Arial", 14), bg="yellow", fg="black", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                threading.Thread(target=self.time_thread).start()

        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cpm = (len(self.input_entry.get()) / self.counter) * 60
            wpm = cpm / 5
            self.speed_label.config(
                text=f"Speed: {cpm} CPM" if cpm < 100 else f"Speed: {wpm} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.input_entry.delete(0, tk.END)
        # self.input_entry.config(fg="black")
        self.speed_label.config(text="Speed: 0 WPM")
        self.sample_label.config(text=random.choice(self.texts))


TypeSpeedGUI()
