import pygame
import pygame_gui
from engine.event import Event
from engine.event_relay import EventRelay

class GUI_Holder:
    def __init__(self, event_relay: EventRelay, manager) -> None:
        self.event_relay = event_relay
        self.manager = manager
        self.scenes = {
            "ship_placement":
            {
                "ship_placement_button": pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((-300, 250), (200, 50)),
                    text="Confirm Ship Placement",
                    manager=self.manager,
                    anchors={"right": "right","top": "top"}
                ),

                "2x1": pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((-300, 100), (200, 50)),
                    text="2x1",
                    manager=self.manager,
                    anchors={"right": "right","top": "top"}
                ),

                "3x1": pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((-300, 150), (200, 50)),
                    text="3x1",
                    manager=self.manager,
                    anchors={"right": "right","top": "top"}
                ),

                "4x1": pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((-300, 200), (200, 50)),
                    text="4x1",
                    manager=self.manager,
                    anchors={"right": "right","top": "top"}
                ),
                "board_owner_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -340), (600, 32)),
                    text="Currently viewing your game board",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "task_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -400), (900, 600)),
                    text="""Place your ships ([R] to rotate ship, [Right Click] to place, [Left click] to remove)""",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                )
            },
            "user_guess":
            {
                "board_owner_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -340), (600, 50)),
                    text="Currently viewing the opponent's board",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "task_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -400), (900, 50)),
                    text="Fire a shot at a tile on the opponent's board (Left click to shoot at tile)",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                )
            },
            "opponent_guess":
            {
                "board_owner_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -340), (600, 50)),
                    text="Currently viewing your game board",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "task_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -400), (600, 50)),
                    text="The opponent is guessing",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                )
            },
            "opponent_win":
            {
                "board_owner_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -340), (600, 50)),
                    text="Currently viewing your game board",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "task_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -400), (600, 50)),
                    text="The opponent is guessing",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "win_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, 0), (600, 300)),
                    text="YOU LOSE!",
                    manager=self.manager,
                    anchors={"center": "center","center": "center"},
                    object_id=pygame_gui.core.ObjectID(object_id='#lose_text')
                )
            },
            "user_win":
            {
                "board_owner_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -340), (600, 50)),
                    text="Currently viewing the opponent's board",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "task_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, -400), (600, 50)),
                    text="Fire a shot at a tile on the opponent's board",
                    manager=self.manager,
                    anchors={"center": "center","top": "top"}
                ),
                "win_text": pygame_gui.elements.UILabel(
                    relative_rect=pygame.Rect((0, 0), (600, 300)),
                    text="YOU WIN!",
                    manager=self.manager,
                    anchors={"center": "center","center": "center"},
                    object_id=pygame_gui.core.ObjectID(object_id='#win_text')
                )
            },
        }
        self.ui_events = {
            "ship_placement":
            {
                "ship_placement_button": (Event.ON_CONFIRM_SHIP_BUTTON, None),

                "2x1": (Event.ON_SELECT_SHIP_TYPE, "2x1"),

                "3x1": (Event.ON_SELECT_SHIP_TYPE, "3x1"),

                "4x1": (Event.ON_SELECT_SHIP_TYPE, "4x1")
            },
            "user_guess": {},
            "opponent_guess": {}
        }
        for sk in self.scenes:
            self.disable_scene(sk)

    def process_events(self, events):
        for event in events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for sk, sv in self.scenes.items():
                    for k, v in sv.items():
                        if event.ui_element == v:
                            if self.ui_events[sk][k][1] is None:
                                self.event_relay.call(self.ui_events[sk][k][0])
                            else:
                                self.event_relay.call(self.ui_events[sk][k][0], self.ui_events[sk][k][1])

    def enable_scene(self, scene: str):
        for e in self.scenes[scene].values():
            e.enable()
            e.show()

    def disable_scene(self, scene: str):
        for e in self.scenes[scene].values():
            e.disable()
            e.hide()
