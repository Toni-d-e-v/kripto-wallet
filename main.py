from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder  # Import Builder module
from kivytransitions.transitions import LinearBlur
from start_page import StartPage
from create_page import CreatePage
from import_page import ImportPage
from login_page import LoginPage
from main_page import MainPage

class KriptoWalletApp(App):
    decrypted_seed = "test"  # Initialize decrypted_seed as None
    def build(self):
        Builder.load_file('styles.kv')  # Load styles from styles.kv file

        
        screen_manager = ScreenManager()
        screen_manager.add_widget(StartPage(name='start'))
        screen_manager.add_widget(CreatePage(name='create'))
        screen_manager.add_widget(ImportPage(name='import'))
        screen_manager.add_widget(LoginPage(name='login'))
        screen_manager.add_widget(MainPage(name='main'))
        screen_manager.transition = LinearBlur(duration=0.2, direction="lr") #two available directions: "lr" and "rl"
        return screen_manager

if __name__ == '__main__':
    KriptoWalletApp().run()
