#!/usr/bin/env python

import tkinter as tk
from tkinter import *
import datetime
from pynput.keyboard import Key, Listener
from pynput import keyboard
import os

comb1 = [
    {keyboard.Key.ctrl_l, keyboard.Key.ctrl_r},
]
comb2 = [
    {keyboard.Key.shift_l, keyboard.Key.shift_r},
]
current = set()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Logger")
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        #self.datetimelabel = tk.Label(self)
        #self.datetimelabel["text"] = str(now.strftime("%d-%m-%y %H:%M"))
        #self.datetimelabel.pack(fill=X)
        self.label1 = tk.Label(self, text="Enter your log")
        self.label1.pack(fill=X)
        self.text = tk.Entry(self)
        self.text.pack(fill=X)
        self.text.focus_set()
        self.text.bind('<Return>', self.log)
        self.text.bind('<Escape>', self.exit)
        #self.button = tk.Button(text="Log", command=self.log)
        #self.button.pack(fill=X)
    
    def exit(self, event=' '):
        self
        
        
    
    def log(self, event=' '):
        content = str(now.strftime("%d-%m-%y %H:%M"))+" -->"+self.text.get() + "\n" +"-"*20 +"\n"
        main_file = open("/home/anuroop/logger.txt", "a")
        hidden_file = open("/home/anuroop/.logger", "a")
        main_file.write(str(content))
        hidden_file.write(str(content))
        main_file.close()
        hidden_file.close()
        self.master.destroy()

class Show_file(tk.Frame):
    def __init__(self, file_path, master=None):
        super().__init__(master)
        self.master = master
        self.master.title(file_path)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.label1 = tk.Label(self, text="Enter your log")
        f = open('/home/anuroop/logger.txt', 'r')
        self.label1["text"] = f.read() + "\n"*3+ "PRESS Esc to close."
        f.close()
        self.label1.pack(fill=X)
        self.label1.focus_set()
        self.label1.bind('<Escape>', self.log)        
    
    def log(self, event=' '):
        self.master.destroy()



now = datetime.datetime.now()
def on_press(key):
    global current
    if any([key in comb for comb in comb1]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in comb1):
            root = tk.Tk()
            app = Application(master=root)
            app.mainloop()
    #current = set()
    if any([key in comb for comb in comb2]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in comb2):
            #os.system("gedit ./logger.txt") 
            root = tk.Tk()
            app = Show_file("./logger.txt", root)
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