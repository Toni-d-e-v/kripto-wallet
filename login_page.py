from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from core.io import create_wallet, load_wallet, get_wallets
from kivy.app import App  # Import App class
from kivy.uix.popup import Popup


class LoginPage(Screen):
    def show_alert(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        # Drop-down selection
        self.wallet_selection = Button(text='Select Wallet', size_hint_y=0.15,size_hint_x=0.15, height=40 , padding=(10, 10, 10, 10))
        self.wallet_dropdown = DropDown()
        self.add_wallet_options(self.wallet_dropdown)  # Add options to the dropdown
        self.wallet_selection.bind(on_release=self.wallet_dropdown.open)
        self.wallet_dropdown.bind(on_select=lambda instance, x: setattr(self.wallet_selection, 'text', x) )

        # Other UI elements
        self.title_label = Label(text='Kripto Wallet', font_size='28sp')
        self.password_input = TextInput(hint_text='Enter Password', password=True)

        self.login_button = Button(text='Login', size_hint_y=None, height=40)
        self.back_button = Button(text='Back', size_hint_y=None, height=40)
        button_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.wallet_selection)
        self.layout.add_widget(self.password_input)
        button_layout.add_widget(self.login_button)
        button_layout.add_widget(self.back_button)
        self.layout.add_widget(button_layout)

        self.login_button.bind(on_press=self.check_credentials)
        self.back_button.bind(on_press=self.back)

        self.add_widget(self.layout)


    def add_wallet_options(self, dropdown):
        def update_wallet_options(instance):
            wallet_options = get_wallets()  # Use the get_wallets() function from io.py
            dropdown.clear_widgets()  # Clear existing widgets in the dropdown
            for option in wallet_options:
                btn = Button(text=option, size_hint_y=None, height=40)
                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
                dropdown.add_widget(btn)

        self.wallet_selection.bind(on_release=update_wallet_options)  # Bind the update_wallet_options function to dropdown release event

    def check_credentials(self, instance):


        global decrypted_seed
        decrypted_seed = None  # Clear decrypted_seed variable before attempting to load a new wallet
        selected_wallet = self.wallet_selection.text
        password = self.password_input.text
        try:
            decrypted_seed = load_wallet(selected_wallet, password)

            if decrypted_seed:
                print('Login successful')
                app = App.get_running_app()
                
                app.decrypted_seed = decrypted_seed  # Set decrypted_seed attribute in the App class
                self.password_input.text = ''
                self.manager.current = 'main'  # Navigate to the main screen

            else:
                print('Login failed. Please check your credentials.')
                self.show_alert('Login Failed', "Please check your credentials.")

        except Exception as e:
            print('Login failed. Please check your credentials.')
            self.show_alert('Login Failed', "Please check your credentials.")

            print(e)  # Print the specific error for debugging purposes


    def back(self, instance):
        # Implement logic to handle back button press
        print('Back button pressed')
        self.manager.current = 'start'  # Navigate to the start screen
