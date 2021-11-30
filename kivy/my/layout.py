from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


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
        
    def sendMessage(self,_):
        message = self.new_message.text
        self.new_message.text=""
        if message:
            self.history.updateChat(f"[color=20dddd]>:[/color] {message}")
            
                
    def historyMessage(self, username, message):
        self.history.updateChat(
            f"[color=20dd20]{username}[/color] [color=20dddd]>:[/color] {message}")


class MyApp(App):

    def build(self):
        return chatPage()


if __name__ == '__main__':
    MyApp().run()