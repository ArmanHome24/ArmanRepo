import time

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        current_time = time.strftime('%y%m%d-%H%M%S')
        file_path = f"./resources/{current_time}.png"
        self.ids.camera.export_to_png(file_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = file_path


class ImageScreen(Screen):
    """ I did not implement all functionalities
     """
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__()
        self.file_path = ''

    def create_link(self):
        self.file_path = self.ids.img.source
        self.ids.lbl_link.text = self.file_path

    def copy_link(self):
        Clipboard.copy(self.file_path)

    def open_link(self):
        webbrowser.open(self.file_path)


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
