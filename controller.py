import pygame as pg
from player import Player

UP = ( 0, -1 )
DOWN = ( 0, 1 )
LEFT = ( -1, 0 )
RIGHT = ( 1, 0 )

CLOCK = pg.time.Clock()

class Controller:
  def __init__(self, caption, size):
    pg.init()
    pg.display.set_caption(caption)
    self.screen = pg.display.set_mode(size)
    self.done = False

    self.player = Player((10, 10), (100, 100), './assets/Koala.jpg', self.screen)

  def run(self):
    while not self.done:
      self.treat_events()
      self.update()

      pg.display.update()
      CLOCK.tick(40)

    pg.display.quit()

  def treat_events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
        self.done = True
      elif event.type == pg.KEYDOWN:
        if event.key == pg.K_w:
          self.player.move(UP)
        elif event.key == pg.K_s:
          self.player.move(DOWN)
        elif event.key == pg.K_a:
          self.player.move(LEFT)
        elif event.key == pg.K_d:
          self.player.move(RIGHT)
      elif event.type == pg.KEYUP:
        if event.key == pg.K_w:
          self.player.stop(UP)
        elif event.key == pg.K_s:
          self.player.stop(DOWN)
        elif event.key == pg.K_a:
          self.player.stop(LEFT)
        elif event.key == pg.K_d:
          self.player.stop(RIGHT)

  def update(self):
    self.player.update()