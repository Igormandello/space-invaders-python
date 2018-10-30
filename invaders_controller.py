import random
import pygame as pg
from invader import Invader
from shot_controller import ShotController

DOWN = (0, 1)
SHOT_SIZE = 6

class InvadersController:
  def __init__(self, rows, cols, base_y, padding, size, sprites, display):
    self.rows = rows
    self.cols = cols
    self.base_y = base_y
    self.padding = padding
    self.size = size
    self.shot_controller = ShotController(size[1] + base_y, (size[0], SHOT_SIZE), -3, './assets/shot.png', display)

    self.invaders = []
    for y in range(self.rows):
      row = []
      for x in range(self.cols):
        invader_pos = (padding[0] + x * (size[0] + padding[0]), padding[1] + y * (size[1] + padding[1]))
        row.append(Invader(invader_pos, size, random.choice(sprites), display))

      self.invaders.append(row)

  def update(self):
    for y in range(self.rows):
      for x in range(self.cols):
        self.invaders[y][x].update()

    self.shot_controller.update()