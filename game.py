#!/usr/bin/python

class Outside:
    def message(self, command):
        if("open door" in command):
            return Response(DarkRoom(), "You Open The Door")    
        return Response(self, "You are at a door.")  

class DarkRoom:
    haveWeLookedAround=False
    matchLit=False    
    def message(self, command):
        if (self.matchLit):
            if(self.haveWeLookedAround):
                if("yes" in command):
                    return Response(BaseRoom(),"The room is light and there are people,")
            if ("yes" in command):
                self.haveWeLookedAround=True            
                return Response(self, "Behind you and behind the open door there is another door. Under the crack of the door you can see light, enter the door? (Yes/No)")
            return Response(self, "The room is light and there are people,")
        if ("look around" in command):
            return Response(self, "You look around and notice, the room is dark..")
        if ("look down" in command):
            return Response(self, "You see a box of matches on your belt.")
        if ("light match" in command):
            self.matchLit=True
            return Response(self, "The match lights up for 5 seconds, in that time a sign ahead of you reads \"look behind you\" \n Look behind you? (Yes/No)")
        return Response(self, "The Door Is Open")

class BaseRoom:
    def message(self, command):
        return Response(self, "You have reached the base.")

class Response:
    room = Outside()    
    text = "This text shoul never show up."
    def __init__(self, room, text):
        self.room = room
        self.text = text    
    def getRoom(self):
        return self.room
    def getText(self):
        return self.text

class Game:
    room=Outside()    
    def processCommand(self, command):
        response = self.room.message(command)
        self.room = response.getRoom()
        return response.getText()
        
    def prompt(self):
        command = raw_input("> ")
        print self.processCommand(command)
     
"""
class DarkRoom

class Game:
    doorOpen=False
    def message(self, command):
        #Here is where we are dealing with what they typed and channging state
        if("open door" in command):
            self.doorOpen=True            
       

        #Here is where we show a message based on the state.
        if (self.doorOpen == True):

        
        return 'You are at a door.'
        
    def prompt(self):
        command = raw_input("> ")
        print self.message(command)

"""
game = Game()
print "Welcome!"
while True :
    game.prompt()
