import unittest
import zoolandia

#################### Animal tests ####################

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_animal_creation(self):
    bob = zoolandia.Betta('Bob', 'orange')
    self.assertEqual(bob.name, 'Bob')
    self.assertEqual(bob.species.color, 'orange')
    self.assertIsInstance(bob.species, zoolandia.BettaTrifasciata)
    self.assertIsInstance(bob, zoolandia.Animal)
    self.assertIsInstance(bob.species, zoolandia.Species)

#################### Species tests ####################

class TestSpecies(unittest.TestCase):

  def test_commonname_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.common_name, '')

  def test_georegion_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.geo_region, '')

#################### Habitat tests ####################

class TestHabitat(unittest.TestCase):

  def test_name_empty_string_default(self):
    habitat = zoolandia.Habitat()
    self.assertEqual(habitat.name, '')

  def test_members_set_default(self):
    habitat = zoolandia.Habitat()
    self.assertIsInstance(habitat.members, set)

  def test_add_member(self):
    aquarium = zoolandia.Aquarium('freshwater')
    bob = zoolandia.Betta('Bob', 'orange')
    james = zoolandia.Betta('James', 'blue')
    aquarium.add_member(bob)
    self.assertIn(bob, aquarium.members)
    aquarium.add_member(james)
    self.assertIn(bob, aquarium.members)
    self.assertIn(james, aquarium.members)

  def test_remove_member(self):
    aquarium = zoolandia.Aquarium('freshwater')
    james = zoolandia.Betta('James', 'blue')
    aquarium.add_member(james)
    aquarium.remove_member(james)
    self.assertNotIn(james, aquarium.members)

#################### Movement class tests ####################

class TestWalking(unittest.TestCase):

  def test_legs_zero_default(self):
    walking = zoolandia.Walking()
    self.assertEqual(walking.legs, 0)

  def test_walk_speed_zero_default(self):
    walking = zoolandia.Walking()
    self.assertEqual(walking.walk_speed, 0)

class TestFlying(unittest.TestCase):

  def test_wings_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.wings, 0)

  def test_wingspan_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.wingspan, 0)

  def test_air_speed_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.air_speed, 0)

class TestSwimming(unittest.TestCase):

  def test_appendages_false_default(self):
    swimming = zoolandia.Swimming()
    self.assertFalse(swimming.fins)
    self.assertFalse(swimming.flippers)
    self.assertFalse(swimming.web_feet)

  def test_swim_speed_zero_default(self):
    swimming = zoolandia.Swimming()
    self.assertEqual(swimming.swim_speed, 0)

  def test_swim_speed_zero_default(self):
    swimming = zoolandia.Swimming()
    self.assertEqual(swimming.swim_speed, 0)

if __name__ == '__main__':
  unittest.main()
