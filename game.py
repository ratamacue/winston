#!/usr/bin/python

from rooms import *
import textwrap
import sys
import pickle


class Game:
    room=Outside()

    def processCommand(self, command):

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
            sys.exit("You are leaving the game.")


        response = self.room.message(command)
        self.room = response.getRoom()
        return response.getText()

    def prompt(self):
        command = raw_input("> ")
        print textwrap.fill(self.processCommand(command),80, subsequent_indent='    ', initial_indent='    ',)

game = Game()
print "Hello!"
while True :
    game.prompt()
