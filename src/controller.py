import pygame as pg
from src.scene_controller import SceneController
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
  def __init__(self, caption, icon, size):
    pg.init()
    pg.font.init()
    pg.display.set_caption(caption)

    self.screen = pg.display.set_mode(size)
    self.done = False
    self.font = pg.font.Font('./assets/arcade.ttf', 20)

    icon = pg.image.load(icon)
    pg.display.set_icon(icon)

    self.scene_controller = SceneController([['./assets/initialScreen1.png', './assets/initialScreen2.png'], (0, 0, 0), ['./assets/endScreen1.png', './assets/endScreen2.png'], ['./assets/endScreen1.png', './assets/endScreen2.png']], self.reset, self.screen)
    self.player = Player((size[0] / 2 - PLAYER_SIZE / 2, size[1] - PLAYER_SIZE * 5 / 4), (PLAYER_SIZE, PLAYER_SIZE), 3, './assets/player.png', self.screen)
    self.shot_controller = ShotController(size[1] - PLAYER_SIZE * 5 / 4, (SHOT_WIDTH, SHOT_HEIGHT), 8, './assets/shot.png', self.screen, 60)

    invadersSprites = [
      [
        './assets/invader11.png',
        './assets/invader12.png'
      ], [
        './assets/invader21.png',
        './assets/invader22.png'
      ], [
        './assets/invader21.png',
        './assets/invader22.png'
      ], [
        './assets/invader31.png',
        './assets/invader32.png'
      ]
    ]
    self.invaders_controller = InvadersController(4, 7, 30, (30, 20), (34, 34), invadersSprites, self.screen)
    self.score = 0

  def reset(self):
    self.score = 0
    self.player.reset()
    self.shot_controller.reset()
    self.invaders_controller.reset()

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
        elif event.key == pg.K_RETURN:
          self.scene_controller.process_action()
      elif event.type == pg.KEYUP:
        if event.key in MOVEMENTS:
          self.player.stop(MOVEMENTS[event.key])

  def update(self):
    self.scene_controller.update()

    if self.scene_controller.in_game():
      self.screen.blit(self.font.render('SCORE:' + str(self.score), True, (255, 255, 255)), (10, 10))

      self.player.update()
      if self.shot_controller.check_hit(self.invaders_controller):
        self.score += 100
      self.shot_controller.update()

      if self.invaders_controller.max_y() >= self.player.pos[1]:
        self.scene_controller.lose()
      elif self.invaders_controller.game_end():
        self.scene_controller.win()
      else:
        if self.invaders_controller.update(self.player):
          self.scene_controller.lose()

    return True