#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


class Player(Entity):

    def __init__(self):
        super().__init__()
        self.lives: int = None
        self.score: int = None

    def move(self):
        pass
