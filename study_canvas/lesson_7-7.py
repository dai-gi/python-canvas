# いちばんやさしいPython入門教室
# 円をディクショナリとリストで管理する
# coding:utf-8

import tkinter as tk

# 円をコレクション(リストとディクショナリ)で管理
balls = [
    {"x" : 400, "y" : 300, "dx" : 3, "dy" : 3, "color":"red"},
    {"x" : 200, "y" : 100, "dx" : -3, "dy" : 3, "color":"green"},
    {"x" : 300, "y" : 400, "dx" : +3, "dy" : 3, "color":"black"},
    {"x" : 100, "y" : 200, "dx" : 3, "dy" : -3, "color": "blue"}
]

def move():
    global balls
    for b in balls:
        canvas.create_oval(b["x"] - 20.9, b["y"] - 20.9, b["x"] + 20.9, b["y"] + 20.9, fill="white",width=0)
        # Xの座標を動かす
        b["x"] = b["x"] + b["dx"]
        # Yの座標も動かす
        b["y"] = b["y"] + b["dy"]
        # 円の位置
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill=b["color"],width=0)
        
        # 端を超えていたら反対向きにする
        # x座標
        if b["x"] >= canvas.winfo_width():
            b["dx"] = -1
        if b["x"]  <= 0:
            b["dx"] = +1
        # y座標
        if b["y"] >= canvas.winfo_height():
            b["dy"] = -1
        if b["y"] <= 0:
            b["dy"] = +1

    root.after(10, move)

root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root,width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

root.after(10, move)

root.mainloop()