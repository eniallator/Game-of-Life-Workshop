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

    def loop(self):
        while not self.__done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__done = True

            pygame.display.flip()


if __name__ == "__main__":
    game = Game_Graphics(800, 600)
    game.loop()
