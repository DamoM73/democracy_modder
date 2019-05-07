''' this program allows users to create their own country for Democracy 3 '''
import tkinter as tk

WIDTH = 1200
HEIGHT = 800

# **** Create main window ****
root = tk.Tk()
#root.geometry("1200x800")
root.title("Democracy 3 Country Generator")
root.config(bg="white")


# **** Add content to window ****

# header frame
header_fr = tk.Frame(root, bg="white", width=WIDTH).pack(fill=tk.X) 
logo = tk.PhotoImage(file="logo_small.png")
tk.Label(header_fr, image= logo, bg="white").pack(side=tk.LEFT)
tk.Label(header_fr, text="Country Generator ", font=("Arial", 25), bg="white").pack(side=tk.RIGHT)


# **** run window loop ****
root.mainloop()