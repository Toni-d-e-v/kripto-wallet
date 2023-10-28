from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock

class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)

        # Create layout elements
        self.title_label = Label(text='Settings', font_size=24)

        # Add a GridLayout to hold the "Reveal Seed" and "Back" buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=10, padding=10)
        self.reveal_seed_button = Button(text='Reveal Seed')
        self.back_button = Button(text='Back')
        button_layout.add_widget(self.reveal_seed_button)
        button_layout.add_widget(self.back_button)

        # Add widgets to the main layout
        self.add_widget(button_layout)

        # Bind button events
        self.reveal_seed_button.bind(on_press=self.show_secret_seed)
        self.back_button.bind(on_press=self.go_back)

    def show_secret_seed(self, instance):
        # Implement your code to reveal the secret seed here
        app = App.get_running_app()
        seed = app.decrypted_seed
        self.show_popup(seed)

    def show_popup(self, seed):
        # Create a popup to display the revealed secret seed
        content = BoxLayout(orientation='vertical', spacing=10)
        seed_label = Label(text=f'DO NOT SHARE THIS!', font_size=16, size_hint_y=None, height=44)
        copy_button = Button(text='Copy', size_hint_y=None, height=44, font_size=14)
        close_button = Button(text='Close', size_hint_y=None, height=44, font_size=14)

        # Bind events for the buttons
        copy_button.bind(on_press=lambda instance: self.copy_to_clipboard(seed, copy_button))
        close_button.bind(on_press=lambda instance: popup.dismiss())

        content.add_widget(seed_label)
        content.add_widget(copy_button)
        content.add_widget(close_button)

        popup = Popup(title='Secret Seed', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def copy_to_clipboard(self, text, copy_button):
        Clipboard.copy(text)
        print('Copied to clipboard:', text)
        copy_button.text = 'Copied'
        # Reset the button text after 1 second
        Clock.schedule_once(lambda dt: self.reset_button_text(copy_button), 1)

    def reset_button_text(self, copy_button):
        copy_button.text = 'Copy'

    def go_back(self, instance):
        self.manager.current = 'main'
