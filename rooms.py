class BaseRoom:
    havewelookedaround = False
    dialogue1 = False
    Yes_or_no_masked = False
    Insertgenerictrueorfalsehere = False
    def message(self, command):

        if (self.Insertgenerictrueorfalsehere == True):
            if("no" in command):
                return Response(self, 'Ok, here is an explanation.. typing look (Up or down) will look in that direction the, most common command you will use is "look around" (Use look around too see sorroundings from left to right) ...   Next open (Insert any object here) will open things, sorry for you getting a tutorial now.. It took probably 30 minutes to figure out how to open a door, now finally try typing "inventory" to see what you have on you (type use, info, or remove to interact with your items) ......... Now finally do you want me to take you to the market? They have different stores for potions, all of the generic RPG items you can buy! ')
        if (self.Yes_or_no_masked == True):
            self.Insertgenerictrueorfalsehere = True
            return Response(self, 'Masked Man: Do you know what you\'re doing? (Yes/No)')
        if (self.dialogue1 == True):
            self.Yes_or_no_masked = True
            return Response(self, 'Masked Man: Would you like some help?')
        if("look around" in command):
            self.havewelookedaround = True
            return Response(self, "There is a tall skinny man with a mask on.")
        if (self.havewelookedaround == True):
            self.dialogue1 = True
            return Response(self, "Masked Man: Are you lost?")
        return Response(self, "You have reached the base.")
        


class Outside:
    def message(self, command):
        if("open door" in command):
            return Response(DarkRoom(), "You open the door.")    
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
            return Response(self, 'You see a box of matches on the stone floor, you picked up the matches (Hint: "light _____")')
        if ("light match" in command):
            self.matchLit=True
            return Response(self, "The match lights up for 5 seconds, in that time a sign ahead of you reads \"look behind you\" \n Look behind you? (Yes/No)")
        return Response(self, "The door is open.")

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
