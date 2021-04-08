from ursina import *
from levels.level_intro import LevelIntro


class Collimateur(Entity):
    def __init__(self):
        self.app = Ursina(
            borderless=False,
            title='Collimateur'
        )
        super().__init__(
            eternal=True
        )

        self.levels = {
            'intro': LevelIntro()
        }

        self.app.run()

    def update(self):
        pass


if __name__ == '__main__':
    app = Collimateur()
