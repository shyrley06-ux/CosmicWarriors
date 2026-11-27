
#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Player import Player
from code.Enemy import Enemy
from code.Background import Background


class EntityFactory:

    def get_entity(self, entity_type, surf=None):

        if entity_type == "Player":
            return Player()

        elif entity_type == "Enemy":
            return Enemy()

        elif entity_type == "Background":
            return Background(surf)

        return None
