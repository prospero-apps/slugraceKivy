# File name: splash.py

import kivy
from kivy.uix.screenmanager import Screen, FadeTransition, SlideTransition
from kivy.clock import Clock

class SplashScreen(Screen):
    def on_enter(self):      
        Clock.schedule_once(self.move_on, 5)   

    def move_on(self, dt):
        self.game.transition = FadeTransition()
        self.game.current = 'settingsscreen'

    def on_leave(self):
        self.game.transition = SlideTransition()
        
