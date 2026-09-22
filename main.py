import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        # Safe structural UI definitions
        self.lbl = Label(
            text="App Compiled Successfully!", 
            font_size='24sp',
            size_hint=(1, 0.7)
        )
        self.btn = Button(
            text="Click Me", 
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.btn.bind(on_press=self.on_button_click)
        
        self.add_widget(self.lbl)
        self.add_widget(self.btn)

    def on_button_click(self, instance):
        self.lbl.text = "Hello from Android!"

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
        
