from inventory import Inventory

class Player:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.inventory = Inventory()

    def move_north(self):
        """Move player north by one tile"""
        self.y += 1
    
    def move_south(self):
        """Move player south by one tile"""
        self.y -= 1 

    def move_east(self):
        """Move player east by one tile"""
        self.x += 1 

    def move_west(self):
        """Move player west by one tile"""
        self.x -= 1 
