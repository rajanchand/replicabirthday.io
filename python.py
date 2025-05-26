import tkinter as tk
from tkinter import messagebox
import time

class MemoryDeletionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Deletion")
        self.root.geometry("400x500")
        
        # Main frame
        self.main_frame = tk.Frame(root, bg='black')
        self.main_frame.pack(expand=True, fill='both')
        
        # Memory image (represented by a simple figure)
        self.canvas = tk.Canvas(self.main_frame, width=400, height=400, bg='black')
        self.canvas.pack(pady=20)
        
        # Create memory figure
        self.memory_figure = self.canvas.create_oval(150, 100, 250, 200, fill='pink')
        self.canvas.create_line(200, 200, 200, 300, fill='pink', width=2)
        self.canvas.create_line(200, 250, 150, 200, fill='pink', width=2)
        self.canvas.create_line(200, 250, 250, 200, fill='pink', width=2)
        self.canvas.create_line(200, 300, 150, 350, fill='pink', width=2)
        self.canvas.create_line(200, 300, 250, 350, fill='pink', width=2)
        
        # Question label
        self.question_label = tk.Label(
            self.main_frame,
            text="Do you want to delete all memories?",
            bg='black',
            fg='white',
            font=('Arial', 12)
        )
        self.question_label.pack(pady=10)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.main_frame, bg='black')
        self.button_frame.pack(pady=10)
        
        # Yes and No buttons
        self.yes_button = tk.Button(
            self.button_frame,
            text="Yes",
            command=self.delete_memory,
            bg='red',
            fg='white',
            width=10
        )
        self.yes_button.pack(side=tk.LEFT, padx=10)
        
        self.no_button = tk.Button(
            self.button_frame,
            text="No",
            command=self.no_choice,
            bg='green',
            fg='white',
            width=10
        )
        self.no_button.pack(side=tk.LEFT, padx=10)
        
        self.no_count = 0
        
    def delete_memory(self):
        # Animation for disappearing
        for i in range(100):
            self.canvas.update()
            self.canvas.delete('all')
            size = 100 - i
            if size > 0:
                x1 = 200 - size
                y1 = 200 - size
                x2 = 200 + size
                y2 = 200 + size
                self.canvas.create_oval(x1, y1, x2, y2, fill='pink')
            time.sleep(0.02)
            
        messagebox.showinfo("Deleted", "All memories have been deleted...")
        self.root.quit()
        
    def no_choice(self):
        self.no_count += 1
        if self.no_count == 1:
            messagebox.showwarning("Warning", "Please choose clearly. Are you sure?")
        else:
            messagebox.showinfo("Message", "Maybe not in this life... In the next life, she will surely be yours.")
            self.root.quit()

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryDeletionApp(root)
    root.mainloop()
