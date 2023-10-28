from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.app import App
from coin_page import CoinPage
from settings_page import SettingsPage
from config import version
from kivy.base import EventLoop
import uuid



# Assuming Coin class has a name, symbol, color, and data attribute
class Coin:
    def __init__(self, name, symbol, color):
        self.name = name
        self.symbol = symbol
        self.color = color

class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=(20, 50, 20, 50))

        layout.bind(minimum_height=layout.setter('height'))
        scroll_view = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        # Add balance label with gray background
        balance_label = Label(text='KriptoWallet - Free and open-source!', size_hint_y=None, height=40)
        layout.add_widget(balance_label)

        coins = [
            Coin("Bitcoin", "BTC", (1, 0.647, 0, 0.3)),  # Orange color
            Coin("Bitcoin TEST", "BTCT", (1, 0.647, 0, 0.3)),  # Orange color
            Coin("Ethereum", "ETH", (0, 0, 0.545, 0.3)),  # Dark blue color
            # Coin("Litecoin", "LTC", (0.502, 0.502, 0.502, 0.3)),  # Gray color
            # Coin("BinanceSC", "BSC", (1, 1, 0, 0.3)),  # Yellow color
            # Coin("Tron", "TRX", (1, 0, 0, 0.3)),  # Red color
            # Coin("Monero", "XMR", (1, 0.447, 0, 0.3)),  # Orange color

        ]

        for coin in coins:
            coin_button = Button(text=f'{coin.name} ({coin.symbol})', size_hint_y=None, height=40, background_color=coin.color)
            coin_button.bind(on_release=lambda btn, coin=coin: self.on_coin_button_click(coin))
            layout.add_widget(coin_button)

        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)

        # Add settings and logout buttons
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, padding=(10, 10, 10, 10), size_hint_y=None, height=50)
        settings_button = Button(text='Settings', size_hint_x=None, width=100)
        logout_button = Button(text='Logout', size_hint_x=None, width=100)
        settings_button.bind(on_release=self.on_settings_button_click)
        logout_button.bind(on_release=self.on_logout_button_click)
        buttons_layout.add_widget(settings_button)
        buttons_layout.add_widget(logout_button)
        self.add_widget(buttons_layout)

        # Add label at the left bottom corner
        bottom_label = Label(text=f'KriptoWallet', size_hint=(None, None), pos=(4, 5))
        bottom_label_1 = Label(text=f'v{version}', size_hint=(None, None), pos=(65, 5))

        self.add_widget(bottom_label)
        self.add_widget(bottom_label_1)

    def on_coin_button_click(self, coin):
        screen_name = str(uuid.uuid4())  # Generate a random screen name
        coin_page = CoinPage(coin_name=coin.name, coin_symbol=coin.symbol, name=screen_name)
        self.manager.add_widget(coin_page)
        self.manager.current = screen_name  # Switch to the CoinPage using the random screen name

    def on_settings_button_click(self, instance):
        print('Settings button clicked.')  # Replace this with your settings logic
        screen_name = str(uuid.uuid4())  # Generate a random screen name
        sp = SettingsPage(name=screen_name)
        self.manager.add_widget(sp)
        self.manager.current = screen_name  # Switch to the CoinPage using the random screen name
    def on_logout_button_click(self, instance):
        global decrypted_seed
        decrypted_seed = None  # Clear decrypted_seed variable when logging out
        self.manager.transition.direction = 'rl'  # Set transition direction (optional)
        self.manager.current = 'login'  # Navigate to the login screen

class CryptoWalletApp(App):
    def build(self):
        root = Screen()
        main_page = MainPage(name='main')
        root.add_widget(main_page)
        return root

if __name__ == '__main__':
    CryptoWalletApp().run()
