from classes import *
from minigames import *
import sys
from pyfiglet import Figlet
from colored import fg
import time
import random
def scroll(text):
    text = list(text)
    for char in text:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(scroll_interval)
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
scroll_interval = 0.05
scroll_big(f.renderText('Treasure Game'))
print("Hello! Please enter your name below: ")
name = str(input("")).lower().lstrip().rstrip()
colour = str(input("What colour do you want your player to be? (red, green, blue, black, white): ")).lower().lstrip().rstrip()
if colour not in ['red','green','blue','black','white']:
    print("Please input a valid colour. Defaulting to white.")
    colour = "white"
player = Player(name, colour, 100)
door1 = Door("start door", True)
room1 = Room("end room 1", False, True)
room2 = Room("end room 2", False, True)
room3 = Room("end room 3", False, True)
room_list = [
    Room("dungeon room 1", True, True),
    Room("puzzle room 1", True, True),
    Room("dungeon room 2", False, True),
    Room("puzzle room 2", True, True),
    Room("treasure room",True,True),
    Room("actual treasure room",True,False)
]
npc_list = [
    NPC("The Shade","dungeon room 1", ["Ah, awake at last... Good. I was beginning to think you'd sink beneath the weight of your dreams forever.","Strange tides have carried you here, sailor. Do you even recall the taste of the salt air, the cries of your crew, or the treasures you held so dear?"], None),
    NPC("The Threefold Oracle","puzzle room 1", ["..."], ["Clever, sailor. You have danced the grid and claimed victory where many faltered.","But remember this: a single triumph does not guarantee escape. The dungeon watches, and it will not be so easily outwitted again.","Step forward, and face what lies beyond... if you dare."]),
    NPC("The Word Warden","puzzle room 2",["..."],["You have danced with letters and evaded the noose... for now. Clever, yes, but do not let victory lull you into complacency. The dungeon has far greater trials awaiting you.","Go, wordsmith. Your journey continues, though the shadows grow ever darker."]),
    NPC("Treasure chest","treasure room",["..."],None),
    NPC("Abshir Cisse","actual treasure room",["..."],None)
]

colour = fg(colour)
cyan = fg(45)
red = fg("red")
yellow = fg("yellow")
magenta = fg("magenta")
plum = fg(96)
italics = '\033[3m'
end = '\033[0m'
print(colour + "This is what your text will look like.") 
scroll_interval = float(input("Select your scroll interval (default = 0.05): "))
print("Would you like to hear your origin story?")
choice = str(input("(y/n): ")).lower()
if len(choice) > 1:
    print("Please enter only yes and no. Defaulting to yes")
if choice == "y":
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

choice3 = input("Would you like to skip the tutorial? (y/n): ")
if len(choice3) > 1:
    print("Please input only y or n. Defaulting to n")
    choice3 = "n"
if choice3 == "y":
    scroll("Skipping the tutorial...")
    time.sleep(2)
else:
    scroll_big(g.renderText("[24/11/1987, 5 pm GMT, Current Location: behind bars] \n"))
    scroll("'What the... where am I?' you think to yourself \n")
    scroll("(for the sake of the game, you can only speak in English. I know I said your village is in Somalia, but for universal purposes, you can only speak in English)\n")
    scroll(" You realise, you are by yourself, with nothing, and no one. At that moment you realise, your crew BETRAYED you. \n")
    scroll(" At that moment, you knew exactly what to do. Firstly, you break out of your jail cell, but now, you need to retrieve those items and seek REVENGE. \n")
    scroll(" While wandering past your cell, you come across a door. Naturally, you try opening it... \n")

    print(cyan + "\n")
    door1.interact(player)
    print(colour + "\n")
    scroll(" Yes, the door just spoke to you. Whoever hit you must have hit you really hard. \n")
    time.sleep(2)
    scroll("'Erm, did you just speak to me?' you ask, with extreme confusion and bewilderment. But there is no response. ")
    time.sleep(1)
    scroll("'And what key?' You say as you spin around frantically. \n")
    time.sleep(3)
    scroll(" From what appears to be nowhere, a menu appears. \n")
    time.sleep(1)

    print(cyan + "\n Here are your options: \n 1. Search your current room \n 2. Check your inventory \n 3. Try to break the door down ")
    time.sleep(2)
    print(colour + "\n")
    scroll("'Wha- you know what, I'm not gonna question this anymore, I've clearly gone insane' you say. \n")
    time.sleep(1)
    scroll("Okay, so now you (yes, YOU, the person behind the screen) need to select an option. ")
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
            time.sleep(1)
            print(cyan + "\n")
            key1.unlock_door(door1)
            print(colour + "\n")
            scroll("Success! You unlocked the door to the jail and are now free. ")
            player.inventory.append(key1.colour)
            break
        elif choice2 == 2:
            scroll("You frantically open your convenient bag along your waist. From there you see: \n")
            for item in player.inventory:
                print(f"\n {item} \n")
            scroll("Nothing. What did you expect? You JUST got here. Now you have to choose again. ")
        else:
            scroll("Out of pure anger of what's just happened to you, you take a couple steps back and run into the door... \n")
            scroll("And now you're dead. ")
            time.sleep(1)
            colour = fg("red")
            print(colour + "Idiot. \n")
            time.sleep(1)
            scroll_big(f.renderText("YOU DIED"))
            exit()

