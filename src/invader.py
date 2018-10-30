import pygame as pg

class Invader:
  def __init__(self, pos, size, sprites, display):
    self.images = [pg.image.load(sprites[0]).convert_alpha(), pg.image.load(sprites[1]).convert_alpha()]
    self.images = [pg.transform.scale(self.images[0], size), pg.transform.scale(self.images[1], size)]
    self.image_index = 0
    self.pos = pos
    self.size = size
    self.display = display

  def move(self, direction):
    self.pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])

  def intersects(self, rect):
    return not (rect[0] + rect[2] < self.pos[0] or rect[0] > self.pos[0] + self.size[0] or
                rect[1] + rect[3] < self.pos[1] or rect[1] > self.pos[1] + self.size[1])

  def update(self, pass_image):
    if pass_image:
      self.image_index += 1
      if self.image_index > 1:
        self.image_index = 0

    self.display.blit(self.images[self.image_index], self.pos)