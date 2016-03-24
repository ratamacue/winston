import unittest
from rooms import *

class TestStringMethods(unittest.TestCase):

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())
  
  def testDarkRoom(self):
      response = DarkRoom().message("light match")
      self.assertEqual(response.getText(), 'The match lights up for 5 seconds, in that time a sign ahead of you reads "look behind you" \n Look behind you? (Yes/No)')

