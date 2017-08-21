# Development

## Setting up the editor skeleton

Our first goal is to implement the broad visual elements of the text 
editor. As programmers, we have all used text editors to edit code. We 
are mostly aware of the common GUI elements of a text editor.

The first phase implements the widgets:

* Menu
* Menubutton
* Label
* Button
* Text
* Scrollbar

We will use the `pack()` geometry manager to place all the widgets. We 
have chosen the `pack` manager because it is ideally suited for the 
placing of widgets side by side or in a top-down position. Fortunately, 
in a text editor, we have all the widgets placed either side-by-side or 
in top-down locations. Thus, it is beneficial to use the `pack` manager. 
We can do the same thing with the `grid` manager as well.

Let's start by adding the **Toplevel** window by using the following 
code:

```python
#!/usr/bin/env python3
from tkinter import *
root = Tk()
# all our code goes here
root.mainloop()
```

Also, add a constant and a couple of methods for that window:

```python
...
PROGRAM_NAME = "Texty"    # application's name
...
root.geometry('350x350')    # root size
root.title(PROGRAM_NAME)    # root title
...
```

The application's source code is:

```python
#!/usr/bin/env python3
from tkinter import *

PROGRAM_NAME = "Texty"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

root.mainloop()
```

![texty-img](screenshots/texty-01.png)

Also, type `$ git checkout 1b` to perform a checkout of this version.
