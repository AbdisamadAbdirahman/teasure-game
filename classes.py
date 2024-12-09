class Player:
    def __init__(self,name, colour, health):
        self.name = name
        self.colour = colour
        self.health = health
        self.inventory = []
    def grab(self,item):
        if len(self.inventory) < 5:
            self.inventory.append(item)
        else:
            print(self.inventory)
            print("Your inventory is full!")
            dropper = int(input("Enter the index of which item to drop (0,1,2,3,4) (5 to ignore the item): "))
            if dropper == 5:
                print("You ignored the item and kept moving.")
            elif dropper <= 4 and dropper > -1:
                self.inventory.pop(dropper)
                print("You picked up the item and discarded the other item.")
                self.inventory.append(item)
            else:
                print("Please enter a valid number")
    def fight(self, monster: object):
        print(f"You killed the monster {monster.name}")
    
    def interact_npc(self, npc: object):
        pass

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Room:
    def __init__(self, name, npc: bool):
        self.name = name
        self.is_npc_present = npc

