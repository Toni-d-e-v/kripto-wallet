from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from core.io import create_wallet as core_create_wallet, get_wallets as core_get_wallets
from kivy.uix.popup import Popup

class CreatePage(Screen):
    def show_alert(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.title_label = Label(text='Kripto Wallet', font_size='28sp')
        self.description_label = Label(text='Enter your wallet name and password below to create a new wallet.', font_size='16sp')
        self.wallet_name_input = TextInput(hint_text='Enter Wallet Name')
        self.wallet_password_input = TextInput(hint_text='Enter Wallet Password', password=True)
        self.create_button = Button(text='Create', size_hint_y=None, height=40)
        self.back_button = Button(text='Back', size_hint_y=None, height=40)
        button_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        self.create_button.bind(on_press=self.create_wallet)
        self.back_button.bind(on_press=self.go_to_start_page)

        spacer = Label(size_hint_y=None, height=20)  # Spacer with specific height

        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.description_label)
        self.layout.add_widget(spacer)
        self.layout.add_widget(self.wallet_name_input)
        self.layout.add_widget(self.wallet_password_input)

        button_layout.add_widget(self.create_button)
        button_layout.add_widget(self.back_button)
        self.layout.add_widget(button_layout)

        self.add_widget(self.layout)

    def create_wallet(self, instance):
        wallet_name = self.wallet_name_input.text
        wallet_password = self.wallet_password_input.text

        existing_wallets = core_get_wallets()
        if wallet_name in existing_wallets:
            print(f'Wallet "{wallet_name}" already exists. Please choose a different name.')
            self.show_alert('Create Failed', f'Wallet "{wallet_name}" already exists. Please choose a different name.')

        else:
            # Create wallet using core.io's create_wallet function
            core_create_wallet(wallet_name, wallet_password)
            print(f'Wallet created with name: {wallet_name}')
            self.show_alert('Create Successful', f'Wallet created with name: {wallet_name}')

            self.manager.current = 'login'

    def go_to_start_page(self, instance):
        self.manager.current = 'start'
