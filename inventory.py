class Inventory:
    items = []
    def __init__(self, items):
        self.items = items
    def message(self, command):
        if("inventory" in command):
            if (len(self.items) == 0):
                return InventoryResponse("You don't have anything yet.")
            things = " \n * ".join(self.items)
            return InventoryResponse("You have the following things in your inventory: \n * "+things)
        return NoInventoryReponse()
class Item:
    nothing=[]

class InventoryResponse:
    def __init__(self, text):
        self.text = text
    def getText(self):
        return self.text
    def exists(self):
        return True

class NoInventoryReponse:
        def getText(self):
            return ""
        def exists(self):
            return False
