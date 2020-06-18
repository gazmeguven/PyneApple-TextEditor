import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, simpledialog


class TextEditor:

  def __init__(self, root):   # Constructor Part
    self.root = root
    self.root.title("PyneApple Text")
    self.root.geometry("800x600+200+150")
    self.root.iconphoto(False, tk.PhotoImage(file='/Users/Gamze/Desktop/pyne.png'))
    self.filename = None
    self.title = StringVar()
    self.status = StringVar()

    self.titlebar = Label(self.root, textvariable=self.title, font=("times new roman", 12),
                          bg="SeaGreen2", bd=2, relief=RIDGE)                             # Creating Title bar
    self.titlebar.pack(side=TOP, fill=BOTH)
    self.title.set("Enjoy Coding!")

    self.statusbar = Label(self.root, textvariable=self.status, font=("times new roman", 9),
                           fg="black", bg="ivory3", bd=2, anchor="sw", relief=RIDGE)       # Creating Status bar
    self.statusbar.pack(side=BOTTOM, fill=BOTH)
    self.status.set("PyneApple Text Editor Version 1.0")                                   # Initializing Status

    self.menubar = Menu(self.root, font=("times new roman", 9), activebackground="DarkSeaGreen1")   # Creating Menubar
    self.root.config(menu=self.menubar)         # Configuring menubar on root window

    self.filemenu = Menu(self.menubar, font=("times new roman", 9,), activebackground="DarkSeaGreen3", tearoff=0)    # Creating File Menu
    self.filemenu.add_command(label="New", accelerator="Ctrl+N", command=self.newfile)
    self.filemenu.add_command(label="Open", accelerator="Ctrl+O", command=self.openfile)
    self.filemenu.add_command(label="Save", accelerator="Ctrl+S", command=self.savefile)
    self.filemenu.add_command(label="Save As", accelerator="Ctrl+A", command=self.saveasfile)
    self.filemenu.add_separator()                   # Adding Separator
    self.filemenu.add_command(label="Exit", accelerator="Ctrl+E", command=self.exit)
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    self.editmenu = Menu(self.menubar, font=("times new roman", 9), activebackground="DarkSeaGreen3", tearoff=0)   # Creating Edit Menu
    self.editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)
    self.editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)
    self.editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)
    self.editmenu.add_separator()
    self.editmenu.add_command(label="Undo", accelerator="Ctrl+U", command=self.undo)
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    self.searchmenu = Menu(self.menubar, font=("times new roman", 9), activebackground="DarkSeaGreen3", tearoff=0)  # Creating Find Menu
    self.searchmenu.add_command(label="Find", accelerator="Ctrl+F", command=self.find)
    self.menubar.add_cascade(label="Find", menu=self.searchmenu)

    self.helpmenu = Menu(self.menubar, font=("times new roman", 9), activebackground="DarkSeaGreen3", tearoff=0)   # Creating About Menu
    self.helpmenu.add_command(label="About", command=self.infoabout)
    self.menubar.add_cascade(label="About", menu=self.helpmenu)

    scrol_y = Scrollbar(self.root, orient=VERTICAL, width=14, highlightcolor="peach puff")      # Creating Scrollbar
    self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=("Calibri", 14), state="normal", relief=RIDGE)  # Creating Text Area
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=self.txtarea.yview)
    self.txtarea.pack(fill=BOTH, expand=1)
    self.shortcuts()                           # Calling shortcuts function

  # Defining Set Title Function
  def settitle(self):
    if self.filename:
      self.title.set(self.filename)
    else:
      self.title.set("Untitled")

  # Defining New file Function
  def newfile(self, *args):
    self.txtarea.delete("1.0", END)
    self.filename = None
    self.settitle()
    self.status.set("New File Created")

  # Defining Open File Function
  def openfile(self, *args):
    # Exception handling
    try:
      self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("All Files", "*.*"),
                                                                                 ("Text Files", "*.txt"),
                                                                                 ("Python Files", "*.py"),
                                                                                 ("Markdown Documents", "*.md"),
                                                                                 ("Javascript Files", ".*js"),
                                                                                 ("HTML Documents", ".*html"),
                                                                                 ("CSS Documents", "*.css")))
      if self.filename:
        infile = open(self.filename, "r")
        self.txtarea.delete("1.0", END)
        for line in infile:
          self.txtarea.insert(END, line)
        infile.close()
        self.settitle()
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception", e, icon='error')

  # Defining Save File Function
  def savefile(self, *args):
    # Exception handling
    try:
      if self.filename:
        data = self.txtarea.get("1.0", END)
        outfile = open(self.filename, "w")
        outfile.write(data)
        outfile.close()
        self.settitle()
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception", e, icon='error')

  # Defining Save As File Function
  def saveasfile(self, *args):
    try:
      untitledfile = filedialog.asksaveasfilename(title="Save file As", defaultextension=".txt",
                                                  initialfile="Untitled.txt",
                                                  filetypes=(("All Files","*.*"),
                                                             ("Text Files","*.txt"),
                                                             ("Python Files","*.py"),
                                                             ("Markdown Documents", "*.md"),
                                                             ("Javascript Files", ".*js"),
                                                             ("HTML Documents", ".*html"),
                                                             ("CSS Documents", "*.css")))
      data = self.txtarea.get("1.0", END)
      outfile = open(untitledfile, "w")
      outfile.write(data)
      outfile.close()
      self.filename = untitledfile
      self.settitle()
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception", e, icon='error')

  # Defining Exit Window Function
  def exit(self, *args):
    op = messagebox.askyesno("Warning", "Your Unsaved Data May Be Lost!", icon='warning')

    if op > 0:
      self.root.destroy()
    else:
      return

  # Defining Cut Function
  def cut(self, *args):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy Function
  def copy(self, *args):
    self.txtarea.event_generate("<<Copy>>")

  # Defining Paste Function
  def paste(self, *args):
    self.txtarea.event_generate("<<Paste>>")

  # Defining Undo Function
  def undo(self, *args):
    try:
      if self.filename:
        self.txtarea.delete("1.0", END)
        infile = open(self.filename, "r")
        for line in infile:
          self.txtarea.insert(END, line)
        infile.close()
        self.settitle()
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0", END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception", e, icon='error')

  #Defining Find Function
  def find(self, *args):
      findString = simpledialog.askstring("Find...", "Enter text")
      textData = self.txtarea.get("1.0", END)

      occurances = textData.upper().count(findString.upper())

      if textData.upper().count(findString.upper()) > 0:
        messagebox.showinfo("Results", findString + " has multiple occurances, " + str(occurances), icon='info')

      else:
        messagebox.showinfo("Warning", "No Result", icon='warning')

      print(textData.upper().count(findString.upper()))

  # Defining About Function
  def infoabout(self):
    messagebox.showinfo("About Text Editor", "PyneApple Text Editor\nCreated Using Python\nBy Gamze Guven "
                                             "\n2020", icon='info')

  # Defining Shortcuts Function
  def shortcuts(self):
    self.txtarea.bind("<Control-n>", self.newfile)
    self.txtarea.bind("<Control-o>", self.openfile)
    self.txtarea.bind("<Control-s>", self.savefile)
    self.txtarea.bind("<Control-a>", self.saveasfile)
    self.txtarea.bind("<Control-e>", self.exit)
    self.txtarea.bind("<Control-x>", self.cut)
    self.txtarea.bind("<Control-c>", self.copy)
    self.txtarea.bind("<Control-v>", self.paste)
    self.txtarea.bind("<Control-u>", self.undo)
    self.txtarea.bind("<Control-f>", self.find)


root = Tk()
TextEditor(root)
root.mainloop()