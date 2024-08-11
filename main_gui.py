# gui for better user experience

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import logic
from pathlib import Path
from functools import partial
import multiprocessing


# creating main window
class MainWindow(Tk):
    def __init__(self):

        # main window setup
        super().__init__()
        self.geometry('600x230')
        self.title("BetterDownloads")
        self.rowconfigure(0, minsize=50)
        self.resizable(width=False, height=False)

        self.menu = Menu()
        self.file_menu = Menu(tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.destroy)
        self.help_menu = Menu(tearoff=0)
        self.help_menu.add_command(label="About", command=self.about_click)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        self.config(menu=self.menu)

        self.frame1 = Frame(self)
        self.frame1.pack(anchor=W, ipady=10)

        self.frame2 = Frame(self)
        self.frame2.pack(anchor=W, pady=5)

        self.frame3 = Frame(self)
        self.frame3.pack(anchor=W, pady=5)

        self.frame4 = Frame(self)
        self.frame4.pack(fill=X, padx=10)

        # widgets
        self.label = Label(self.frame1, text="BetterDownloads alpha", font=("Arial black", 20))
        self.label.pack(anchor=W)

        self.desc = Label(self.frame1, text="An app that provides an easy way to move, copy and sort files from preferred folder.", font=("Arial black", 8), foreground="gray")
        self.desc.pack(anchor=W)

        self.label1 = Label(self.frame2, text="Start folder:")
        self.label1.pack(side=LEFT)

        self.path = str(Path.home() / "Downloads")
        self.sublabel1 = Label(self.frame2, text=self.path)
        self.sublabel1.pack(ipadx=10, side=LEFT)

        self.button1 = Button(self.frame2, text="Browse...", command=self.select_start_folder)
        self.button1.pack(ipadx=20, side=LEFT)

        self.label2 = Label(self.frame3, text="Destination folder:")
        self.label2.pack(side=LEFT)

        self.new_path = str(Path.home() / "BetterDownloads")
        self.sublabel2 = Label(self.frame3, text=self.new_path, fg="grey")
        self.sublabel2.pack(ipadx=10, side=LEFT)

        self.button2 = Button(self.frame3, text="Browse...", command=self.select_end_folder, state="disabled")
        self.button2.pack(ipadx=20, side=LEFT)

        self.flag = IntVar()
        self.c1 = Checkbutton(self.frame4, text="automatically create new path", command=self.enable_browse, variable=self.flag, onvalue=1, offvalue=0)
        self.c1.pack(side=LEFT)
        self.c1.select()

        self.button = Button(self.frame4, text="Copy", width=20, height=2, bg="gray", command=partial(self.cleanup, True))
        self.button.pack(side=RIGHT)

        self.button = Button(self.frame4, text="Move", width=20, height=2, bg="gray", command=partial(self.cleanup, False))
        self.button.pack(side=RIGHT)

    # functions

    def about_click(self):
        messagebox.showinfo("About", "This app moves/copies all files from one directory and sorts them to the other by extentions (e.g. documents, videos, applications..)")

    def select_start_folder(self):
        self.path = filedialog.askdirectory(initialdir="C:\\")
        self.sublabel1["text"] = self.path

    def select_end_folder(self):
        self.new_path = filedialog.askdirectory(initialdir="C:\\")
        self.sublabel2["text"] = self.new_path

    def cleanup(self, func):
        self.popup()
        result = multiprocessing.Queue()
        self.p1 = multiprocessing.Process(target=logic.cleanup_folder, args=[self.path, self.new_path, func, result])
        self.p1.start()
        while self.p1.is_alive():
            continue
        self.subwindow.l1["text"] = "Copying is complete!"
        self.subwindow.r1["mode"] = "determinate"
        self.subwindow.r1.stop()
        self.subwindow.r1["value"] = 100
        self.subwindow.mainloop()
        print(result.get)

    def enable_browse(self):
        if self.flag.get() == 0:
            self.sublabel2["fg"] = "black"
            self.button2["state"] = "normal"
        else:
            self.sublabel2["fg"] = "grey"
            global new_path
            new_path = str(Path.home() / "BetterDownloads")
            self.sublabel2["text"] = new_path
            self.button2["state"] = "disabled"

    def popup(self):
        self.subwindow = SubWindow()


class SubWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cleanup in process...")
        self.geometry("300x100")
        self.resizable(width=False, height=False)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.focus()
        self.grab_set()

        self.l1 = Label(master=self, text="Please wait, copying in progress...")
        self.l1.pack()

        self.r1 = ttk.Progressbar(master=self, length=150, mode="indeterminate")
        self.r1.pack(pady=5)
        self.r1.start()

        self.b1 = Button(master=self, text="Ok", command=main.destroy)
        self.b1.pack(anchor="center")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main = MainWindow()
    main.mainloop()
