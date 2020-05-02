from typing import Any

from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition

from arc.editor import EditorScreen

Config.set('input', 'mouse', 'mouse, multitouch_on_demand')

Builder.load_file('core.kv')


class Manager(ScreenManager):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.transition = NoTransition()

        self.add_widget(EditorScreen())


class Arc(App):

    def build(self) -> Manager:
        self.title = 'Arc'
        return Manager()
