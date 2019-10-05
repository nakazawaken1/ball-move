from tkinter import *
screen_width = 600
screen_height = 400
window = Tk() # ウインドウ作成
window.title('ブロックくずし')
canvas = Canvas(window, width=screen_width, height=screen_height) # 描画領域作成
canvas.pack() # ウインドウサイズを描画領域に合わせる
window.mainloop()  # ウィンドウを表示
