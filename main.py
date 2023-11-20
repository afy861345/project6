from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

Window.clearcolor=(100/255,0,0,0)
Window.size=(400,600)
class Myapp3(App):
    def build(self):
        self.title=("Ali [FIRST APP]")
        txt=TextInput(
            text=("enter"),
            multiline=False,
            font_size=32,
            pos_hint={'x':0.1,'y':0.1},
            size_hint=(0.5,0.05)
        )
        return txt   
if __name__=="__main__":
    Myapp3().run()