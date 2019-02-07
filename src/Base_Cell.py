class Base_Cell:
    state = 0

    @staticmethod
    def try_spawn(self):
        print('Error: ' + self.__class__.__name__ + ' hasn\'t gotten a try_spawn method yet.')

    def update(self):
        print('Error: ' + self.__class__.__name__ + ' hasn\'t gotten an update method yet.')

    def draw(self):
        print('Error: ' + self.__class__.__name__ + ' hasn\'t gotten a draw method yet.')
