import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

import kivy
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView, FileChooser
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

        self.rows = 4
        self.cols = 1

        self.title_text = Label(text="Auditor")
        self.add_widget(self.title_text)

        self.input_selector = FileSelector("Select Input Path")
        self.add_widget(self.input_selector)
        self.output_selector = FileSelector("Select Output Path")
        self.add_widget(self.output_selector)

        self.progress_text = Label(text="")
        self.add_widget(self.progress_text)

class FileSelector(GridLayout):

    def __init__(self, button_text, **kwargs):
        super(FileSelector, self).__init__(**kwargs)

        self.rows = 1
        self.cols = 2
        self.file = None

        self.select_button = Button(text=button_text, on_press=self.open_selector)
        self.add_widget(self.select_button)

        self.path_text = Label(text="")
        self.add_widget(self.path_text)

    def open_selector(self, instance):
        self.popup = Popup(title=self.select_button.text)

        content = GridLayout()
        self.popup.content = content
        content.cols = 1
        content.rows = 2

        self.file_chooser = FileChooserListView()
        content.add_widget(self.file_chooser)

        self.back_button = Button(text="Back", on_press=self.close_selector, size_hint=(0.3, 0.1))
        content.add_widget(self.back_button)

        self.popup.open()

    def close_selector(self, instance):
        self.path_text.text = self.file_chooser.path
        self.popup.dismiss()

if __name__ == "__main__":
    gui = AuditorApp()
    gui.run()