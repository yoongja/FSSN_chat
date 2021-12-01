from os import name
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.uix.widget import Widget

import client

class FirtstScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cols = 2
        
        self.add_widget(Label(text="kivy"))
        self.add_widget(Label(text="chatting"))
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.add_widget(self.username)
        
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)
        
    def join_button(self,instance):
        username = self.username.text
        info = f"Welcome kiby chatting app as {username}"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = 'Info'
        Clock.schedule_once(self.connect, 3)
        
    def connect(self, _):
        
        username = self.username.text

        chat_app.create_chat_page()
        chat_app.screen_manager.current = "Chat"
        
class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
        
    def update_info(self, message):
        self.message.text = message
        
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

class Scroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)
        self.chatHistory = Label(size_hint_y=None, markup=True)
        self.scroll = Label()
        self.layout.add_widget(self.chatHistory)
        self.layout.add_widget(self.scroll)
        
    def updateChat(self, message):

        self.chatHistory.text += '\n' + message    
        self.layout.height = self.chatHistory.texture_size[1] + 15
        self.chatHistory.height = self.chatHistory.texture_size[1]
        self.chatHistory.text_size = (self.chatHistory.width * 0.98, None)
        self.scroll_to(self.scroll)
        
        
class chatPage(GridLayout):

    def __init__(self, **kwargs):
        super(chatPage, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        
        self.history = Scroll(height=Window.size[1]*0.9,size_hint_y = None)
        self.add_widget(self.history)
        self.new_message = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.sendMessage)
        
        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)
        client.connect()
        client.startlistening(self.commingMessage)
        
    def sendMessage(self,_):
        message = self.new_message.text
        self.new_message.text=""
        if message:
            self.history.updateChat(f"[color=7e4a8f]send:[/color] {message}")
        client.send(message)    
                
    def commingMessage(self,message):
        self.history.updateChat(f"[color=20dddd]recieve:[/color] {message}")

class connectApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.first_screen = FirtstScreen()
        screen = Screen(name="first")
        screen.add_widget(self.first_screen)
        self.screen_manager.add_widget(screen)
        
    
        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        
        return self.screen_manager
    
    def create_chat_page(self):
        self.chat_page = chatPage()
        screen = Screen(name="Chat")
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)
        


if __name__ == '__main__':
    chat_app = connectApp()
    chat_app.run()    
        