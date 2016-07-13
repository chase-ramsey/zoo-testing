import unittest
from zoolandia import *

#################### Animal tests ####################

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.swim = Swimming()
    self.walk = Walking()
    self.bob = Betta('Bob', 'orange')

  def test_animal_creation(self):
    self.assertEqual(self.bob.name, 'Bob')
    self.assertEqual(self.bob.species.color, 'orange')
    self.assertIsInstance(self.bob.species, BettaTrifasciata)
    self.assertIsInstance(self.bob, Animal)
    self.assertIsInstance(self.bob.species, Species)

  def test_locomotion_initialization(self):
    self.assertIsInstance(self.bob.locomotion, set)
    self.assertEqual(0, len(self.bob.locomotion))

  def test_add_locomotion(self):
    bob = Betta('Bob', 'orange')
    swim = Swimming()
    bob.add_locomotion(swim)
    self.assertIn(swim, bob.locomotion)

  def test_remove_locomotion(self):
    bob = Betta('Bob', 'orange')
    swim = Swimming()
    walk = Walking()
    bob.add_locomotion(swim)
    bob.add_locomotion(walk)
    bob.remove_locomotion(swim)
    self.assertNotIn(swim, bob.locomotion)
    self.assertIn(walk, bob.locomotion)

#################### Species tests ####################

class TestSpecies(unittest.TestCase):

  def test_commonname_empty_string_default(self):
    species = Species()
    self.assertEqual(species.common_name, '')

  def test_georegion_empty_string_default(self):
    species = Species()
    self.assertEqual(species.geo_region, '')

#################### Habitat tests ####################

class TestHabitat(unittest.TestCase):

  def test_name_empty_string_default(self):
    habitat = Habitat()
    self.assertEqual(habitat.name, '')

  def test_members_set_default(self):
    habitat = Habitat()
    self.assertIsInstance(habitat.members, set)

  def test_add_member(self):
    aquarium = Aquarium('freshwater')
    bob = Betta('Bob', 'orange')
    james = Betta('James', 'blue')
    aquarium.add_member(bob)
    self.assertIn(bob, aquarium.members)
    aquarium.add_member(james)
    self.assertIn(bob, aquarium.members)
    self.assertIn(james, aquarium.members)

  def test_remove_member(self):
    aquarium = Aquarium('freshwater')
    james = Betta('James', 'blue')
    aquarium.add_member(james)
    aquarium.remove_member(james)
    self.assertNotIn(james, aquarium.members)

#################### Movement class tests ####################

class TestWalking(unittest.TestCase):

  def test_legs_zero_default(self):
    walking = Walking()
    self.assertEqual(walking.legs, 0)

  def test_walk_speed_zero_default(self):
    walking = Walking()
    self.assertEqual(walking.walk_speed, 0)

class TestFlying(unittest.TestCase):

  def test_wings_zero_default(self):
    flying = Flying()
    self.assertEqual(flying.wings, 0)

  def test_wingspan_zero_default(self):
    flying = Flying()
    self.assertEqual(flying.wingspan, 0)

  def test_air_speed_zero_default(self):
    flying = Flying()
    self.assertEqual(flying.air_speed, 0)

class TestSwimming(unittest.TestCase):

  def test_appendages_false_default(self):
    swimming = Swimming()
    self.assertFalse(swimming.fins)
    self.assertFalse(swimming.flippers)
    self.assertFalse(swimming.web_feet)

  def test_swim_speed_zero_default(self):
    swimming = Swimming()
    self.assertEqual(swimming.swim_speed, 0)

  def test_swim_speed_zero_default(self):
    swimming = Swimming()
    self.assertEqual(swimming.swim_speed, 0)

if __name__ == '__main__':
  unittest.main()
