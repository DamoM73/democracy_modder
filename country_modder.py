''' this program allows users to create their own country for Democracy 3 '''
import tkinter as tk

WIDTH = 1000
HEIGHT = 800

# **** Create main window ****
root = tk.Tk()
#root.geometry("1200x800")
root.title("Democracy 3 Country Generator")
root.config(bg="white")


# **** Add content to window ****

# header frame
header_fr = tk.Frame(root, bg="white", width=WIDTH).grid(row=0, column=0) 
logo = tk.PhotoImage(file="logo_small.png")
tk.Label(header_fr, image= logo, bg="white").grid(row=0, column=0, sticky=tk.W)
tk.Label(header_fr, text="Country Generator ", font=("Arial", 22), justify=tk.RIGHT, bg="white")\
    .grid(row=0, column=1, sticky=tk.E)

# country details frame
country_fr = tk.LabelFrame(root, text="Country Details", font=("Arial",16), bg="white")
country_fr.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
tk.Label(country_fr,text="Name", bg="white", font=("Arial",12)).grid(row=0, column=0)
name_ent = tk.Entry(country_fr, width=30)
name_ent.grid(row=0, column=1)


# **** run window loop ****
root.mainloop()