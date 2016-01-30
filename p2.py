class enemy:
   eneCount = 0

   def __init__(self, name, level):
      self.name = name
      self.level = level
      enemy.eneCount += 1
   
   def displayCount(self):
     print "Total enemy %d" % enemy.eneCount

   def displayenemy(self):
      print self.name, "Level:", self.level
This
" would create first object of enemy class"
ene2 = enemy("Mug", 2)
"This would create second object of enemy class"
ene5 = enemy("Truck", 5)
ene2.displayenemy()
ene5.displayenemy()
print "Total enemies %d" % enemy.eneCount