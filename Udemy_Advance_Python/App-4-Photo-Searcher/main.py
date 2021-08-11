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
    def search_image(self):
        image_path = 'resources/image2.jpg'
        query = self.manager.current_screen.ids.txt.text
        image_url = Wiki().find_image_url(query)
        image = Download().download_image(image_url)
        print(image)
        print(image_url)

        with open(image_path, 'wb') as file:
            file.write(image)

        self.manager.current_screen.ids.img.source = image_path


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
