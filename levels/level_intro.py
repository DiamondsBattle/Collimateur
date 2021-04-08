from ursina import *
from level import Level


class LevelIntro(Level):
    def __init__(self):
        super().__init__(
            name='intro',
            desc='The introduction for the game'
        )

        self.entities = {
            'map': Entity()
        }

        for i in self.entities:
            i.enabled = False
