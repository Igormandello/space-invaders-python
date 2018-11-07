import pygame as pg

class SceneController:
  def __init__(self, backgrounds, reset_fn, display):
    self.backgrounds = backgrounds
    for i in range(len(backgrounds)):
      if type(backgrounds[i]) == tuple:
        self.backgrounds.append(lambda: display.fill(backgrounds[i]))
      elif type(backgrounds[i]) == str:
        image = pg.image.load(backgrounds[i]).convert_alpha()
        image = pg.transform.scale(image, (display.get_width(), display.get_height()))
        self.backgrounds[i] = image
      elif type(backgrounds[i]) == list:
        images = []
        for img in backgrounds[i]:
          image = pg.image.load(img).convert_alpha()
          image = pg.transform.scale(image, (display.get_width(), display.get_height()))
          images.append(image)

        self.backgrounds[i] = images

    self.reset = reset_fn
    self.display = display
    self.current = 0
    self.frame = 0
    self.index = 0

  def in_game(self):
    return self.current == 1

  def process_action(self): 
    if self.current > 1:
      self.current = 1
      self.frame = 0
      self.reset()
    elif self.current == 0:
      self.current = 1
      self.frame = 0

  def win(self):
    self.current = 2
    self.frame = 0

  def lose(self):
    self.current = 3
    self.frame = 0

  def update(self):
    self.frame += 1
    if type(self.backgrounds[self.current]) == tuple:
      self.display.fill(self.backgrounds[self.current])
    elif type(self.backgrounds[self.current]) == pg.Surface:
      self.display.blit(self.backgrounds[self.current], (0, 0))
    elif type(self.backgrounds[self.current]) == list:
      if self.frame % 80 == 0:
        self.frame = 0
        self.index += 1
        if self.index > 1:
          self.index = 0

      self.display.blit(self.backgrounds[self.current][self.index], (0, 0))
