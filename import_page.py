from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from core.io import import_wallet as core_import_wallet
class ImportPage(Screen):
    def show_alert(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.title_label = Label(text='Kripto Wallet', font_size='28sp')
        self.description_label = Label(text='Enter your wallet name, seed, and password below to import an existing wallet.', font_size='16sp')
        self.wallet_name_input = TextInput(hint_text='Enter Wallet Name')
        self.wallet_seed_input = TextInput(hint_text='Enter Wallet Seed')
        self.wallet_password_input = TextInput(hint_text='Enter Wallet Password', password=True)
        button_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        self.create_button = Button(text='Import', size_hint_y=None, height=40)
        self.back_button = Button(text='Back', size_hint_y=None, height=40)

        self.create_button.bind(on_press=self.import_wallet)
        self.back_button.bind(on_press=self.go_to_start_page)
        button_layout.add_widget(self.create_button)
        button_layout.add_widget(self.back_button)

        spacer = Label(size_hint_y=None, height=20)  # Spacer with specific height

        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.description_label)
        self.layout.add_widget(spacer)
        self.layout.add_widget(self.wallet_name_input)
        self.layout.add_widget(self.wallet_seed_input)
        self.layout.add_widget(self.wallet_password_input)
        self.layout.add_widget(button_layout)

        self.add_widget(self.layout)

    def import_wallet(self, instance):
        wallet_name = self.wallet_name_input.text
        wallet_seed = self.wallet_seed_input.text
        wallet_password = self.wallet_password_input.text

        encrypted_seed = core_import_wallet(wallet_name, wallet_seed, wallet_password)

        if encrypted_seed:
            success_message = f'Wallet "{wallet_name}" imported successfully.'
            self.show_alert('Import Successful', success_message)
            self.manager.current = 'login'

        else:
            error_message = 'Failed to import wallet. Please check your seed and password.'
            self.show_alert('Import Failed', error_message)

   

    def go_to_start_page(self, instance):
        self.manager.current = 'start'
