import pygame as pg

class Invader:
  def __init__(self, pos, size, sprite, display):
    self.image = pg.image.load(sprite).convert_alpha()
    self.image = pg.transform.scale(self.image, size)
    self.pos = pos
    self.size = size
    self.display = display

  def move(self, direction):
    self.pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])

  def intersects(self, rect):
    return !(rect[0] + rect[2] < self.pos[0] or rect[0] > self.pos[0] + self.size[0] or
             rect[1] + rect[3] < self.pos[1] or rect[1] > self.pos[1] + self.size[1])

  def update(self):
    self.display.blit(self.image, self.pos)