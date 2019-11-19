from kivy.app import App
from kivy.uix.widget import Widget

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
    def on_touch_move(self, touch):
        print(touch)
    def on_touch_up(self, touch):
        print(touch)