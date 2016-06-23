import unittest
from rooms import *
from inventory import *

# python -m unittest -v tests


class TestStringMethods(unittest.TestCase):

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def testDarkRoomHappyPath(self):
      response = DarkRoom().message("")
      self.assertEqual(response.getText(), 'The door is open.')

      response = response.getRoom().message("look around")
      self.assertEqual(response.getText(), 'You look around and notice, the room is dark..')

      response = response.getRoom().message("yes")
      self.assertEqual(response.getText(), 'The door is open.')

      response = response.getRoom().message("look down")
      self.assertEqual(response.getText(), 'You see a box of matches on the stone floor, you picked up the matches (Hint: "light _____")')

      response = response.getRoom().message("light match")
      self.assertEqual(response.getText(), 'The match lights up for 5 seconds, in that time a sign ahead of you reads "look behind you" \n Look behind you? (Yes/No)')

      response = response.getRoom().message("look around")
      self.assertEqual(response.getText(), 'A sign ahead of you reads "look behind you" \n Look behind you? (Yes/No)')

      response = response.getRoom().message("yes")
      self.assertEqual(response.getText(), 'Behind you and behind the open door there is another door. Under the crack of the door you can see light, enter the door? (Yes/No)')

      response = response.getRoom().message("THIS IS NOT A REAL COMMAND")
      self.assertEqual(response.getText(), 'Under the crack of the door you can see light, enter the door? (Yes/No)')

      response = response.getRoom().message("yes")
      self.assertEqual(response.getText(), 'The room is light and there are people,')
      self.assertTrue(isinstance(response.getRoom(), BaseRoom))


      #self.assertEqual(response.getText(), 'The match lights up for 5 seconds, in that time a sign ahead of you reads "look behind you" \n Look behind you? (Yes/No)')

  def testBaseRoomHappyPath(self):
      response = BaseRoom().message("")
      self.assertEqual(response.getText(), 'You have reached the base.')

      response = response.getRoom().message("look around")
      self.assertEqual(response.getText(), 'There is a tall skinny man with a mask on.')

      response = response.getRoom().message("fdkdfwsj")
      self.assertEqual(response.getText(), 'Masked Man: Are you lost?')

      response = response.getRoom().message("dfuskjfhadsy")
      self.assertEqual(response.getText(), 'Masked Man: Would you like some help?')

      response = response.getRoom().message("fdkdfwsj")
      self.assertEqual(response.getText(), 'Masked Man: Do you know what you\'re doing? (Yes/No)')

      response = response.getRoom().message("no")
      self.assertEqual(response.getText(), 'Ok, here is an explanation.. typing look (Up or down) will look in that direction the, most common command you will use is "look around" (Use look around too see sorroundings from left to right) ...   Next open (Insert any object here) will open things, sorry for you getting a tutorial now.. It took probably 30 minutes to figure out how to open a door, now finally try typing "inventory" to see what you have on you (type use, info, or remove to interact with your items) .........  And lastly, write "save" (game save name of your choice) and then type "load" (saved game) .... Do you want me to take you to the market? They have different stores for potions, all of the generic RPG items you can buy! (Yes/No)')

      response1 = response.getRoom().message("no")
      self.assertEqual(response1.getText(), "Alright, then I'll be on my way.  You'll probably be lost, AND YOU HAVE NO FRIENDS.. AND I DON'T LIKE YOU.")

      response = response.getRoom().message("yes")
      self.assertEqual(response.getText(), 'Masked Man: Alright, well I am not taking you there but it will give you directions, take a left a right, go forward, turn back, then take 2 lefts, and a right then go 1 mile forward.. And you should be able to find the shop, ok good luck!')

      response = response.getRoom().message("anything")
      #self.assertEqual(response.getText(), 'Masked Man: Alright, well I am not taking you there but it will give you directions, take a left a right, go forward, turn back, then take 2 lefts, and a right then go 1 mile forward.. And you should be able to find the shop, ok good luck!')




  def testBaseRoomNoHelp(self):
      response = BaseRoom().message("")
      self.assertEqual(response.getText(), 'You have reached the base.')

      response = response.getRoom().message("look around")
      self.assertEqual(response.getText(), 'There is a tall skinny man with a mask on.')

      response = response.getRoom().message("fdkdfwsj")
      self.assertEqual(response.getText(), 'Masked Man: Are you lost?')

      response = response.getRoom().message("dfuskjfhadsy")
      self.assertEqual(response.getText(), 'Masked Man: Would you like some help?')

      response = response.getRoom().message("fdkdfwsj")
      self.assertEqual(response.getText(), 'Masked Man: Do you know what you\'re doing? (Yes/No)')

      response = response.getRoom().message("yes")
      self.assertEqual(response.getText(), "Tutorial Guy (Your only chance to figure out how to play this game): Ok then, bye..\n I'll just go, also I'm not just a masked man I'm a generic tutorial person")
      self.assertTrue(isinstance(response.getRoom(), Hahaverycleverroomname))

  def testhahaverycleverroomnameHappyPath(self):
    response = Hahaverycleverroomname().message("Eat an apple")
    self.assertEqual(response.getText(), "Unless you know what you're doing, or the tutorial guy helped you.  You are stuck,")
    response = response.getRoom().message('look around')
    self.assertEqual(response.getText(), "???: Hi there!")

    response = response.getRoom().message('gdfhachx')
    self.assertEqual(response.getText(), "???: Now, you seem to be lost.. That other guy is pretty mean huh?")

  def testThatICanListMyInventory(self):
      response = Inventory().message("inventory")
      self.assertEqual(response.getText(), "You don't have anything yet.")

  def testThatICanListMyInventory(self):
      inventory = Inventory([])
      response = inventory.message("inventory")
      self.assertEqual(response.getText(), "You don't have anything yet.")

      inventory = Inventory(["baseball"])
      response = inventory.message("inventory")
      self.assertEqual(response.getText(), "You have the following things in your inventory: \n * baseball")

      inventory = Inventory(["baseball", "cupcake"])
      response = inventory.message("inventory")
      self.assertEqual(response.getText(), "You have the following things in your inventory: \n * baseball \n * cupcake")

      inventory = Inventory(["baseball", "cupcake", "donkey"])
      response = inventory.message("inventory")
      self.assertEqual(response.getText(), "You have the following things in your inventory: \n * baseball \n * cupcake \n * donkey")
