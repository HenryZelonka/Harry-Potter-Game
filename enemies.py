from random import randInt

class Enemy:
  hp = 0
  name = ""
  conditions = []
  strength = 0
  def __init__(self,hp,name,strength:
    self.hp = hp
    self.name = name
    self.strength = strength
  def fight(self):
    a = randInt(1,8)
      if self.strength >= a:
        conditions.remove("paralyzed")
        scroll("\n{} recovered from their paralysis.\n".format(self.name))
    if "paralyzed" not in self.conditions:
      a = randint(1,2) + self.strength
      scroll("{} attacks you dealing {} damage.".format(self.name,a))
      return a
    else:
      return 0
      