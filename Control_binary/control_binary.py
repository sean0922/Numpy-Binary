import tkinter as tk
import cv2
import os
import numpy as np
from PIL import ImageTk,Image
window = tk.Tk()
window.title('my window')
window.geometry('650x650')

l = tk.Label(window, bg='yellow', width=20, text='0')
l.pack()
l2 = tk.Label(window)
l2.pack()
lable=tk.Label(window,text="value",fg='Blue')
lable.place(x=100,y=100)



var = tk.StringVar()
def print_selection():
    print(var.get())

def print_selection(v):
    a=int(v)
    l2.configure(text=a, fg='BLUE')
    img = cv2.imread("1-111.bmp")
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grayImg = cv2.cvtColor(imgrgb, cv2.COLOR_RGB2GRAY)

    tmp=0
    if(var.get()=="A"):
        tmp=255
    else:
        tmp=0

    
    ret, thresh1 = cv2.threshold(grayImg, a, 255, cv2.THRESH_BINARY)
    grayImg1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB)
    images = thresh1
    iimm = Image.fromarray(images)
    image3 = ImageTk.PhotoImage(image=iimm)

    print(image3)
    lable.configure(image=image3)
    lable.image = image3

    def motion(event):
        x, y = event.x, event.y
        try:
            print(x,y)
            b, g, r = grayImg1[y ,x]  # 获取b, g, r
            print("像素点的bgr值", b, g, r)
            l.configure(text="像素点的bgr值" +str(b)+","+str(g)+","+str(r), fg='BLUE')
        except:
            print("error")

    window.bind('<Motion>', motion)

s = tk.Scale(window, label='try me', from_=0, to=255, orient=tk.HORIZONTAL,length=400, showvalue=0, tickinterval=51, resolution=1, command=print_selection)
s.pack()

window.mainloop()