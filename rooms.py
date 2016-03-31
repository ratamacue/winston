class BaseRoom:
    havewelookedaround = False
    dialogue1 = False
    def message(self, command):
        if (self.dialogue1 == True):
            return Response(self, 'Masked man: Would you like some help?')
        if("look around" in command):
            self.havewelookedaround = True
            return Response(self, "There is a tall skinny man with a mask on.")
        if (self.havewelookedaround == True):
            self.dialogue1 = True
            return Response(self, "Masked man: Are you lost?")
        return Response(self, "You have reached the base.")
        


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
                return Response(self, "Under the crack of the door you can see light, enter the door? (Yes/No)")
            if ("yes" in command):
                self.haveWeLookedAround=True            
                return Response(self, "Behind you and behind the open door there is another door. Under the crack of the door you can see light, enter the door? (Yes/No)")
            return Response(self, 'A sign ahead of you reads "look behind you" \n Look behind you? (Yes/No)')
        if ("look around" in command):
            return Response(self, "You look around and notice, the room is dark..")
        if ("look down" in command):
            return Response(self, "You see a box of matches on your belt.")
        if ("light match" in command):
            self.matchLit=True
            return Response(self, "The match lights up for 5 seconds, in that time a sign ahead of you reads \"look behind you\" \n Look behind you? (Yes/No)")
        return Response(self, "The Door Is Open")

class Response:
    room = Outside()    
    text = "This text should never show up."
    def __init__(self, room, text):
        self.room = room
        self.text = text    
    def getRoom(self):
        return self.room
    def getText(self):
        return self.text
