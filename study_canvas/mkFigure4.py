# いちばんやさしいPython入門教室
# 一定時間ごとに関数を実行する
# coding:utf-8

import tkinter as tk

# 円の座標
x = 400
y = 300

def move():
    global x, y
    # 赤の円を消す
    canvas.create_oval(x - 30, y - 30, x + 20, y + 20, fill="white", width=0)
    # X座標を動かす
    x = x + 1
    # 次の位置に円を描く
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", width=0)
    # 再びタイマー
    root.after(10, move)

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# キャンバスを置く
canvas =tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

# タイマーを設定する
root.after(10, move)

root.mainloop()
