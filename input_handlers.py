from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        if key == tcod.event.KeySym.KP_8: # Up
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.KP_2: # Down
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.KP_4: # Left
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.KP_6: # Right
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.KeySym.KP_7: # Up-Left
            action = MovementAction(dx=-1, dy=-1)
        elif key == tcod.event.KeySym.KP_9: # Up-Right
            action = MovementAction(dx=1, dy=-1)
        elif key == tcod.event.KeySym.KP_1: # Down-Left
            action = MovementAction(dx=-1, dy=1)
        elif key == tcod.event.KeySym.KP_3: # Down-Right
            action = MovementAction(dx=1, dy=1)

        elif key == tcod.event.KeySym.KP_5: # Wait
            action = MovementAction(dx=0, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()


        # No valid key was pressed
        return action