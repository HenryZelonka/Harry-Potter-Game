#imports
from spells import *

#class for a wizard
class Wizard:
  #hitpoints
  hp = 0
  #strength
  strength = 0
  #spells
  spells = []
  stars = 1
  starLimit = 0

#class for harry potter
class Harry(Wizard):
  def describe(self):
    scroll("\nHarry Potter(regular)")
    scroll("\nStars:{}/{}\n".format(self.stars,self.starLimit))
    scroll("Spells: ")
    for x in self.spells:
      scroll(x.name + "   ")
    print("\n")
  #constructor
  def __init__(self):
    self.starLimit = 5
    #setting default hitpoints
    self.hp = 10
    #setting default strength
    self.strength = 2
    #setting spells
    self.spells =[Petri(),Wing()]