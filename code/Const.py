# C
import pygame

COLOR_GREEN = (72, 150, 44)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (237, 255, 0)

# E
ENTITY_SPEED = {
        'level1Bg0': 0,
        'level1Bg1': 2,
        'level1Bg2': 0.9,
        'level1Bg3': 6,
        'player': 4,
        'playerShot': 3,
        'enemy': 3,
        'enemyShot': 6,
}

ENTITY_HEALTH = {
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'player': 300,
    'playerShot': 1,
    'enemy': 60,
    'enemyShot': 1,
}

ENTITY_SHOT_DELAY = {
    'player': 20,
    'enemy': 140,

}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'SCORE',
               'EXIT')

# W
WIN_WIDTH = 1536
WIN_HEIGHT = 1000
