from screenStuff import *
from random import randint

#class for a spell
class Spell:
  #name forn the spell
  name = ""
#class for petrificus totalus
class Petri(Spell):
  name = "Petrificus Totalus"
  def effects(x,a):
    b = randint(1,8)
    if a >= b:
      scroll("\nYou have paralyzed your opponent!\n")
      return[0,"paralyzed"]
    else:
      scroll("Your spell missed!")
      return[0,""]

class Wing(Spell):
  name = "Wingardium Leviosa"
  def effects(x,a):
    b = randint(1,3)
    if a >= b:
      scroll("\nYou lift your opponent in the air, then drop them!\n")
      scroll("This causes them to to take {} damage!\n".format(a))
      return[a+randint(-1,2),""]
    else:
      scroll("\nYour spell missed!\n")
      return[0,""]


    
