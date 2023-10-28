from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class StartPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = BoxLayout(orientation='vertical')

        self.title_label = Label(text='Kripto Wallet', font_size='28sp')
        button_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        self.create_button = Button(text='Create Wallet', size_hint_y=None, height=40)
        self.import_button = Button(text='Import Wallet', size_hint_y=None, height=40)
        self.login_button = Button(text='Login', size_hint_y=None, height=40)
        self.create_button.bind(on_press=self.go_to_create_page)
        self.import_button.bind(on_press=self.go_to_import_page)
        self.login_button.bind(on_press=self.go_to_login)
        button_layout.add_widget(self.create_button)
        button_layout.add_widget(self.import_button)
        button_layout.add_widget(self.login_button)

        self.layout.add_widget(Label())  # Spacer
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(Label())  # Spacer
        self.layout.add_widget(button_layout)  # Add the horizontal button layout
        self.add_widget(self.layout)

    
    def go_to_create_page(self, instance):
        self.manager.current = 'create'
    def go_to_import_page(self, instance):
        self.manager.current = 'import'
    def go_to_login(self, instance):
        self.manager.current = 'login'