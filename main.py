from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WalletApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        box.add_widget(Label(text='My Wallet App', font_size=30))
        box.add_widget(Label(text='Balance: $ 0.00', font_size=24))
        box.add_widget(Button(text='Add Money', size_hint=(1,0.2)))
        box.add_widget(Button(text='Send Money', size_hint=(1,0.2)))
        return box

WalletApp().run()
