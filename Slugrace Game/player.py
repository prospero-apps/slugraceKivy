# File name: player.py

from kivy.properties import StringProperty, NumericProperty, ObjectProperty, BooleanProperty
from kivy.event import EventDispatcher

class Player(EventDispatcher):
    name = StringProperty('')
    initial_money = NumericProperty(0)  # amount of money the player starts with
    money = NumericProperty(0) # amount of money the player has at a particular time              
    money_before_race = NumericProperty(0)  # amount of money the player has before the race starts
    money_won = NumericProperty(0)  # amount of money won by the player in the race (negative if the player loses)
    bet = NumericProperty(1) # amount of money the player has put on their chosen slug    
    chosen_slug = ObjectProperty(None, allownone=True) # the slug the player bets on
    bankrupt = BooleanProperty(False)
    
    def update(self, winning_slug):
        self.money_before_race = self.money  
        self.money_won = (int(self.bet * (winning_slug.odds - 1)) if self.chosen_slug == winning_slug 
                          else -self.bet)  
        self.money += self.money_won

        # bankrupt check
        if self.money == 0:
            self.bankrupt = True

    def reset(self, gameover=False):
        self.chosen_slug = None     
        self.bet = 1

        if gameover:
            self.bankrupt = False

    
