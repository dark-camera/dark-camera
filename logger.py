#!/usr/bin/env python

import tkinter as tk
from tkinter import *
import datetime
from pynput.keyboard import Key, Listener
from pynput import keyboard
import os
from pathlib import Path

comb1 = [
    {keyboard.Key.ctrl_l, keyboard.Key.ctrl_r},
]
comb2 = [
    {keyboard.Key.shift_l, keyboard.Key.shift_r},
]
current = set()
home = str(Path.home())
file_path = home + '/.logger'

class Application(tk.Frame):
    def __init__(self, file_path, master=None):
        super().__init__(master)
        self.file_path = file_path
        self.master = master
        self.master.title("Logger")
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter your log")
        self.label.pack(fill=X)
        self.text = tk.Entry(self)
        self.text.pack(fill=X)
        self.text.focus_set()
        self.text.bind('<Return>', self.log)
        self.text.bind('<Escape>', self.exit)
    
    def exit(self, event=' '):
        self.master.destroy()
        
    def log(self, event=' '):
        content = str(now.strftime("%d-%m-%y %H:%M"))+" -->"+self.text.get() + "\n" +"-"*20 +"\n"
        main_file = open(self.file_path, "a")
        main_file.write(str(content))
        main_file.close()
        self.master.destroy()

class Show_file(tk.Frame):
    def __init__(self, file_path, master=None):
        super().__init__(master)
        self.file_path = file_path
        self.master = master
        self.master.title(file_path)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self, text="Enter your log")
        f = open(self.file_path, 'r')
        self.label["text"] = f.read() + "\n"*3+ "PRESS Esc to close."
        f.close()
        self.label.pack(fill=X)
        self.label.focus_set()
        self.label.bind('<Escape>', self.log)        
    
    def log(self, event=' '):
        self.master.destroy()



now = datetime.datetime.now()
def on_press(key):
    global current
    global file_path
    if any([key in comb for comb in comb1]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in comb1):
            root = tk.Tk()
            app = Application(file_path, root)
            app.mainloop()
    #current = set()
    if any([key in comb for comb in comb2]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in comb2):
            #os.system("gedit ./logger.txt") 
            root = tk.Tk()
            app = Show_file(file_path, root)
            app.mainloop()
                
        
def on_release(key):
    global current
    current = set()
    #if key == Key.esc:
    #    return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

"""
If you want to make this a command in linux. Just do following:
* Add #!/usr/bin/env python to the first line of this script.
* Save the script with any name like "logger" in your path. Run command "echo $PATH" in terminal to know path locations.
* then run command "chmod +x logger" to make it executable.
I saved it to "/home/anuroop/.local/bin" with name logger.
Now i can run it from anywhere in linux. Just by typing logger in terminal.
You can also run it using command "nohup logger &" to run in background.
"""