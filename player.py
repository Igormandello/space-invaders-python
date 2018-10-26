import pygame as pg

class Player:
  def __init__(self, pos, size, speed, sprite, display):
    self.image = pg.image.load(sprite).convert_alpha()
    self.image = pg.transform.scale(self.image, size)
    self.display = display
    self.pos = pos
    self.direction = (0, 0)
    self.speed = speed

  def move(self, direction):
    self.direction = (self.direction[0] + direction[0], self.direction[1] + direction[1])

  def stop(self, direction):
    self.direction = (self.direction[0] - direction[0], self.direction[1] - direction[1])

  def update(self):
    self.pos = (self.pos[0] + self.direction[0] * self.speed, self.pos[1] + self.direction[1] * self.speed)
    self.display.blit(self.image, self.pos)