from ursina import *


class Collimateur(Ursina):
    def __init__(self):
        super().__init__(
            borderless=False,
            title='Collimateur'
        )

        self.run()


if __name__ == '__main__':
    app = Collimateur()
