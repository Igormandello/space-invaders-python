import pygame as pg
from src.player import Player
from src.shot_controller import ShotController
from src.invaders_controller import InvadersController

MOVEMENTS = {
  pg.K_a: -1,
  pg.K_d: 1,
  pg.K_RIGHT: 1,
  pg.K_LEFT: -1
}

CLOCK = pg.time.Clock()
PLAYER_SIZE = 50
SHOT_WIDTH = 4
SHOT_HEIGHT = 10

class Controller:
  def __init__(self, caption, size):
    pg.init()
    pg.display.set_caption(caption)
    self.screen = pg.display.set_mode(size)
    self.done = False

    self.player = Player((size[0] / 2 - PLAYER_SIZE / 2, size[1] - PLAYER_SIZE * 5 / 4), (PLAYER_SIZE, PLAYER_SIZE), 3, './assets/player.png', self.screen)
    self.shot_controller = ShotController(size[1] - PLAYER_SIZE * 5 / 4, (SHOT_WIDTH, SHOT_HEIGHT), 8, './assets/shot.png', self.screen)
    self.invaders_controller = InvadersController(4, 7, 10, (30, 20), (34, 25), ['./assets/invader.png', './assets/invader2.png'], self.screen)

  def run(self):
    while not self.done:
      self.treat_events()
      if not self.update():
        self.done = True

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
        elif event.key == pg.K_SPACE:
          self.shot_controller.send_shot(self.player.pos[0] + PLAYER_SIZE / 2 - SHOT_WIDTH / 2)
      elif event.type == pg.KEYUP:
        if event.key in MOVEMENTS:
          self.player.stop(MOVEMENTS[event.key])

  def update(self):
    self.screen.fill((0, 0, 0))
    self.player.update()
    self.shot_controller.check_hit(self.invaders_controller)
    self.shot_controller.update()

    if not self.invaders_controller.game_end():
      if self.invaders_controller.update(self.player):
        self.player.reset()
        self.shot_controller.reset()
        self.invaders_controller.reset()
    else:
      print('Win')
      return False

    return True