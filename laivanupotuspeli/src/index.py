from game.game import Game
from engine.application import Application
from engine.game_board_visual import GameBoardVisual
from engine.board_controller import BoardController
if __name__ == "__main__":
    g = Game()
    #e = Application(g.event_relay)
    #user_board_visual = GameBoardVisual(
    #    g.event_relay,
    #    e.renderer.asset_loader,
    #    10,
    #    10,
    #    e.renderer.display.resolution[0]/2-320,
    #    e.renderer.display.resolution[1]/2-320,
    #    64
    #)
    #e.renderer.add_renderable(
    #    user_board_visual
    #)
    #user_board_controller = BoardController(g.event_relay, g.player1.board, user_board_visual)
    #e.start()
