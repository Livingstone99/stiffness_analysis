import kivy

from kivy.app import App
kivy.require("1.10.1")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass
class LogInScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text = 'USERNAME:'))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

        self.add_widget(Label(text = 'PASSWORD:'))
        self.password = TextInput(multiline = False)
        self.add_widget(self.password)

        

class Simple(App):
    def build(self):
        my_wid = Widget()
        # with open('myOptions.txt') as f:
        #     contents = f.read()
        #     my_wid.text = contents

        return Widgets()
if __name__ == "__main__":
    Simple().run()