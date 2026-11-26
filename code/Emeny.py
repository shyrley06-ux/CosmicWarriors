#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Emeny(Entity, Entity):

    def __init__(self):
        self.speed: int = None
        self.health: int = None

    def move(self):
        pass
