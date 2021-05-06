from tkinter import *
from tkinter.ttk import *   # to use Combobox
from tkinter import messagebox
import tkinter

window = Tk()
window.title("Mi AI Form")
window.geometry("800x600")

# Thêm label
lbl = tkinter.Label(window,text="Hello My AI", fg = "blue", font =("Arial",50))
lbl.grid(column =0, row=0 )

# Thêm textbox
txt = Entry(window,width = 50)
txt.grid(column=0,row=1)


def handleButton():
    #lbl.configure(text = "HI "  + txt.get())
    messagebox.showinfo("hello boss")
    return
# Thêm button
btnHello = Button(window,text="Say hello", command=handleButton)
btnHello.grid(column=0,row=2)

# Thêm combobox
combo = Combobox(window)
combo['value'] = ("num1","num2")
combo.grid(column=0,row=3)
combo.current(0)    # khi form load lên thì phần tử đầu tiên được chọn
window.mainloop()