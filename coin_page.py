from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import random
from coin import get_address_balance, send_crypto
from kivy.app import App  # Import App class
from kivy.uix.popup import Popup


class CoinPage(Screen):
    def __init__(self, coin_name, coin_symbol, **kwargs):
        super(CoinPage, self).__init__(**kwargs)
        self.coin_symbol = coin_symbol
        self.balance, self.address = self.gen_address_balance()
        # Coin name label
        coin_name_label = Label(text=f'Coin Name: {self.coin_symbol}', font_size=18, size_hint_y=None, height=50)

        # Address and Balance labels aligned horizontally
        address_balance_layout = BoxLayout(size_hint_y=None, height=50, spacing=20)
        address_label = TextInput(text=f'{self.balance}', readonly=True, size_hint_x=0.7)
        balance_label = TextInput(text=f'{self.address} {self.coin_symbol}', readonly=True, size_hint_x=0.3)


        address_balance_layout.add_widget(address_label)
        address_balance_layout.add_widget(balance_label)

        # Send Form section
        send_form_layout = BoxLayout(orientation='vertical', spacing=10)
        send_to_input = TextInput(hint_text='Recipient Address')
        amount_input = TextInput(hint_text='Amount')
        send_button = Button(text='Send', size_hint_y=None, height=40)

        def send_callback(instance):
            recipient_address = send_to_input.text
            amount = amount_input.text
            print(f"Recipient Address: {recipient_address}")
            print(f"Amount: {amount}")
            symbol = self.coin_symbol
            app = App.get_running_app()
            seed = app.decrypted_seed 
            amount = amount_input.text
            try:
                txid = send_crypto(symbol, seed, recipient_address, amount)
                success_message = f"Transaction Successful! TXID: {txid}"
                popup_content = BoxLayout(orientation='vertical')
                popup_content.add_widget(Label(text=success_message))
                copy_button = Button(text='Copy TXID', size_hint_y=None, height=40)
            except Exception as e:
                error_message = f"Error: {str(e)}"
                popup = Popup(title='Error', content=Label(text=error_message), size_hint=(None, None), size=(400, 200))
                popup.open()

        send_button.bind(on_press=send_callback)
        send_form_layout.add_widget(send_to_input)
        send_form_layout.add_widget(amount_input)
        send_form_layout.add_widget(send_button)

        # Back button
        back_button = Button(text='Back', size_hint_y=None, size_hint_x=None, height=40, width=80)

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        main_layout.add_widget(coin_name_label)
        main_layout.add_widget(address_balance_layout)
        main_layout.add_widget(send_form_layout)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

        # Bind the back button to the go_back method
        back_button.bind(on_press=self.go_back)


    def gen_address_balance(self):
        symbol = self.coin_symbol
        app = App.get_running_app()
        seed = app.decrypted_seed 
        return get_address_balance(symbol,seed)

    def go_back(self, instance):
        self.manager.current = 'main'
