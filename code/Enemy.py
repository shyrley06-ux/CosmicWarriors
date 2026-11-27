
#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


class Enemy(Entity):

    def __init__(self):
        super().__init__()
        self.speed: int = None
        self.health: int = None

    def move(self):
        pass
