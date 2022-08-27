class Scene:

    __active_scene__ = None

    def __init__(self, game_objects: list, width= 1280, height= 720):   

        self.__new_objects__ = set()
        self.__active_objects__ = set()
        self.__delete_objects__ = []
        self.__width__ = width
        self.__height__ = height

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @classmethod
    def get_active_scene(cls):
        return cls.__active_scene__

    @classmethod
    def add_to_active_scene(cls, game_object):
        try:
            cls.__active_scene__.load_game_object(game_object)
        except AttributeError:
            print("No active scene available")

    def load_game_object(self, game_object):
        self.__new_objects__.add(game_object)

    def remove_game_object(self, game_object):
        self.__active_objects__.remove(game_object)

    def active_scene(self):
        Scene.__active_scene__ = self

    @classmethod
    def get_game_objects(cls):
        cls.__active_scene__.get_active_gameobjects()

    def get_activegameobjects(self):
        return self.__active_objects__

    def update_scene(self):

        while True:
            try:
                item = self.__new_objects__.pop()
                self.__active_objects__.add(item)
            except KeyError:
                break

        while True:
            try:
                item = self.__delete_objects__.pop()
                self.__active_objects__.remove(item)
            except IndexError:
                break
