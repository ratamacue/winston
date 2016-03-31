import unittest
from rooms import *

class TestStringMethods(unittest.TestCase):

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())
  
  def testDarkRoomHappyPath(self):
      response = DarkRoom().message("")
      self.assertEqual(response.getText(), 'The Door Is Open')

      response = response.getRoom().message("look around")
      self.assertEqual(response.getText(), 'You look around and notice, the room is dark..')

      response = response.getRoom().message("yes")
      self.assertEqual(response.getText(), 'The Door Is Open')

      response = response.getRoom().message("look down")
      self.assertEqual(response.getText(), 'You see a box of matches on your belt.')
      
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
      self.assertEqual(response.getText(), 'Masked man: Are you lost?')

      response = response.getRoom().message("dfuskjfhadsy")
      self.assertEqual(response.getText(), 'Masked man: Would you like some help?')
