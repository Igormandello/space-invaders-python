import pygame as pg

class Player:
  def __init__(self, pos, size, speed, sprite, display):
    self.image = pg.image.load(sprite).convert_alpha()
    self.image = pg.transform.scale(self.image, size)
    self.size = size
    self.display = display
    self.display_width = display.get_width()
    self.starting_pos = pos
    self.pos = pos
    self.horizontal = 0
    self.speed = speed

  def reset(self):
    self.pos = self.starting_pos

  def move(self, direction):
    self.horizontal = self.horizontal + direction

  def stop(self, direction):
    self.horizontal = self.horizontal - direction

  def check_kill(self, rect):
    return not (rect[0] + rect[2] < self.pos[0] or rect[0] > self.pos[0] + self.size[0] or
                rect[1] + rect[3] < self.pos[1] or rect[1] > self.pos[1] + self.size[1])

  def update(self):
    self.pos = (self.pos[0] + self.horizontal * self.speed, self.pos[1])
    self.pos = (max(0, min(self.pos[0], self.display_width - self.size[0])), self.pos[1])

    self.display.blit(self.image, self.pos)