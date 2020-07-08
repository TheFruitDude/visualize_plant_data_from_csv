import tkinter as tk

root = tk.Tk()
WIDTH = HEIGHT = 400
x1 = y1 = WIDTH / 2
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
c1 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)
canvas.create_text((100,10), text="Move iwth a,d,w,s")
left, right, up, down = -10,10,-10,10

def keypress(event):
  """If you go down or right increase
     If you go left of up decrease"""
  x = 0
  y = 0
  if event.char == "a": x = -10 # left 
  elif event.char == "d": x = 10 # right
  elif event.char == "w": y = -10 # up
  elif event.char == "s": y = 10 # down
  canvas.move(c1, x, y)


root.bind("<Key>", keypress)
root.mainloop()