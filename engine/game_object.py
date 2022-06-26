from typing import List
from abc import ABC


class Transform:

    def __init__(self, x = 0, y = 0, width = 0, height = 0, scale_x = 1, scale_y = 1):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale_x = scale_x
        self.scale_y = scale_y
    
    @property
    def center(self):
        x = self.x + (self.width / 2)
        y = self.y + (self.height / 2)

        return x, y

    def change_position(self, x, y):
        self.x = x or self.x
        self.y = y or self.y

    def change_dimension(self, height, width):
        self.height = height or self.height
        self.width = width or self.width

    def change_scale(self, sx, sy):
        self.scale_x = sx + self.scale_x
        self.scale_y = sy + self.scale_y
#=================================================================================================================================================================
#                                                                   Game Object Class  #=================================================================================================================================================================

class AbstractGameObject(ABC):

    def __init__(self, transform: Transform, tags: List(str) = None, name: str = None):

        self.__transform__: Transform = transform or Transform()
        self.__tags__ = tags
        self.__name__ = name

    @property
    def transform(self):
        return self.__transform__

    @property
    def tags(self):
        return self.__tags__

    @property
    def name(self):
        return self.__name__

    def input(self):
        pass

    def update(self):
        pass

    def fixedUpdate(self):
        pass

    def render(self):
        pass


class GameObject(AbstractGameObject):

    def __init__(self, transform: Transform, tags: List(str) = None, name: str = None):
        super().__init__(transform= transform, tagss= tags, name= name)
        #On Screen
        self.started = False

        #Removed from screen
        self.destroyed = False

echo "# xyz_repo" >> README.md