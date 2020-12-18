# いちばんやさしいPython入門教室
# クリックされたされたところに描画する
# coding:utf-8

import tkinter as tk 

def click(event):
    # クリックされたときにそこに描画する
    canvas.create_oval(event.x -20, event.y - 20, event.x + 20, event.y + 20, fill="red", width=0)

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# キャンバスを置く
canvas =tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

"""
bindメソッド(第一引数)：
<Button-1> = Button <- マウス？が「クリック」されたという意
<Button-1> = 
「1」の場合 <- マウス？が「左クリック」されたという意
「2」の場合 <- マウス？が「右クリック」されたという意
「3」の場合 <- マウス？が「中央クリック」されたという意

bindメソッド(第二引数)：
定義したclick関数を呼び出す
"""
canvas.bind("<Button-1>",click)

root.mainloop()