import tkinter as tk
from tkinter import messagebox

class MemoryManagementVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Memory Management Visualizer")

        tk.Label(root, text="Number of Frames").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Page Reference String").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Page Replacement Algorithm").grid(row=2, column=0, padx=10, pady=5)

        self.frame_entry = tk.Entry(root)
        self.frame_entry.grid(row=0, column=1)

        self.page_entry = tk.Entry(root)
        self.page_entry.grid(row=1, column=1)

        self.algorithm = tk.StringVar(value="FIFO")
        tk.Radiobutton(root, text="FIFO", variable=self.algorithm, value="FIFO").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(root, text="LRU", variable=self.algorithm, value="LRU").grid(row=3, column=1, sticky="w")

        tk.Button(root, text="Simulate", command=self.simulate).grid(row=4, column=1, pady=10)

        self.output = tk.Text(root, height=18, width=55)
        self.output.grid(row=5, column=0, columnspan=2, padx=10)

    def simulate(self):
        self.output.delete("1.0", tk.END)

        try:
            frames_count = int(self.frame_entry.get())
            pages = list(map(int, self.page_entry.get().split()))
        except:
            messagebox.showerror("Input Error", "Please enter valid inputs")
            return

        if self.algorithm.get() == "FIFO":
            self.fifo(pages, frames_count)
        else:
            self.lru(pages, frames_count)

    def fifo(self, pages, capacity):
        frames = []
        index = 0
        page_faults = 0

        self.output.insert(tk.END, "FIFO Page Replacement\n\n")

        for page in pages:
            if page not in frames:
                if len(frames) < capacity:
                    frames.append(page)
                else:
                    frames[index] = page
                    index = (index + 1) % capacity
                page_faults += 1
                status = "Page Fault"
            else:
                status = "Page Hit"

            self.output.insert(tk.END, f"Page {page} → Frames: {frames} → {status}\n")

        self.output.insert(tk.END, f"\nTotal Page Faults = {page_faults}")

    def lru(self, pages, capacity):
        frames = []
        recent = {}
        time = 0
        page_faults = 0

        self.output.insert(tk.END, "LRU Page Replacement\n\n")

        for page in pages:
            time += 1
            if page not in frames:
                if len(frames) < capacity:
                    frames.append(page)
                else:
                    lru_page = min(recent, key=recent.get)
                    frames[frames.index(lru_page)] = page
                    del recent[lru_page]
                page_faults += 1
                status = "Page Fault"
            else:
                status = "Page Hit"

            recent[page] = time
            self.output.insert(tk.END, f"Page {page} → Frames: {frames} → {status}\n")

        self.output.insert(tk.END, f"\nTotal Page Faults = {page_faults}")


root = tk.Tk()
app = MemoryManagementVisualizer(root)
root.mainloop()
