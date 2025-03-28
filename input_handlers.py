from typing import Optional

import tcod.event

from actions import Action, EscapeAction, BumpAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        if key == tcod.event.KeySym.KP_8: # Up
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.KP_2: # Down
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.KP_4: # Left
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.KP_6: # Right
            action = BumpAction(dx=1, dy=0)
        elif key == tcod.event.KeySym.KP_7: # Up-Left
            action = BumpAction(dx=-1, dy=-1)
        elif key == tcod.event.KeySym.KP_9: # Up-Right
            action = BumpAction(dx=1, dy=-1)
        elif key == tcod.event.KeySym.KP_1: # Down-Left
            action = BumpAction(dx=-1, dy=1)
        elif key == tcod.event.KeySym.KP_3: # Down-Right
            action = BumpAction(dx=1, dy=1)

        elif key == tcod.event.KeySym.KP_5: # Wait
            action = BumpAction(dx=0, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()


        # No valid key was pressed
        return action