# いちばんやさしいPython入門教室
# キャンバスの端に当たったら、移動量を反転する
# coding:utf-8

import tkinter as tk

# 円の座標と半径
x = 400
y = 300
# 移動量
dx = 1

def move():
    global x, y, dx
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="white", width=0)
    x = x + dx
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", width=0)
    # 端を超えていたら反対向きにする
    if x >= canvas.winfo_width():
        dx = -2
    if x <= 0:
        dx = +1
    root.after(10, move)

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

root.after(10, move)

root.mainloop()