#!/usr/bin/python

from rooms import *
import textwrap

class Game:
    room=Outside()    
    def processCommand(self, command):
        response = self.room.message(command)
        self.room = response.getRoom()
        return response.getText()
        
    def prompt(self):
        command = raw_input("> ")
        print textwrap.fill(self.processCommand(command),80, subsequent_indent='    ', initial_indent='    ',)
     
game = Game()
print "Welcome!"
while True :
    game.prompt()
