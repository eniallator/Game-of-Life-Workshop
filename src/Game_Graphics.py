from time import time
import pygame


class Game_Graphics:
    def __init__(self, width, height):
        pygame.init()
        self.__screen_dim = (width, height)
        self.__screen = pygame.display.set_mode(self.__screen_dim)
        self.__done = False

    def rect(self, rgb, box):
        pygame.draw.rect(self.__screen, rgb, pygame.Rect(box['x'], box['y'], box['width'], box['height']))

    def get_pygame(self):
        return pygame

    def get_screen_dimensions(self):
        return {'x': self.__screen_dim[0], 'y': self.__screen_dim[1]}

    def loop(self, run_func):
        last_time = time()
        while not self.__done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__done = True

            self.rect(
                (0, 0, 0),
                {'x': 0, 'y': 0, 'width': self.__screen_dim[0], 'height': self.__screen_dim[1]}
            )
            dt = time() - last_time
            last_time = time()
            run_func(dt)
            pygame.display.flip()
