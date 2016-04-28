import unittest
from rooms import *


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
      self.assertEqual(response.getText(), 'Ok, here is an explanation.. typing look (Up or down) will look in that direction the, most common command you will use is "look around" (Use look around too see sorroundings from left to right) ...   Next open (Insert any object here) will open things, sorry for you getting a tutorial now.. It took probably 30 minutes to figure out how to open a door, now finally try typing "inventory" to see what you have on you (type use, info, or remove to interact with your items) ......... Now finally do you want me to take you to the market? They have different stores for potions, all of the generic RPG items you can buy! ')


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
    response = Hahaverycleverroomname().message('')
    self.assertEqual(response.getText(), "???: Hi there!")
