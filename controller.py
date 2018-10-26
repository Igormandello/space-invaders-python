import pygame as pg
from player import Player

MOVEMENTS = {
  pg.K_w: ( 0, -1 ),
  pg.K_s: ( 0, 1 ),
  pg.K_a: ( -1, 0 ),
  pg.K_d: ( 1, 0 )
}

CLOCK = pg.time.Clock()

class Controller:
  def __init__(self, caption, size):
    pg.init()
    pg.display.set_caption(caption)
    self.screen = pg.display.set_mode(size)
    self.done = False

    self.player = Player((10, 10), (100, 100), 3, './assets/Koala.jpg', self.screen)

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
        if event.key in MOVEMENTS:
          self.player.move(MOVEMENTS[event.key])
      elif event.type == pg.KEYUP:
        if event.key in MOVEMENTS:
          self.player.stop(MOVEMENTS[event.key])

  def update(self):
    self.screen.fill((0, 0, 0))
    self.player.update()