rnd = random.randint(1,10000)
if rnd == 6962:
    scroll_big(g.renderText("\n [24/11/1987, 7 pm GMT, Current Location: In the treasure room] \n"))
    scroll("Erm. Why are you in the treasure room? How have you done that? ")
    time.sleep(1)
    scroll("Well, I guess we'll skip to the end.")
    scroll("\n (If you're confused about what happened, this message has a 1 in 10000 chance of appearing. Great job, you found the secret ending on accident!) \n")
    scroll("You look around to find your crew tied up, next to the treasure.")
    scroll(plum + "*muffled cheers of excitement* \n")
    scroll(colour + "'What? How did all of you get here?'")
    scroll("You free your co-captain, Abshir Cisse, to do the talking for the rest of the crew. ")
    scroll(plum + f"{name}! Thank you for freeing us! Listen, we NEED to get back with this treasure, before it's too late! \n")
    scroll(colour + "'Too late?'")
    scroll(plum + "I lied. We aren't in a time constraint, don't worry. BUT, we still have to get back to Kismaayo, we've been trapped in here for how long? \n")
    scroll_big(g.renderText("[26/11/1987, 7 pm GMT, Current Location: In the treasure room] \n"))
    scroll(colour + "'Only 2 days, apparently.' \n")
    scroll(plum + "That's besides the point. We ALL have to get back home... \n")
    
    scroll(colour + italics + "'But wait. Didn't they betray me? Didn't they want to take the treasures themselves?' \n" + end)
    while True:
        choice8 = input(colour + "Do you leave them behind? (y/n): ").lower().strip()
        if choice8 not in ['y','n']:
            print("Please enter only y or n. ")
        elif choice8 == 'y':
            scroll("Without saying another word, you take the treasures and disappear in an instant. \n")
            scroll("You get back home with all the treasure, and were greeted by cheers and applause. \n")
            scroll("Upon interrogation about the rest of the crew, you make up a fake story, get caught and are sentenced to life in prison. \n")
            scroll_big(yellow + f.renderText("YOU WON, BUT AT WHAT COST?"))
            exit()
        elif choice8 == 'n':
            scroll(italics + "No, I'm not like this, I'm a good person. \n" + end)
            scroll("With the help of Abshir, you untie the rest of the crew, and disappear from the dungeon in an instant. \n")
            scroll("You get back home safely with all the treasure, and your crew, and were greeted by cheers and applause. \n")
            scroll("The president of Somalia recognises your great feat and hails you and your crew for your brave actions. \n")
            scroll_big(yellow + f.renderText("YOU WON!"))
            exit()
    exit()
else:
    scroll_big(g.renderText("\n [24/11/1987, 7 pm GMT, Current Location: Outside the jail] \n"))
