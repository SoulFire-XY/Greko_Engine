from .scene import Scene


class GameLoop:

    def __init__(self, limit_fps = 60):
        self.limit_fps = limit_fps

    def init(self, canvas, window=None):
        
        self.__start__game_loop()

    def __start__game_loop(self):

        gameobjects = Scene.get_active_scene().get_gameobjects()

        for go in gameobjects:
            go.start()

        #Game Loop
        while True:
            # update scene g.o.s
            Scene.get_active_scene().update_scene()

            # access objs in active scene 
            gameobjects = Scene.get_active_scene().get_gameobjects()

            # loop g.o.s in current scene
            for go in gameobjects:

                #start g.o.s
                if not go.started:
                    go.start()

                if go.destroyed:
                    Scene.get_active_scene().remove_game_object(go)

                # handle input
                go.input()

                #handle update
                go.update()

                # handle render
                go.render()
