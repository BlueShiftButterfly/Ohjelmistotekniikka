from engine.display import Display
from engine.render_clock import RenderClock

class Renderer:
    def __init__(self, display: Display, render_clock: RenderClock):
        self.__do_rendering = True
        self.__display = display
        self.__render_clock = render_clock
        self.__loop_functions = []
    
    def start(self):
        while self.__do_rendering:
            self.__render()

    def stop(self):
        self.__do_rendering = False

    def register_loop(self, func):
        self.__loop_functions.append(func)

    def __render(self):
        for loop in self.__loop_functions:
            loop()
        if self.__do_rendering is False: return
        self.__display.update()
        self.__render_clock.tick(60)
