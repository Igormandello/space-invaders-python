import pygame as pg

class Controller:
  def __init__(self, caption, size):
    pg.init()
    pg.display.set_caption(caption)
    self.screen = pg.display.set_mode(size)
    self.done = False

  def run(self):
    while not self.done:
      for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
          self.done = True

      pg.display.update()

    pg.display.quit()