time.sleep(1)
scroll("Nice! You escaped the jail. However as you look around, your happiness will not last...")
time.sleep(3)
scroll_big(g.renderText("\n [24/11/1987, 7 pm GMT, Current Location: Inside a dungeon] \n"))
count = 0
scroll("'Oh for god's sake' you say, frustrated. 'Why me?' \n")
scroll("But there is no time to be angry, as the worst is yet to come. You are now on your own for the rest of this. Good luck. \n")
while True:
    dungeon = room_list[count]
    print(cyan + "Here are your options: ")
    print(" 1. Interact with the room \n 2. Show statistics ")
    room_choice = input(colour + "Enter options (1,2): ")
    if room_choice not in ['1','2']:
        scroll("Please enter only 1 or 2.")
    elif room_choice == '1':
        scroll(f"\n Room name: {dungeon.name} ")
        time.sleep(0.5)
        scroll(f"\n Is an NPC in the room with us? {dungeon.is_npc_present} ")
        time.sleep(0.5)
        scroll(f"\n Are you locked in the room? {dungeon.locked} ")
        while True:
            if dungeon.is_npc_present:
                room_choice2 = input("\n Interact with the NPC? (y/n): ").lower()
                if room_choice2 not in ['y','n']:
                    scroll("\n Please enter only y or n.")
                elif room_choice2 == 'y':
                    for i in range(len(npc_list)):
                        if npc_list[i].current_room == dungeon.name:
                            npc = npc_list[i]
                    npc.interact_player()
                    if npc.current_room == "dungeon room 1":
                        scroll(cyan + "Here are your options: ")
                        print("\n 1. 'Who are you?' \n 2. 'What is this place?' \n 3. 'How do i find my way out of here?' \n 4. 'Get out of my head!' \n 5. 'Please talk normally.' ")
                        print(colour + "")
                        choice4 = input("Enter options (1,2,3,4,5): ")
                        if choice4 not in ['1','2','3','4','5']:
                            scroll("\n Please enter only 1,2,3,4 or 5. Defaulting to 1.")
                            time.sleep(1)
                            choice4 = "1"
                        if choice4 == "1":
                            scroll(magenta + "Me? I am but a whisper in the dark, a fragment of what this place once was... or what it will be again. Names hold no meaning here, but you can call me Shade, if that helps. \n")
                            time.sleep(2)
                        elif choice4 == "2":
                            scroll(magenta + "A prison. A labyrinth. A graveyard for souls who dared too much or knew too little. But what it truly is... that, you must discover for yourself. \n")
                            time.sleep(2)
                        elif choice4 == "3":
                            scroll(magenta + "Out? Ha! Many have tried, sailor, but this place is alive. It shifts, it hungers, it toys with its prey. But if you are clever, perhaps it will let you slip through its fingers. \n")
                            time.sleep(2)
                        elif choice4 == "4":
                            scroll(magenta + "Out of your head? I am not in your head, sailor. It is you who are in mine. The walls hear you. The stones feel you. The air itself watches you. \n")
                            time.sleep(2)
                        elif choice4 == "5":
                            scroll(magenta + "Talk... normally? Oh, how quaint. But sailor, this is my normal. If you wish for plain words, you must seek them elsewhere... though I doubt you'll find much simplicity in this place. \n")
                            time.sleep(2)
                        scroll(magenta + "But alas, sailor, the choices you make here are as fleeting as the tides—ripples in a vast ocean of inevitability. Whether you seek answers, escape, or meaning, this place will not care for your desires. It will do as it pleases, and so shall I. \n")
                        time.sleep(2)
                        scroll("Fear not, sailor, for I am no bringer of harm, nor a chain to drag your steps. My purpose here is not to hinder, but to guide... though the path I offer may be shrouded in shadow. \n")
                        time.sleep(2)
                        scroll("Beyond this threshold lies a room not built for wandering feet, but for a restless mind. The stones themselves whisper riddles, their secrets locked tight behind clever thought. Fail to listen, sailor, and you may find the silence... eternal. \n")
                        time.sleep(2)
                        scroll("Step carefully, for this place thrives on confusion. Solve, or surrender — it does not care which you choose. \n")
                        time.sleep(2)
                        scroll(colour + "And with that, the Shade disappears into the shadows, which revealed a green key. \n")
                        time.sleep(1)
                        key2 = Key("Key 2", "green", "dungeon room 1")
                        scroll("'Oh. Well that was nice of him, whatever his name was again' you think to yourself. \n")
                        time.sleep(1)
                        scroll("Obviously, now that you have the key, you unlock the door... \n")
                        key2.unlock_room(room_list[count])
                        time.sleep(1)
                        scroll("And you walk in to the next room. \n")
                        time.sleep(1)
                        player.inventory.append(key2.colour)
                        count += 1   
                        break
                    elif npc.current_room == "puzzle room 1":
                        tic = TicTacToe()
                        scroll(colour + "The NPC in this room appears to not speak. That's because, there is no NPC. It appears to be... a tic tac toe machine? \n")
                        time.sleep(1)
                        scroll("'Bit random, but okay' you think to yourself. \n")
                        scroll("Obviously, with there being no other way around this, you have to verse the machine in a tic tac toe battle. Shouldn't be too difficult, right? \n")
                        scroll(magenta + "'I'll be nice, and let you go first.' said the machine, out of nowhere. ")
                        scroll(colour + "'I thought you cannot speak? You're a machine!' you say. \n")
                        scroll(magenta + "When has anything made sense here? ")
                        scroll(colour + "'Fairs.'\n")
                        scroll("Okay, so how the game works is that you have a 3*3 grid, like normal, but you have to input an x coordinate and a y coordinate. (0,0) would be top left, (2,0) would be top right, (2,2) would be bottom right, and (0,2) would be bottom left. \n")
                        scroll("Got it? No? Well too bad. \n")
                        while True:
                            print("Game starting")
                            tic.start_game()
                            if tic.winner == 'X':
                                npc.thank_player()
                                break
                            elif tic.winner == 'O':
                                scroll(magenta + "Defeated. Your mind falters where precision is key. Expected, to tell the honest truth. ")
                                time.sleep(1)
                                scroll("But the dungeon is patient, sailor. Prove your worth, or remain here forever. \n")
                                time.sleep(1)
                                scroll(colour + "The machine lets you try again. How lucky of you! Don't waste this opportunity. \n")
                                time.sleep(1)
                                tic.restart_game()
                            elif tic.winner == 'D':
                                scroll(magenta + "A stalemate, sailor. Neither wit nor will prevails this time. ")
                                time.sleep(1)
                                scroll("Try again, if you dare. The path forward requires more than balance — it demands triumph. \n")
                                time.sleep(1)
                                scroll(colour + "The machine lets you try again. How lucky of you! Don't waste this opportunity. \n")
                                time.sleep(1)
                                tic.restart_game()
                        scroll(colour + "You begin to hear the soft hum of the machine get louder and louder, and it appears to not stop, until... \n")
                        scroll_big(g.renderText("BOOM!") + "\n")
                        scroll("'Why did the machine blow up bro \U0001F62D \U0001F64F' \n")
                        scroll("Amongst all of the debris, there lay a blue key \n")
                        key3 = Key("Puzzle Key","blue","puzzle room 1")
                        scroll("'The machine did NOT have to die to give me this \U0001F480 \U0001F64F' \n")
                        scroll("But oh well, you go to unlock the door again... \n")
                        key3.unlock_room(room_list[count]) 
                        time.sleep(1)
                        scroll("And you walk in to the next room. \n")
                        time.sleep(1)
                        player.inventory.append(key3.name)
                        count += 1   
                        break
                    elif npc.current_room == "puzzle room 2":
                        hang = Hangman()
                        scroll(colour + "The NPC in this room also appears to not speak. But you've seen this before. This isn't an NPC. This is... a hangman machine?")
                        scroll("The Monster from the previous room releases you and you scramble up onto your feet. \n")
                        scroll("'Why? Why not just like riddles or something? Why is there a HANGMAN machine out of anything?'")
                        scroll(plum + "Shut up.")
                        scroll(colour + "'My fault.' \n")
                        scroll("You've been through this before. You OBVIOUSLY have to verse the Monster in a hangman battle.")
                        scroll(plum + "What? No! You have to beat the hangman in under 5 attempts.")
                        scroll(colour + "Oh. \n")
                        scroll("Well, you heard the guy. \n")
                        scroll(magenta + "'You have 7 tries, actually.' said the machine, once again out of nowhere. \n")
                        scroll(plum + "Bro, he didn't need to know that! Now he's guaranteed to win. ")
                        scroll(magenta + "I thought you said you were fair. ")
                        scroll(plum + "Just start the game man. ")
                        while True:
                            print(magenta + "Game starting")
                            hang.restart()
                            hang.start_game()
                            if hang.winner:
                                npc.thank_player()
                                break
                            else:
                                scroll(magenta + "Ah, the noose tightens, and the final letter eludes you. Your wit has failed, and so too shall you.")
                                scroll("In this dungeon, failure is not forgiven. Prepare to meet the fate reserved for those who cannot solve its secrets.")
                                scroll(plum + "You heard the machine. Prepare to meet your fate.")
                                scroll(colour + "The monster pulls out an AXE and makes quick work of you. \n")
                                time.sleep(1)
                                scroll_big(red + f.renderText("YOU DIED"))
                                exit()
                        scroll(colour + "You once again hear a loud hum. Since you've seen this before, you take off running to the corner of the room. \n")
                        scroll(plum + "Where are you going? Don't you want to claim your- \n")
                        scroll_big(g.renderText("BOOM!"))
                        scroll(colour + "The machine blows up again, this time taking out the monster with it. \n")
                        scroll("'Can these machines STOP blowing up? This is NOT necessary \U0001F62D \U0001F64F' \n")
                        scroll("But now you have to find the key among both rubble AND blood and flesh. You're a pirate though, so this is not too unfamiliar. \n")
                        scroll("Among the mess, you find a black key covered in blood and rubble.")
                        key4 = Key("Key 4","black","treasure room")
                        scroll("You go up to unlock the door... \n")
                        key4.unlock_room(room_list[count])
                        scroll("Huh. Weird. The key doesn't work. Perhaps there is another key among the mess? \n")
                        while True:
                            final_decision = input("Do you want to throw the black key out? (y/n): ").lower()
                            if final_decision not in ['y','n']:
                                print("Please enter only y or n.")
                            elif final_decision == "y":
                                scroll("You toss the black key aside, and rummage around to find a purple key.")
                                key5 = Key("Key 5","purple","treasure room")
                                scroll("'Surely this must be it..' you think as you open the door, and walk into the next room.")
                                player.inventory.append(key5.colour)
                            else:
                                scroll("'Actually, I might need this key', you think as you go back and rummage around to find a purple key.")
                                key5 = Key("Key 5","purple","treasure room")
                                scroll("'Surely this must be it..' you think as you open the door, and walk into the next room.")
                                player.inventory.append(key4.colour)
                                player.inventory.append(key5.colour)                                
                            break
                        count += 1
                        break
                    elif npc.current_room == "treasure room":
                        scroll("The NPC in this room, once again, doesn't speak. Because, there obviously is not an NPC, It's.. a door? \n")
                        door2 = Door("treasure room",True)
                        scroll("You walk up to the door to find out it has FIVE keyholes. There is also a note posted on the front of the door. It reads: \n")
                        scroll(yellow + "Evaluate the following integral to 1 significant figure for the clue : (bottom limit: 0, top limit: π/2) ∫ (e^(sin(x)))/(3.5+cos^2(x)) with respect to x. \n")
                        scroll(colour + "'I thought this game was in english?' ")
                        scroll(yellow + "It is in English. It's called MATHS. ")
                        scroll(colour + "'What's that?'")
                        scroll(yellow + "You don't know MATHS? Ugh, fine, I'll give you 8 options, just because I'm nice. ")
                        scroll(cyan + "Here are your options: ")
                        print("\n 1. '0' \n 2. '0.2' \n 3. '0.6' \n 4. '0.8' \n 5. '1' \n 6. '1.4' \n 7. '2.2' \n 8. 'π' ")
                        print(colour + "")
                        scroll("'π'? What? \n")
                        scroll(yellow + "Shut up and pick an option already. ")
                        scroll(colour + "Erm, okay. \n")
                        while True:
                            choice6 = input(colour + "Enter options (1,2,3,4,5,6,7,8): ")
                            if choice6 not in ['1','2','3','4','5','6','7','8']:
                                scroll("\n Please enter only 1,2,3,4,5,6,7 or 8. \n")
                            elif choice6 != '4':
                                scroll(yellow + "WRONG! But I'll let you keep trying, just because I feel sorry for you. \n")
                            else:
                                scroll(yellow + "Correct! Now figure out what it means, and you will be sure to escape... \n")
                                scroll(colour + "And with that, the door stops talking. \n")
                                scroll("Okay, so I've already figured it out, so good luck. \n")
                                time.sleep(5)
                                scroll("Nothing? You have NO clue what 0.8 means? \n")
                                scroll("'Of course I have no clue what 0.8 could mean, I don't know MATHS.' \n")
                                scroll("BRO- okay, let me just lead you on. ")
                                while True:
                                    choice6 = input("Convert 0.8 to a fraction: ")
                                    if choice6 != '4/5':
                                        scroll("Not quite. Try again. \n")
                                    else:
                                        scroll("Correct! Now since the door has FIVE keyholes, what could 4/5 tell you? \n")
                                        scroll("'Oh! You need 4 out of 5 keys to get through!' \n")
                                        scroll("Well done! \n")
                                        if len(player.inventory) >= 4:
                                            scroll("'And I have enough, because I kept the black key from earlier!' \n")
                                            scroll("You approach the door with haste, and waste no time. You unlock the green keyhole. ")
                                            scroll("You unlock the purple keyhole. ")
                                            scroll("You unlock the black keyhole. ")
                                            scroll("Now for the blue keyhole. You approach the door holding the blue key, and watch in HORROR as the key disintegrates in your hand. \n")
                                            scroll("'What? NO! My chance to ESCAPE! NO!'")
                                            if "red" in player.inventory:
                                                scroll("Don't panic, you have a red key too. \n")
                                                scroll("'Oh yeah. Forgot that I did the tutorial like you were supposed to.' \n")
                                                scroll("You unlock the red keyhole, and..")
                                                print("Door treasure room has been unlocked!")
                                                scroll("And you walk into the next room for the final time. \n")
                                                break
                                            else:
                                                scroll("You have no other keys, do you? \n")
                                                scroll("'No, why would I?' \n")
                                                scroll("You see the red keyhole? Yeah, you woulda got that key if you did the tutorial. Sorry bro \n")
                                                scroll("'Really. So I did ALL THAT, just to LOSE because of a TUTORIAL?'")
                                                scroll("Sorry bro, that's life \n")
                                                time.sleep(1)
                                                scroll_big(red + f.renderText("YOU LOSE"))
                                                exit()
                                        else:
                                            scroll("You only appear to have 3 keys. You probably shouldn't have thrown out that black key. \n")
                                            scroll("'Can I go back and get it?' No. \n")
                                            scroll("'So I lose?' Yeah. \n")
                                            time.sleep(1)
                                            scroll_big(red + f.renderText("YOU LOSE"))
                                            exit()
                                break
                        count += 1 
                        break
                    else:
                        scroll("The NPC in this room doesn't speak either, that's because it's.. all of your crew members tied up? \n")
                        scroll(plum + "*muffled cheers of excitement* \n")
                        scroll(colour + "'What? How did all of you get here?'")
                        scroll("You free your co-captain, Abshir Cisse, to do the talking for the rest of the crew. ")
                        scroll(plum + f"{name}! Thank you for freeing us! Listen, we NEED to get back with this treasure, before it's too late! \n")
                        scroll(colour + "'Too late?'")
                        scroll(plum + "I lied. We aren't in a time constraint, don't worry. BUT, we still have to get back to Kismaayo, we've been trapped in here for how long? \n")
                        scroll_big(g.renderText("[26/11/1987, 7 pm GMT, Current Location: In the treasure room] \n"))
                        scroll(colour + "'Only 2 days, apparently.' \n")
                        scroll(plum + "That's besides the point. We ALL have to get back home... \n")
                        scroll(colour + italics + "But wait. Didn't they betray me? Didn't they want to take the treasures themselves? \n" + end)
                        while True:
                            choice7 = input(colour + "Do you leave them behind? (y/n): ").lower().strip()
                            if choice7 not in ['y','n']:
                                print("Please enter only y or n. ")
                            elif choice7 == 'y':
                                scroll("Without saying another word, you take the treasures and disappear in an instant. \n")
                                scroll("You get back home with all the treasure, and were greeted by cheers and applause. \n")
                                scroll("Upon interrogation about the rest of the crew, you make up a fake story, get caught and are sentenced to life in prison. \n")
                                scroll_big(yellow + f.renderText("YOU WON, BUT AT WHAT COST?"))
                                exit()
                            elif choice7 == 'n':
                                scroll(italics + "No, I'm not like this, I'm a good person. \n" + end)
                                scroll("With the help of Abshir, you untie the rest of the crew, and disappear from the dungeon in an instant. \n")
                                scroll("You get back home safely with all the treasure, and your crew, and were greeted by cheers and applause. \n")
                                scroll("The president of Somalia recognises your great feat and hails you and your crew for your brave actions. \n")
                                scroll_big(yellow + f.renderText("YOU WON!"))
                                exit()

                else:
                    scroll("Bro, you're not gonna move on without interacting with the NPC. I know I said you can make your own decisions, but there kind of is a set way to win.")
            else:
                while True:
                    another_choice = input("\n Explore the room? (y,n): ").lower()
                    if another_choice not in ['y','n']:
                        scroll("\n Please enter only y or n.")
                    elif another_choice == "y":
                        scroll("The room is dark. You scramble to find a light switch and switch it on with haste, only to reveal a MONSTER! \n")
                        monster = Monster("Charles",100,10)
                        scroll(plum + "Intruder... You trespass where you do not belong. Speak quickly: why should I not rend you apart where you stand? \n")
                        time.sleep(1)
                        scroll(cyan + "Here are your options: ")
                        print("\n 1. 'Let me escape this place man' \n 2. 'Move man' \n 3. 'Do I HAVE to fight you?' \n 4. 'Get out of my head!' \n 5. (you say nothing and prepare to fight) ")
                        print(colour + "")
                        choice5 = input("Enter options (1,2,3,4,5): ")
                        if choice5 not in ['1','2','3','4','5']:
                            scroll("\n Please enter only 1,2,3,4 or 5. Defaulting to 1.")
                            time.sleep(1)
                            choice5 = "1"
                        if choice5 == "1":
                            scroll(plum + "Escape? Fool. No one escapes this labyrinth unless it allows them to. But perhaps... I can let you live. Solve my riddle, and I may spare you. \n")
                            scroll("I have no eyes, yet I see all. I have no lungs, yet I breathe. I have no life, yet I can die. What am I?")
                            print(colour + "")
                            riddle = input("Enter your answer: ").lower().strip()
                            if riddle in ["a flame","flame","fire","a fire"]:
                                scroll(plum + "Clever, but you aren't deemed worthy of escape yet. Another trial will begin shortly. Prove your worth, and the dungeon might forgive you. \n")
                            else:
                                scroll(plum + "Incorrect! Your ignorance deems your fate, but I will forgive your mistakes just this once. Another trial will begin shortly, prove that you aren't ignorant, and you might live. \n")
                        elif choice5 == "2":
                            scroll(plum + "No. I shall only move if you prove your worth in this upcoming trial. Fail to succeed, and you have succeeded to fail. Once again. \n")
                        elif choice5 == "3":
                            scroll(plum + "Fool, I have no intent of fighting you, as this will only result in my victory. Although I am a beast, I want to give every opponent a chance. And this next upcoming trial will be your ONLY chance. \n")
                        elif choice5 == "4":
                            scroll(plum + "Out of your head? I am not in your head, you idiot. It is you who are in mine. The walls hear you. The stones feel you. The air itself watches you. \n")            
                        else:
                            scroll(plum + "Ha! You IDIOT! You think you can defeat ME without a weapon? I would have given you a chance to get past, but your ignorance has sealed your fate. \n")
                            monster.attack(player)
                            scroll(colour + "The monster lunges and punches you, dealing 10 damage. \n")
                            scroll(colour + "'That's it? Only 10 damage? Yeah this is about to be quick.'\n")
                            scroll("You open your inventory to pull out your trusty sword, only to find: \n")
                            print(player.inventory)
                            scroll("Keys. You only have keys on you, you idiot. Now you have no weapon to fight. And don't say 'But I can use those as brass knuckles' because the keys aren't sharp enough.")
                            scroll(plum + "'yEaH tHiS iS aBoUt To Be QuIcK' Yeah, for YOU! \n")
                            scroll(colour + "The monster pulls out an AXE and makes quick work of you. \n")
                            time.sleep(1)
                            scroll_big(red + f.renderText("YOU DIED"))
                            exit()
                    else:
                        scroll("Bro you HAVE to explore the room. What are you doing? \n")
                    scroll(colour + "'Wait. What trials are you talking about? And why are you sparing me?'")
                    scroll("You are silenced as you are picked up by the beast as he unlocks the door into the next room.")
                    count += 1
                    break
            break    


    else:                   
        scroll(f"\n Name: {player.name} ")
        time.sleep(0.5)
        scroll(f"\n Health: {player.health} ")
        time.sleep(0.5)
        scroll(f"\n Inventory: {player.inventory} \n")
        
    
