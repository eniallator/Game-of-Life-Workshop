from src.Game import Game

GAME = Game(50, 50)


def main():
    GAME.update()
    GAME.draw()


if __name__ == '__main__':
    main()
