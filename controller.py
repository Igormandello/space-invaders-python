import pygame as pg
from player import Player
from shot_controller import ShotController

MOVEMENTS = {
  pg.K_a: -1,
  pg.K_d: 1
}

CLOCK = pg.time.Clock()
PLAYER_SIZE = 50
SHOT_SIZE = 40

class Controller:
  def __init__(self, caption, size):
    pg.init()
    pg.display.set_caption(caption)
    self.screen = pg.display.set_mode(size)
    self.done = False

    self.player = Player((10, size[1] - PLAYER_SIZE * 5 / 4), (PLAYER_SIZE, PLAYER_SIZE), 3, './assets/player.png', self.screen)
    self.shot_controller = ShotController(size[1] - PLAYER_SIZE * 5 / 4, (PLAYER_SIZE, SHOT_SIZE), 4, './assets/shot.png', self.screen)

  def run(self):
    while not self.done:
      self.treat_events()
      self.update()

      pg.display.update()
      CLOCK.tick(120)

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
        elif event.key == pg.K_SPACE:
          self.shot_controller.send_shot(self.player.pos[0])

  def update(self):
    self.screen.fill((0, 0, 0))
    self.player.update()
    self.shot_controller.update()