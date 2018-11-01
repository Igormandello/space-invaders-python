import pygame as pg

UP = (0, -1)

class ShotController:
  def __init__(self, base_y, size, speed, sprite, display):
    self.image = pg.image.load(sprite).convert_alpha()
    self.image = pg.transform.scale(self.image, size)
    self.base_y = base_y
    self.size = size
    self.display = display
    self.display_width = display.get_width()
    self.speed = speed
    self.shots = []

  def reset(self):
    self.shots = []

  def check_hit(self, target):
    nextShots = []
    hit = False
    for i in range(len(self.shots)):
      shot = self.shots[i]
      if not target.check_kill([shot[0], shot[1], self.size[0], self.size[1]]):
        nextShots.append(shot)
      else:
        hit = True

    self.shots = nextShots
    return hit

  def send_shot(self, x):
    self.shots.append((x, self.base_y))

  def update(self):
    newList = []
    for i in range(len(self.shots)):
      self.shots[i] = (self.shots[i][0], self.shots[i][1] + UP[1] * self.speed)
      if self.shots[i][1] > -self.size[1]:
        newList.append(self.shots[i])
        self.display.blit(self.image, self.shots[i])

    self.shots = newList