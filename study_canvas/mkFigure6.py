# いちばんやさしいPython入門教室
# 斜めに動かす
# codng:utf-8

import tkinter as tk

x = 400
y = 300
dx = 5
dy = 5

def move():
    global x, y, dx, dy
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="white", width=0)
    x = x + dx
    y = y + dy
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", width=0)
    if x >= canvas.winfo_width():
        dx = -5
    if x <= 0:
        dx = +5
    
    # Y座標
    if y >= canvas.winfo_height():
        dy = -5
    if y <= 0:
        dy = +5
    root.after(10, move)

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width ="600", height ="400", bg="white")
canvas.place(x = 0, y = 0)

root.after(10, move)

root.mainloop()
