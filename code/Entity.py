#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Entity:

    def __init__(self):
        self.name: str = None
        self.surf = None
        self.rect: pygame.Rect = None

    def move(self):
        pass

