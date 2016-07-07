#!/usr/bin/python

from rooms import *
from inventory import *
import textwrap
import sys
import pickle

class Command:
    input=""
    inventory= Inventory([])
    def __init__(self, input, inventory):
        self.input = input
        self.inventory = inventory
    def __str__(self):
        return self.input
    def inventory(self):
        return self.inventory
    def input(self):
        return self.input


class Game:
    room=Outside()
    inventory = Inventory([])

    def processCommand(self, command):
        #command = Command(commandAsString, self.inventory)

        if(command.startswith("save")):
            gameName=command[5:]
            pickle.dump( self, open( gameName+".savegame", "wb" ) )
            print "You saved the game called.. "+gameName

        if(command.startswith("load")):
            try:
                state = pickle.load( open( command[5:]+".savegame", "rb" ) )
                self.room=state.room
                print "Welcome Back!"
            except:
                print "Either your save doesn't exist, or you went into the pickle files for some reason."

        if("quit" in command):
            sys.exit("Quitter!\n")

        inventoryResponse = self.inventory.message(command)
        if(inventoryResponse.exists()):
            return inventoryResponse.getText()

        #response = self.room.message(Command(command, self.inventory))
        response = self.room.message(command)
        self.room = response.getRoom()
        #self.inventory = response.getInventory()
        return response.getText()

    def prompt(self):
        command = raw_input("> ")
        print textwrap.fill(self.processCommand(command),80, subsequent_indent='    ', initial_indent='    ',)

game = Game()
print "Hello!"
while True :
    game.prompt()
