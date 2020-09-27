from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set)
mylist.configure(state=NORMAL)
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))
mylist.bind("<1>", lambda event: mylist.focus_set())
mylist.configure(state=DISABLED)

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()