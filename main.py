import tkinter # GUI描画

screen_width = 600 # 画面の幅
screen_height = 400 # 画面の高さ
blocks_height = 200 # ブロック部分の高さ
fps = 1000 // 30 # 描画間隔
block_columns = 10 # ブロックの横の数
block_rows = 4 # ブロックの縦の数
colors = ['', 'red', 'yellow', 'blue', 'gray'] # ブロックの色

class Ball:

  def __init__(self):
    self.r = 10 # 半径
    self.x = screen_width // 2 - self.r # 初期横位置
    self.y = screen_height * 3 // 4 - self.r # 初期縦位置
    self.dx = 4 # 初期横移動量
    self.dy = 3 # 初期縦移動量
  
  def left(self):
    return self.x - self.r

  def right(self):
    return self.x + self.r

  def top(self):
    return self.y - self.r

  def bottom(self):
    return self.y + self.r

  def draw(self, canvas):
    canvas.create_oval(
        self.x - self.r, self.y - self.r,
        self.x + self.r, self.y + self.r,
        fill = 'green')
  
  def move(self):
    global gameover
    self.x += self.dx
    self.y += self.dy
    if self.x <= self.r or self.x + self.r >= screen_width:
      self.dx = -self.dx
    if self.y <= self.r:
      self.dy = -self.dy
    if self.y + self.r >= screen_height:
      gameover = True

  def hit(self, target):
    if self.left() <= target.right() and target.left() <= self.right() and self.top() <= target.bottom() and target.top() <= self.bottom():
      return True
    return False

class Block:
  def __init__(self, row, column, life = 1):
    self.row = row
    self.column = column
    self.life = life

  def left(self):
    return self.column * screen_width // block_columns
  
  def top(self):
    return self.row * blocks_height // block_rows
  
  def right(self):
    return self.left() + screen_width // block_columns - 1
  
  def bottom(self):
    return self.top() + blocks_height // block_rows - 1

  def color(self):
    return colors[self.life]

  def draw(self, canvas):
    if self.life > 0:
      canvas.create_rectangle(self.left(), self.top(), self.right(), self.bottom(), fill=self.color())

  def act(self, ball):
    global score
    if self.life > 0 and ball.hit(self):
      ball.dx = -ball.dx
      ball.dy = -ball.dy
      self.life -= 1
      score += 100

class Bar:
  
  def __init__(self, width=200, height=10):
    self.width = width
    self.height = height
    self.x = screen_width // 2
    self.y = screen_height - height
  
  def left(self):
    return self.x - self.width // 2
  
  def right(self):
    return self.x + self.width // 2
  
  def top(self):
    return self.y - self.height // 2
  
  def bottom(self):
    return self.y + self.height // 2

  def draw(self, canvas):
    canvas.create_rectangle(self.left(), self.top(), self.right(), self.bottom(), fill='pink')
    
  def act(self, ball):
    global score
    if ball.hit(self):
      ball.dy = -ball.dy
      score += 1

def gameloop():
  global gameover
  if not gameover:
    ball.move() # ボール移動
    bar.act(ball) # バー動作
    for row in blocks: # ブロックの衝突判定
      for block in row:
        block.act(ball)
  canvas.delete('all') # 画面クリア
  for row in blocks: # ブロックの描画
    for block in row:
      block.draw(canvas)
  ball.draw(canvas) # ボールの描画
  bar.draw(canvas) # バーの描画
  canvas.create_text(screen_width - 50, 10, text = 'score {:,d}'.format(score), fill = 'black') # 点数の描画
  if gameover:
     canvas.create_text(screen_width // 2, screen_height // 2, text = 'GameOver', font=('Times', '100', ('italic', 'bold')))
  window.after(fps, gameloop) # 繰り返し

gameover = False # ゲームオーバーかどうか
score = 0 # 点数
ball = Ball() # ボール
bar = Bar() # バー
blocks = [] # ブロック
def setup():
  global gameover, score, ball, bar, blocks
  gameover = False
  score = 0
  ball = Ball()
  bar = Bar()
  blocks = []
  for row in range(0, block_rows):
    blocks.append([])
    for column in range(0, block_columns):
      blocks[-1].append(Block(row, column, block_rows - row))    

def motion(e): # マウスポインタの移動
  bar.x = e.x

def click(e): # マウスボタンクリック時
  global gameover
  if gameover:
    setup()

window = tkinter.Tk() # ウインドウ作成
window.title('ブロックくずし')
window.bind('<Motion>', motion)
window.bind('<Button-1>', click)
canvas = tkinter.Canvas(window, width=screen_width, height=screen_height) # 描画領域作成
canvas.pack() # ウインドウサイズを描画領域に合わせる
setup()
gameloop()
window.mainloop()  # ウィンドウを表示
