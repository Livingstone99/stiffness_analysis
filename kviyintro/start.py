import kivy
from kivy.properties import ListProperty
from kivy.app import App
kivy.require("1.10.1")
from kivy.uix.floatlayout import FloatLayout

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color,Rectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import  ScreenManager, Screen,SlideTransition
# Window.clearcolor = (1, 1, 1, 1)
kv  = Builder.load_file('myOptions.kv')
class cata(Screen):
    pass
class VegetablesClass(Screen):
    pass
class MyScreenManage(ScreenManager):
    pass
class myOptions(App):
    def build(self):
        return kv



if __name__ == "__main__":
    myOptions().run()