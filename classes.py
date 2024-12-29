import time
import sys
from colored import fg
magenta = fg("magenta")

def scroll(text, scroll_interval=0.01):
    text = list(text)
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(scroll_interval)
class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability
    def use(self, monster: object):
        monster.health -= self.damage
        self.durability -= 1
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
                temp = self.inventory[dropper]
                self.inventory.pop(dropper)
                print(f"You picked up the item and discarded {temp}.")
                self.inventory.append(item)
            else:
                print("Please enter a valid number")
    def fight(self, monster: object, Weapon: object):
        while monster.health > 0:
            Weapon.use(self)
        print(f"You killed {monster.name}.")
class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, player: object):
        player.health -= self.damage
class Room:
    def __init__(self, name, npc: bool, locked: bool):
        self.name = name
        self.is_npc_present = npc
        self.locked = locked
    def display_current(self):
        print(self.name, self.is_npc_present, self.locked)
class Key:
    def __init__(self, name, colour, property):
        self.name = name
        self.colour = colour
        self.room = property
    def unlock_room(self,room: object):
        if self.room == room.name:
            room.locked = False
            print(f"Room {room.name} has been unlocked!")
    def unlock_door(self, door: object):
        if self.room == door.name:
            door.locked = False
            print(f"Door {door.name} has been unlocked!")

class NPC:
    def __init__(self, name, room,dialogue: list, thank: list):
        self.name = name
        self.current_room = room
        self.dialogue = dialogue
        self.thank = thank
    def interact_player(self):
        for line in self.dialogue:
            scroll(magenta + line)
            time.sleep(1)
            print("")
    def thank_player(self):
        for line in self.thank:
            scroll(magenta + line)
            time.sleep(1)
            print("")

class Door:
    def __init__(self, name, locked: bool):
        self.name = name
        self.locked = locked

    def interact(self,player: object):
        if self.locked:
            print(f" Not yet, {player.name}! You haven't opened me with the key yet!")
            time.sleep(2)
    
