import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

import kivy
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

class AuditorApp(App):

    def __init__(self):
        super(AuditorApp, self).__init__()

    def build(self):
        self.root = AuditorView()

class AuditorView(GridLayout):

    def __init__(self, **kwargs):
        super(AuditorView, self).__init__(**kwargs)

        self.rows = 1
        self.cols = 1

        self.filechooser = FileChooserListView()
        self.add_widget(self.filechooser)

if __name__ == "__main__":
    gui = AuditorApp()
    gui.run()