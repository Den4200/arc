from kivy.lang import Builder
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty
)
from kivy.uix.codeinput import CodeInput
from kivy.uix.screenmanager import Screen

from arc.terminal import Terminal  # NOQA: F401

Builder.load_file('arc/editor.kv')


class EditorScreen(Screen):
    editor = ObjectProperty()
    recycler = ObjectProperty()

    foreground_color = ColorProperty((1, 1, 1, 1))
    background_color = ColorProperty((0.2, 0.2, 0.2, 1))

    font_size = NumericProperty(15)


class Editor(CodeInput):
    file_path = StringProperty()
