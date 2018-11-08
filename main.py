import pygame as pg
from src.controller import Controller

if __name__ == '__main__':
  controller = Controller('Space Invaders', './assets/icon.png', (500, 750))
  controller.run()