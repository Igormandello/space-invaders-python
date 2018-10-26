import pygame as pg

class Player:
  def __init__(self, pos, size, sprite, display):
    self.image = pg.image.load(sprite).convert_alpha()
    self.image = pg.transform.scale(self.image, size)
    self.display = display
    self.pos = pos
    self.direction = (0, 0)

  def move(self, direction):
    self.direction = (self.direction[0] + direction[0], self.direction[1] + direction[1])

  def stop(self, direction):
    self.direction = (self.direction[0] - direction[0], self.direction[1] - direction[1])

  def update(self):
    self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
    self.display.blit(self.image, self.pos)