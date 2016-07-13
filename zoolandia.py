########## Animals ##########

class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.locomotion = set()

  def add_locomotion(self, loco):
    self.locomotion.add(loco)

  def remove_locomotion(self, loco):
    self.locomotion.discard(loco)

class Betta(Animal):

  def __init__(self, name, color):
    Animal.__init__(self, name, BettaTrifasciata(color))


########## Species ##########

class Species:

  def __init__(self):
    self.common_name = ''
    self.geo_region = ''

class BettaTrifasciata(Species):

  def __init__(self, color):
    self.color = color
    self.common_name = 'Betta'
    self.geo_region = 'Asia'

########## Movement classes ##########

class Walking:

  def __init__(self):
    self.legs = 0
    self.walk_speed = 0

class Flying:

  def __init__(self):
    self.wings = 0
    self.wingspan = 0
    self.air_speed = 0

class Swimming:

  def __init__(self):
    self.fins = False
    self.flippers = False
    self.web_feet = False
    self.swim_speed = 0


########## Habitat ##########

class Habitat:

  def __init__(self):
    self.name = ''
    self.members = set()

  def add_member(self, member):
    self.members.add(member)

  def remove_member(self, member):
    self.members.discard(member)

class Aquarium(Habitat):

  def __init__(self, water_type):
    Habitat.__init__(self)
    self.water_type = ''
