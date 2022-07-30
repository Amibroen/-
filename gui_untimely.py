from tkinter import *
import tkinter.messagebox
from threading import Timer
import random

import pandas as pd
import numpy as np
import turtle
import time
from PIL import Image, ImageTk


def Start():
    root2 = Tk()  # 创建窗口对象
    root2.geometry("50x40+650+275")
    root2.title("声源定位跟踪系统")  # 设置窗口标题
    Label(root2,text="开始定位！").grid()
    root2.mainloop()

def pen_back():
    turtle.tracer(False)
    turtle.penup()
    turtle.home()
    turtle.goto(-100, 0)
    turtle.left(90)
    turtle.pendown()

def draw(i):
    turtle.screensize(800, 600)
    turtle.speed(10)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(-100, 150)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(150, 150)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(300)
    pen_back()
    turtle.goto(x[i], y[i])
    pen_back()

    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="finall{}.eps".format(i))


def dynamic_fill(i):
    ddata = pd.read_csv('dynamic.csv', usecols=['x', 'y'])
    ddata = np.array(ddata)
    dx = [row[0] for row in data]
    dy = [row[1] for row in data]
    turtle.screensize(800, 600)
    turtle.speed(10)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(-100, 150)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(150, 150)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(300)
    pen_back()
    turtle.pencolor(100, 100, 100)
    turtle.goto(x[i], y[i])
    pen_back()

    dts = turtle.getscreen()
    dts.getcanvas().postscript(file="dfinall.eps")

def pos_find(i):
    vector1 = np.array([0, 0])
    vector2 = np.array([x[i], y[i]])
    distance = np.linalg.norm(vector1 - vector2)
    angle = 1.03741

    sites = ['AB距离：                         {:.5}'.format(distance),
             '角度：                             {:.5}'.format(angle),
             'X:                                  {:.5}'.format(x[i]),
             'Y:                                  {:.5}'.format(y[i])]
    for j in range(4):
        l = Label(root,text=sites[j])
        l.place(x=100, y=30 + j * 80, width=360, height=50)


def pos_find(i):
    vector1 = np.array([0, 0])
    vector2 = np.array([x[i], y[i]])
    distance = np.linalg.norm(vector1 - vector2)
    angle = 1.03741

    sites = ['AB距离：                         {:.5}'.format(distance),
             '角度：                             {:.5}'.format(angle),
             'X:                                  {:.5}'.format(x[i]),
             'Y:                                  {:.5}'.format(y[i])]
    for j in range(4):
        l = Label(root,text=sites[j])
        l.place(x=100, y=30 + j * 80, width=360, height=50)

data = pd.read_csv('sites.csv', usecols=['x', 'y'])
data = np.array(data)
x = [row[0] for row in data]
y = [row[1] for row in data]

root = Tk() # 创建窗口对象
root.geometry("1980x1020+0+0")
root.title("声源定位跟踪系统")   # 设置窗口标题
# 初始化
im = Image.open("bg.png").resize((1980,1020))
im = ImageTk.PhotoImage(im)
canvas = Canvas(root,width=1980,height=1020)
canvas.create_image(1980, 1020)
canvas.place(x=0,y=0,width=1980,height=1020)

sites = ['AB距离：                         {:.5}'.format(0.0000),
         '角度：                             {:.5}'.format(0.0000),
         'X:                                  {:.5}'.format(0.0000),
         'Y:                                  {:.5}'.format(0.0000)]
for j in range(4):
    l = Label(root,text=sites[j])
    l.place(x=100, y=30 + j * 80, width=360, height=50)
Button(root, text="声源定位",command=lambda:Start()).place(x=100, y=400, width=360, height=100)
Button(root, text="声源1查找",command=lambda:[draw(0),pos_find(0)]).place(x=900, y=100, width=360, height=100)
Button(root, text="声源2查找",command=lambda:[draw(1),pos_find(1)]).place(x=900, y=250, width=360, height=100)
Button(root, text="声源3查找",command=lambda:[draw(2),pos_find(2)]).place(x=900, y=400, width=360, height=100)
Button(root, text="声源4查找",command=lambda:[draw(3),pos_find(3)]).place(x=900, y=550, width=360, height=100)
Button(root, text="动态追踪",command=lambda:dynamic_fill(i=-1)).place(x=100, y=550, width=360, height=100)


root.mainloop()
