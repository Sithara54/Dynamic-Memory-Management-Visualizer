# Dynamic Memory Management Visualizer
# Page Replacement Algorithms: FIFO and LRU

import tkinter as tk
from tkinter import messagebox

class MemoryVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Memory Management Visualizer")
        self.frames = []
        self.page_faults = 0

        tk.Label(root, text="Number of Frames").grid(row=0, column=0)
        tk.Label(root, text="Page Reference String").grid(row=1, column=0)
        tk.Label(root, text="Algorithm").grid(row=2, column=0)

        self.frames_entry = tk.Entry(root)
        self.frames_entry.grid(row=0, column=1)

        self.pages_entry = tk.Entry(root)
        self.pages_entry.grid(row=1, column=1)

        self.algo = tk.StringVar()
        self.algo.set("FIFO")

        tk.Radiobutton(root, text="FIFO", variable=self.algo, value="FIFO").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(root, text="LRU", variable=self.algo, value="LRU").grid(row=3, column=1, sticky="w")

        tk.Button(root, text="Simulate", command=self.simulate).grid(row=4, column=1)

        self.output = tk.Text(root, height=15, width=50)
        self.output.grid(row=5, column=0, columnspan=2)

    def simulate(self):
        self.output.delete("1.0", tk.END)
        self.frames = []
        self.page_faults = 0

        try:
            capacity = int(self.frames_entry.get())
            pages = list(map(int, self.pages_entry.get().split()))
        except:
            messagebox.showerror("Error", "Invalid Input")
            return

        if self.algo.get() == "FIFO":
            self.fifo(pages, capacity)
        else:
            self.lru(pages, capacity)

        self.output.insert(tk.END, f"\nTotal Page Faults = {self.page_faults}")

    def fifo(self, pages, capacity):
        index = 0
        for page in pages:
            if page not in self.frames:
                if len(self.frames) < capacity:
                    self.frames.append(page)
                else:
                    self.frames[index] = page
                    index = (index + 1) % capacity
                self.page_faults += 1
                fault = "Yes"
            else:
                fault = "No"

            self.output.insert(tk.END, f"Page {page} → Frames {self.frames} → Fault: {fault}\n")

    def lru(self, pages, capacity):
        recent = {}
        time = 0

        for page in pages:
            time += 1
            if page not in self.frames:
                if len(self.frames) < capacity:
                    self.frames.append(page)
                else:
                    lru_page = min(recent, key=recent.get)
                    self.frames[self.frames.index(lru_page)] = page
                    del recent[lru_page]
                self.page_faults += 1
                fault = "Yes"
            else:
                fault = "No"

            recent[page] = time
            self.output.insert(tk.END, f"Page {page} → Frames {self.frames} → Fault: {fault}\n")

root = tk.Tk()
app = MemoryVisualizer(root)
root.mainloop()

