import pygame


class Game_Graphics:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((800, 600))
        self.__done = False

    def loop(self):
        while not self.__done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__done = True

            pygame.draw.rect(self.__screen, (0, 200, 0), pygame.Rect(100, 100, 50, 50))
            pygame.display.flip()


if __name__ == "__main__":
    game = Game_Graphics()
    game.loop()
