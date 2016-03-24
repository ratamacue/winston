#!/usr/bin/python

from rooms import *

class Game:
    room=Outside()    
    def processCommand(self, command):
        response = self.room.message(command)
        self.room = response.getRoom()
        return response.getText()
        
    def prompt(self):
        command = raw_input("> ")
        print self.processCommand(command)
     
game = Game()
print "Welcome!"
while True :
    game.prompt()
