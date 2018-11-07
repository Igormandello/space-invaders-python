import pygame as pg

class SceneController:
  def __init__(self, backgrounds, display):
    self.backgrounds = []
    for b in backgrounds:
      if type(b) == tuple:
        self.backgrounds.append(lambda: display.fill(b))
      elif type(b) == str:
        image = pg.image.load(b).convert_alpha()
        image = pg.transform.scale(image, (display.get_width(), display.get_height()))
        self.backgrounds.append(lambda: display.blit(image, (0, 0)))

    self.current = 0

  def update(self):
    self.backgrounds[self.current]()