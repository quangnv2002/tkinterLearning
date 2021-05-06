from tkinter import *
from tkinter.ttk import *   # to use Combobox
from tkinter import messagebox
import tkinter
import cv2
import PIL.Image # cài đặt pillow
import PIL.ImageTk
window = Tk()
window.title("Tkinter opencv")
window.geometry("800x600")

video = cv2.VideoCapture(0)
# ret,frame = video.read()
# cv2.imshow("window",frame)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)//2
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2
canvas = Canvas(window, width=canvas_w,height=canvas_h,bg="red")
canvas.grid(column=2,row=0)

canvas.pack(side=LEFT)# Lệnh pack để vứt vào window




bw = 0
def handleBW():
    global bw
    bw = 1-bw

btn = Button(window,text="black and white",command=handleBW)
btn.pack()

photo = None

def updateFrame():
    global canvas, photo, bw
    # Đọc từ Camera
    ret, frame = video.read()
    # Resize
    frame = cv2.resize(frame, dsize=None, fx=0.5,fy=0.5)
    # Chuyển hệ màu
    if bw==0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, )
    # Convert thành ImageTk
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show lên
    canvas.create_image(0,0, image = photo,anchor = tkinter.NW)
    window.after(15,updateFrame)
updateFrame()
window.mainloop()