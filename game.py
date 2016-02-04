#!/usr/bin/python

class Game:
    doorOpen=False
    def message(self, command):
        #Here is where we are dealing with what they typed and channging state
        if("open door" in command):
            self.doorOpen=True            
       

        #Here is where we show a message based on the state.
        if (self.doorOpen == True):
            if ("look around" in command):
                return "You look around and notice, the room is dark.."
            if ("look down" in command):
                return "You see a box of matches on your belt."   

            return "The Door Is Open"
        
        return 'You are at a door.'
        
    def prompt(self):
        command = raw_input("> ")
        print self.message(command)


game = Game()
print "Welcome!"
while True :
    game.prompt()
