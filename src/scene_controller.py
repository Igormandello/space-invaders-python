import pygame as pg

class SceneController:
  def __init__(self, backgrounds, reset_fn, display):
    self.backgrounds = backgrounds
    for i in range(len(backgrounds)):
      if type(backgrounds[i]) == tuple:
        self.backgrounds.append(lambda: display.fill(backgrounds[i]))
      elif type(backgrounds[i]) == str:
        image = pg.image.load(b).convert_alpha()
        image = pg.transform.scale(image, (display.get_width(), display.get_height()))
        self.backgrounds[i] = image

    self.reset = reset_fn
    self.display = display
    self.current = 0

  def in_game(self):
    return self.current == 1

  def process_action(self): 
    if self.current > 1:
      self.current = 1
      self.reset()
    elif self.current == 0:
      self.current = 1

  def win(self):
    self.current = 2

  def lose(self):
    self.current = 3

  def update(self):
    if type(self.backgrounds[self.current]) == tuple:
      self.display.fill(self.backgrounds[self.current])
    else:
      self.display.blit(self.backgrounds[self.current], (0, 0))