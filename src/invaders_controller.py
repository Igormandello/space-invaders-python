import random
import pygame as pg
from src.invader import Invader
from src.shot_controller import ShotController

DOWN = (0, 1)
LEFT = (-20, 0)
RIGHT = (20, 0)
SHOT_WIDTH = 4
SHOT_HEIGHT = 6

class InvadersController:
  def __init__(self, rows, cols, base_y, padding, size, sprites, display):
    self.rows = rows
    self.cols = cols
    self.base_y = base_y
    self.padding = padding
    self.size = size
    self.shot_controller = ShotController(size[1] + base_y, (SHOT_WIDTH, SHOT_HEIGHT), -3, './assets/shot.png', display)
    self.dir = RIGHT
    self.display_width = display.get_width()
    self.sprites = [sprites[0], sprites[1]]
    self.display = display

    self.reset()

  def reset(self):
    self.shot_controller.reset()
    self.dir = RIGHT
    self.frame_count = 0
    self.killed = 0
    self.invaders = []
    for y in range(self.rows):
      row = []
      for x in range(self.cols):
        invader_pos = (self.padding[0] + x * (self.size[0] + self.padding[0]), self.padding[1] + y * (self.size[1] + self.padding[1]))
        row.append(Invader(invader_pos, self.size, self.sprites, self.display))

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

  def update(self, player):
    ratio = self.killed / (self.rows * self.cols)

    self.frame_count += 1
    for y in range(self.rows):
      for x in range(self.cols):
        if not self.invaders[y][x] is None:
          self.invaders[y][x].update(self.frame_count % (30 - int(ratio * 30)) == 0)

    for x in range(self.cols):
      for y in range(self.rows - 1, -1, -1):
        if not self.invaders[y][x] is None:
          if random.random() < 0.001 + ratio / 100:
            self.shot_controller.base_y = self.invaders[y][x].pos[1] + self.size[1]
            self.shot_controller.send_shot(self.invaders[y][x].pos[0] + self.size[0] / 2 - SHOT_WIDTH / 2)
          
          break

    if self.frame_count % (120 - int(ratio * 120)) == 0:
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
    return self.shot_controller.check_hit(player)