import tkinter #GUI描画
screen_width = 600 # 画面の幅
screen_height = 400 # 画面の高さ
fps = 1000 // 30 # 描画間隔
window = tkinter.Tk() # ウインドウ作成
window.title('ブロックくずし')
canvas = tkinter.Canvas(window, width=screen_width, height=screen_height) # 描画領域作成
canvas.pack() # ウインドウサイズを描画領域に合わせる

class Ball:

  def __init__(self):
    self.r = 10 # 半径
    self.x = screen_width / 2 - self.r # 初期横位置
    self.y = screen_height / 2 - self.r # 初期縦位置
    self.dx = 4 # 初期横移動量
    self.dy = 3 # 初期縦移動量

  def draw(self, canvas):
    canvas.create_oval(
        self.x - self.r, self.y - self.r,
      self.x + self.r, self.y + self.r,
        fill = 'green')

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x <= self.r or self.x + self.r >= screen_width:
      self.dx = -self.dx
    if self.y <= self.r or self.y + self.r >= screen_height:
      self.dy = -self.dy

ball = Ball()

def gameloop():
  ball.move() # ボール移動
  canvas.delete('all') # 画面クリア
  ball.draw(canvas) # ボールの描画
  window.after(fps, gameloop) # 繰り返し

gameloop()
window.mainloop()  # ウィンドウを表示
