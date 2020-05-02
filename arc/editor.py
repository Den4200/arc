from typing import Any, Tuple

from kivy.core.window import Keyboard
from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    ObservableList,
    StringProperty
)
from kivy.uix.codeinput import CodeInput
from kivy.uix.screenmanager import Screen

from arc import KEYS
from arc.terminal import Terminal  # NOQA: F401

Builder.load_file('arc/editor.kv')


class EditorScreen(Screen):
    editor = ObjectProperty()
    recycler = ObjectProperty()

    foreground_color = ColorProperty((1, 1, 1, 1))
    background_color = ColorProperty((0.2, 0.2, 0.2, 1))

    font_size = NumericProperty(15)


class Editor(CodeInput):
    file_path = StringProperty('arc/core.py')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        with open(self.file_path, 'r') as f:
            self.text = f.read()

    def keyboard_on_key_down(
            self,
            window: Keyboard,
            keycode: Tuple[int, str],
            text: str,
            modifiers: ObservableList
    ):
        """
        Captures specific key presses
        and executes accordingly.
        """
        if keycode[0] in KEYS['s'] and 'ctrl' in modifiers:
            with open(self.file_path, 'w') as f:
                f.write(self.text)

        elif keycode[0] in KEYS['del', 'backspace']:
            self.cancel_selection()

        elif keycode[0] in KEYS['='] and 'ctrl' in modifiers:
            self.font_size += 1

        elif keycode[0] in KEYS['-'] and 'ctrl' in modifiers:
            if self.font_size > 0:
                self.font_size -= 1

        return super().keyboard_on_key_down(
            window, keycode, text, modifiers
        )
