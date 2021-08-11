import requests
import wikipedia
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('frontend.kv')


class Wiki:
    def find_image_url(self, query):
        page = wikipedia.page(query)
        return page.images[0]


class Download:
    def download_image(self, url) -> bytes:
        return requests.get(url).content


class FirstScreen(Screen):
    def get_image_url(self):
        query = self.manager.current_screen.ids.txt.text
        image_url = Wiki().find_image_url(query)
        print(image_url)
        return image_url

    def get_image(self):
        image_path = 'resources/image2.jpg'
        image = Download().download_image(self.get_image_url())
        print(image)
        with open(image_path, 'wb') as file:
            file.write(image)
        return image

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.get_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
