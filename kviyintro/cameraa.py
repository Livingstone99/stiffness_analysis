'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ListProperty




class MyWidget(Widget):
    r_size = ListProperty([0, 0])

class otyr(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    otyr().run()


# r_size: [root.size[0]/2, root.size[1]/2]
#     Canvas:
#         Color:
#             rgba: .5,1,.9,.8
#         Rectangle:
#             # self here refers to the widget i.e FloatLayout
#             size: root.r_size
#             pos: 0, root.size[1]-root.r_size[1]
# Button:
#         background_normal: 'shopping-basket.png'
#         background_down: ''
#         background_disabled_normal: 'shopping-basket.png'
#         pos: 0,520
#
#     Button:
#         background_normal: 'seasoning.png'
#         background_down: ''
#         background_disabled_normal: 'seasoning.png'
#         pos: 150,520
#
#     Button:
#         background_normal: 'vegetables.png'
#         background_down: ''
#         background_disabled_normal: 'vegetables.png'
#         pos: 300,520
# Button:
#                 background_normal: 'wheat.png'
#                 background_down: ''
#                 background_disabled_normal: 'wheat.png'
#                 pos: 150,400
#
#             Button:
#                 background_normal: 'proteins.png'
#                 background_down: ''
#                 background_disabled_normal: 'proteins.png'
#                 pos: 300,400
#
# <cata>
#
#     Image:
#         source:'./bags (1).png'
#         pos_hint: {'top':1, 'left':1}
#
#
#
#     TextInput:
#         pos_hint: {'top':1, 'right':.95}
#         text: 'search'
#         size_hint: .3,.06
#         font_size:20
#         multiline: False
#
#     Button:
#         pos_hint: {'x':.5, 'right':1}
#         text: 'but2'
#         size_hint: .3,.5

