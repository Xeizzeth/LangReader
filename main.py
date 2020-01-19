from random import choice

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class WordPopup(Popup):
    pass


class WordButton(ButtonBehavior, Label):
    def on_press(self):
        popup = WordPopup(title=self.text)
        popup.open()


class MainWindow(BoxLayout):
    def check_status(self, btn):
        imported_text = self.ids.text_input.text
        for word in imported_text.split():
            btn = WordButton(text=str(word), width=len(word) * 10, height=25, size_hint=(None, None))
            self.ids.text_layout.add_widget(btn)


class LangReaderApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    LangReaderApp().run()
