from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button

'''
class chatPage(GridLayout):
    def __init__(self, **kwargs):
        super(chatPage,self).__init__(**kwargs)
        self.cols =2
        self.add_widget(Label(text='History'))
        self.history = TextInput(multiline=False)
        self.add_widget(self.history)
        self.add_widget(Label(text='>'))
        self.send = TextInput(multiline=False)
        self.add_widget(self.send)
        
class chatApp(App):
    
    def build(self):
        return chatPage()
    
if __name__ == '__main__':
    chatApp.run()
    '''
    
    
class chatPage(GridLayout):

    def __init__(self, **kwargs):
        super(chatPage, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        
        self.history = Label(height=Window.size[1]*0.9,size_hint_y = None)
        self.add_widget(self.history)
        self.new_message = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        
        
        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)
        
        
class MyApp(App):

    def build(self):
        return chatPage()


if __name__ == '__main__':
    MyApp().run()