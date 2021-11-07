#Couple issues but should work on the whole
from tkinter import *
canvas_height = 400
canvas_width = 600
canvas_colour = "black"
p1_x = canvas_width/2
p1_y = canvas_height
p1_colour = "green"
line_width = 5
line_length = 5
def p1_move_N(self):
  global p1_y
  canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
  p1_y = p1_y - line_length
def p1_move_S(self):
  global p1_y
  canvas.create_line(p1_x, p1_y, p1_x, p1_y=line_length, width=line_width, fill=p1_colour)
  p1_y = p1_y + line_length
def p1_move_E(self):
  global p1_x
  canvas.create_line(p1_x, p1_y, p1_x + line_length, width=line_width, fill=p1_colour)
  p1_x = p1_x + line_length
def p1_move_W(self):
  global p1_x
  canvas.create_line(p1_x, p1_y, p1_x-line_length, width=line_width, fill=p1_colour)
  p1_x = p1_x - line_length
def erase_all():
  canvas.delete(all)
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()
window.bind("<Up>",p1_move_N)
window.bind("<Down>",p1_move_S)
window.bind("<Right>",p1_move_E)
window.bind("<Left>",p1_move_W)
window.bind("<u>",erase_all)
window.mainloop()
