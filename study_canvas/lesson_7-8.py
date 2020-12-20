# class・self
# coding:utf-8
import tkinter as tk

class Ball:

    # アトリビュートの初期化
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    # メソッド
    def move(self, canvas):
        # いまの円を消す
        canvas.create_oval(self.x -25, self.y -25, self.x +25, self.y +25, fill="white", width=0)
        # X座標、Y座標を動かす
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # 次の位置に円を描画する
        canvas.create_oval(self.x -20, self.y -20, self.x +20, self.y +20, fill=self.color, width=0)
        # 端を超えていたら反対向きにする
        if self.x >= canvas.winfo_width():
            self.dx = -0.5
        if self.x <= 0:
            self.dx = 0.5
        if self.y >= canvas.winfo_height():
            self.dy = -0.5
        if self.y <= 0:
            self.dy = 0.5        

# 円をインスタンス化
balls = [
    Ball(400, 300, 1, 1, "red"),
    Ball(200, 100, -1, 1, "green"),
    Ball(100, 200, 1, -1, "blue")
]

def loop():
    # 動かす
    for b in balls:
        # クラスで定義したメソッドは下記ような文法で使用することができる
        b.move(canvas)
        
    root.after(10,loop)

root = tk.Tk()
root.geometry("800x600")

canvas =tk.Canvas(root, width =800, height =600, bg="white")
canvas.place(x = 0, y = 0)

root.after(10, loop)

root.mainloop()

