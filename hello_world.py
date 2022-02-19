import kivy
from kivy.app import App
from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello World!', size=self.texture_size)


if __name__ == '__main__':
    HelloWorldApp().run()







