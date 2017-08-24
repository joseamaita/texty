#!/usr/bin/env python3
from tkinter import *

PROGRAM_NAME = "Texty"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

new_file_icon = PhotoImage(file='files/new_file.gif')
open_file_icon = PhotoImage(file='files/open_file.gif')
save_file_icon = PhotoImage(file='files/save.gif')
cut_icon = PhotoImage(file='files/cut.gif')
copy_icon = PhotoImage(file='files/copy.gif')
paste_icon = PhotoImage(file='files/paste.gif')
undo_icon = PhotoImage(file='files/undo.gif')
redo_icon = PhotoImage(file='files/redo.gif')

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label = 'New', 
                      accelerator = 'Ctrl+N', 
                      compound = 'left', 
                      image = new_file_icon, 
                      underline = 0)
file_menu.add_command(label = 'Open', 
                      accelerator = 'Ctrl+O', 
                      compound = 'left', 
                      image = open_file_icon, 
                      underline = 0)
file_menu.add_command(label = 'Save', 
                      accelerator = 'Ctrl+S', 
                      compound = 'left', 
                      image = save_file_icon, 
                      underline = 0)
file_menu.add_command(label = 'Save as', 
                      accelerator = 'Shift+Ctrl+S')
file_menu.add_separator()
file_menu.add_command(label = 'Exit', 
                      accelerator = 'Alt+F4')

menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label = 'Undo', 
                      accelerator = 'Ctrl+Z', 
                      compound = 'left', 
                      image = undo_icon)
edit_menu.add_command(label = 'Redo', 
                      accelerator = 'Ctrl+Y', 
                      compound = 'left', 
                      image = redo_icon)
edit_menu.add_separator()
edit_menu.add_command(label = 'Cut', 
                      accelerator = 'Ctrl+X', 
                      compound = 'left', 
                      image = cut_icon)
edit_menu.add_command(label = 'Copy', 
                      accelerator = 'Ctrl+C', 
                      compound = 'left', 
                      image = copy_icon)
edit_menu.add_command(label = 'Paste', 
                      accelerator = 'Ctrl+V', 
                      compound = 'left', 
                      image = paste_icon)
edit_menu.add_separator()
edit_menu.add_command(label = 'Find', 
                      underline = 0, 
                      accelerator = 'Ctrl+F')
edit_menu.add_separator()
edit_menu.add_command(label = 'Select All', 
                      underline = 7, 
                      accelerator = 'Ctrl+A')

menu_bar.add_cascade(label='View', menu=view_menu)

menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About')
about_menu.add_command(label='Help')

root.config(menu=menu_bar)

root.mainloop()
