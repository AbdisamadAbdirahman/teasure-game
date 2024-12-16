from classes import *
import sys
from pyfiglet import Figlet
from colored import fg
import time
def scroll(text):
    text = list(text)
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(0.05)
def scroll_big(text):
    text = list(text)
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(0.001)
temp = input("Press anything to start. ")
f = Figlet(font='the_edge')
g = Figlet(font='big')
print("\n")
scroll_big(f.renderText('Treasure Game'))
print("Hello: Please enter your name below: ")
name = str(input("")).lower().lstrip().rstrip()
colour = str(input("What colour do you want your player to be? (red, green, blue, black, white): ")).lower().lstrip().rstrip()
if colour not in ['red','green','blue','black','white']:
    print("Please input a valid colour. Defaulting to white.")
    colour = "white"
player = Player(name, colour, 100)
colour = fg(colour)
print(colour + "This is what your text will look like.")
print("Would you like to hear your origin story?")
choice = str(input("(y/n): ")).lower()
if len(choice) > 1:
    print("Please enter only yes and no. Defaulting to yes")
elif choice == "y":
    print("Okay, here we go!")
    scroll("You are a pirate sailing with your crew, back to your home village in Kismaayo, Somalia, triumphant in retrieving treasures that were once a myth and were never found (no pillaging happened, I promise), when beneath the crew, there was an undiscovered leak, and you realised WAY too late.")
    time.sleep(1)
    scroll(" You could only watch as your ship sank to the bottom of the ocean. All is good though, as all of your crew had been safely evacuated and you still have your treasures with you- \n")
    time.sleep(1)

    print(g.renderText("WHACK!"))
    time.sleep(1)
    scroll(" You feel a sharp pain in the back of your head, and everything goes black. When you opened your eyes again, you were alone, in a place that you had never seen before, with what appears to be nothing else…")
    time.sleep(1)
    scroll(" You wake up in some dungeon, and your story begins. You only have a vague idea of how you got here, but all you know is that you MUST escape. \n")
    time.sleep(2)
else:
    print("Fine, but you WILL have little context on where you are.")
    time.sleep(1)

scroll_big(g.renderText("[24/11/1987, 5 pm GMT, Current Location: behind bars] \n"))
scroll("'What the... where am I?' you think to yourself \n")
scroll("(for the sake of the game, you can only speak in English. I know I said your village is in Somalia, but for universal purposes, you can only speak in English)\n")
scroll(" You realise, you are by yourself, with nothing, and no one. At that moment you realise, your crew BETRAYED you. \n")
scroll(" At that moment, you knew exactly what to do. Firstly, you break out of your jail cell, but now, you need to retrieve those items and seek REVENGE. \n")
scroll(" While wandering past your cell, you come across a door. Naturally, you try opening it... \n")
door1 = Door("start door", True)
door1.interact(player)
scroll(" Yes, the door just spoke to you. Whoever hit you must have hit you really hard. \n")
time.sleep(2)
scroll("'Erm, did you just speak to me?' you ask, with extreme confusion and bewilderment. But there is no response. ")
time.sleep(1)
scroll("'And what key?' You say as you spin around frantically. \n")
time.sleep(3)
scroll(" From what appears to be nowhere, a menu appears. \n")
time.sleep(1)
print(" Here are your options: \n 1. Search your current room \n 2. Check your inventory \n 3. Try to break the door down \n")
time.sleep(2)
scroll("'Wha- you know what, I'm not gonna question this anymore, I've clearly gone insane' you say. \n")
time.sleep(1)
scroll("Okay, so now you need to select an option. ")
while True: 
    choice2 = int(input("Enter option (1,2,3): "))
    if choice2 != 1 and choice2 != 2 and choice2 != 3:
        print("Please only input choice 1, 2 or 3.")
        continue
    elif choice2 == 1:
        scroll("Desperate to escape, you start frantically searching around the room to find a red key.")
        key1 = Key("prison door opener", "red", "start door")
        scroll("Surely this MUST be the right key... \n")
        scroll("You approach the door and try to open it... \n")
        key1.unlock_door(door1)
        scroll("Don'")
        break
    elif choice2 == 2:
        scroll("You frantically open your convenient bag along your waist. From there you see: \n")
        for item in player.inventory:
            print(f"\n {item} \n")
        scroll("Nothing. What did you expect? You JUST got here. Now you have to choose again.")
    else:
        scroll("Out of pure anger of what's just happened to you, you take a couple steps back and run into the door... \n")
        scroll("And now you're dead. Idiot.")
        exit()