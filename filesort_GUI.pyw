from os import listdir, mkdir
from os.path import isdir, isfile, join, exists
from shutil import move
from tkinter import *
from tkinter import ttk, messagebox


def filesort():
    if messagebox.askyesno(message=f"Are you sure you want to sort all the files in {path.get()}?",
                           icon="question", title="File Sorter"):
        parent_dir = str(path.get())
        move_mode = int(mode.get())
        if isdir(parent_dir):
            files = (f for f in listdir(parent_dir) if isfile(join(parent_dir, f)))
            for file in files:
                target_dir = join(parent_dir, file.split(".")[move_mode - 1])
                if not exists(target_dir):
                    mkdir(target_dir)
                move(join(parent_dir, file), target_dir)
            messagebox.showinfo("File Sorter", "Operation Complete!")
        else:
            messagebox.showerror("Error!", "Parent directory does not exist!")
    else:
        pass


root = Tk()
root.title("File Sorter")

# setting the window name and placement location:

w = 250  # width for the Tk root
h = 100  # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# creating the items in the window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

path = StringVar()
path_entry = ttk.Entry(mainframe, width=12, textvariable=path)
path_entry.grid(column=2, row=1, sticky=(W, E))

mode = StringVar()
ttk.Radiobutton(mainframe, text="Sort by Name", variable=mode, value=1).grid(column=2, row=2, sticky=(W, E))
ttk.Radiobutton(mainframe, text="Sort by Format", variable=mode, value=2).grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Sort", command=filesort).grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="Parent Directory: ").grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

path_entry.focus()
root.bind("<Return>", filesort)

root.mainloop()
