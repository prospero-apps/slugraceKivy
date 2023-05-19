# File name: test.py

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
     
class TestLayout(BoxLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music = SoundLoader.load('assets/Sounds/Game/Background Music.mp3')
        
    def toggle_music(self):
        if self.music.state == 'play':
            self.music.stop()
        else:
            self.music.play()

    def change_volume(self, value):
        self.music.volume = value

class TestApp(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    TestApp().run()

