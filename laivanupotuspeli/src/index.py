from game.game import Game
from engine.application import Application

if __name__ == "__main__":
    g = Game()
    e = Application(g.event_relay)
