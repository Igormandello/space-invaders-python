import pygame as pg
from src.invader import Invader
from src.shot_controller import ShotController

DOWN = (0, 1)
LEFT = (-20, 0)
RIGHT = (20, 0)
SHOT_SIZE = 6

class InvadersController:
  def __init__(self, rows, cols, base_y, padding, size, sprites, display):
    self.rows = rows
    self.cols = cols
    self.base_y = base_y
    self.padding = padding
    self.size = size
    self.shot_controller = ShotController(size[1] + base_y, (size[0], SHOT_SIZE), -3, './assets/shot.png', display)
    self.frame_count = 0
    self.dir = RIGHT
    self.display_width = display.get_width()
    self.killed = 0

    self.invaders = []
    for y in range(self.rows):
      row = []
      for x in range(self.cols):
        invader_pos = (padding[0] + x * (size[0] + padding[0]), padding[1] + y * (size[1] + padding[1]))
        row.append(Invader(invader_pos, size, [sprites[0], sprites[1]], display))

      self.invaders.append(row)

  def check_kill(self, shot):
    for y in range(self.rows):
      for x in range(self.cols):
        if not self.invaders[y][x] is None:
          if self.invaders[y][x].intersects(shot):
            self.invaders[y][x] = None
            self.killed += 1
            return True

    return False

  def move_all(self, direction):
    for y in range(self.rows):
      for x in range(self.cols):
        if not self.invaders[y][x] is None:
          invader = self.invaders[y][x]
          self.invaders[y][x].move(direction)
          self.invaders[y][x].pos = (max(-1, min(invader.pos[0], self.display_width - invader.size[0] + 1)), invader.pos[1])

  def update(self):
    self.frame_count += 1
    for y in range(self.rows):
      for x in range(self.cols):
        if not self.invaders[y][x] is None:
          self.invaders[y][x].update(self.frame_count % 40 == 0)

    if self.frame_count % (120 - self.killed * 4) == 0:
      self.frame_count = 0

      self.move_all(self.dir)

      for y in range(self.rows):
        broke = False
        for x in range(self.cols):
          if not self.invaders[y][x] is None:
            if self.invaders[y][x].pos[0] + self.invaders[y][x].size[0] > self.display_width:
              self.dir = LEFT
              self.move_all((-1, self.size[1]))
              broke = True
            elif self.invaders[y][x].pos[0] < 0:
              self.dir = RIGHT
              self.move_all((1, self.size[1]))
              broke = True
          
        if broke:
          break

    self.shot_controller.update()