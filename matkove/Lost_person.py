
""" Used Variables:
WOLF      - checks, if you have a wolf
          - and starts the quest if you didn't write junk

cloth1    - random number
cloth2    - number truth check
clothSHOW - informs the player, if he gets a piece of cloth

C1        - choice 'At the place'
CH        - random variable choosing possitive or negative 'story' lines
C2        - second stage choice
C3        - third stage choice
CH2       - random variable choosing possitive or negative 'story' lines in second stage


ZERO   - fill empty space
"""

# GENERAL INFO
print("Lost Person:")
print("a new fan made quest from the bar")
print('by #6221')
print()
print("Range from survivors camp:                      50-100km")
print("Chance to get cloth:                            10%")
print("Chance for a possitive or negative story line:  50%")
print()

import random

# COUNTERS SPOILERS, ENDS THE PROGRAM
def gotcha():
    print("Nice try, bro \nTry again typing right  :)")
        
# GIVES EXPERIENCE, REPUTATION AND MONEY
def to_base(Q):
    print('Hit \'ENTER\' to continue')
    input()
    print()
    print('You returned to base')
    if Q == 1:
        XP   = 150
        REP  = 75
        CASH = 250

    elif Q == 10:
        XP   = 0
        REP  = -30
        CASH = 0

    print('Experience gained:  ', XP)
    print('Reputation gained:  ', REP)
    print('Money gained:       ', CASH)
    print()
    print('These values are for the FISHING VILLAGE, I don\'t know')
    print('the formula of increasing these values in other surv. bases')

WOLF = input('Do you own a wolf? \nWrite true or false     ',)

if WOLF == 'true':
    cloth1 = random.randint(1,100)
    cloth2 = cloth1%10

    if cloth2 == 0:     # if cloth1 == 10,20,30,40,50,60,70,80,90,100
        def clothSHOW():
            print()
            print('The bartender gave you a piece of cloth')
            print('belonging to the lost person.')
        def cloth3():
            print("3) Let the wolf track the smell")
    else:
        def clothSHOW():
            print()
            print('The bartender didn\'t give you a piece of cloth')
            print('belonging to the lost person.')
        def cloth3():
            pass

elif WOLF == 'false':
    def cloth3():
        pass
    def clothSHOW():
        pass

else:
    print()
    print("Nice try, bro \nTry again typing right  :)")


# THE QUEST STARTS
if WOLF == 'true' or WOLF == 'false':

    clothSHOW()
    print()
    print("I have arrived at the place of their last contact. What now?")
    print("1) Search for tracks")
    print("2) Shoot into air")
    cloth3()

    C1 = int(input("Write the number you want to choose:  ", ))
    print()

    # 1) SEARCH FOR TRACKS
    if  C1 == 1:
        CH = random.randint(1,2)

        if CH == 1:
            print('After ten minutes of searching \nI found a trace of a boot in the mud \nseveral metres from the place')
            print('1) Follow the track, \'hit ENTER\'')
            input()
            print('I saw a camp, where a man was sitting \nnear the fire holding a shotgun. \nI immmediately called him and told who I am.')
            print('After I mentioned the names of his comrades, \nhe grabbed his backpack and came to me with a smile.')
            print('1) Go back to base')
            to_base(1)
        
        elif CH == 2:
            print('I kept following the trail \nfor about half a hour. Then, suddenly, \nI found wolf tracks near it. I reloaded my gun')
            print('and continued forward. A few minutes after that \nI stumbled upon a corpse, more like a skeleton with')
            print('damaged clothes on it. There was a shotgun n\in the grass nearby.')                                                    
            print('1) Search the body')
            print('2) Leave')
            C2 = int(input("Write the number you want to choose:  ", ))
            print()

            #  1) SEARCH THE BODY
            if C2 == 1:
                print('I\'ve found a wallet with a passport in one of the packets.')
                print('This was our lost person.')
                print()
                print('got IZh-18, 1-6 bandages, 1-10 insulating tape, TT-33 damaged,')
                print('3-15 pistol ammo, standard looter corpse loot')
                print()
                print('1) Bury the body')
                print('2) Leave')
                C3 = int(input("Write the number you want to choose:  ", ))
                print()

                # 1) BURY THE BODY aka *BURY THE LIIIGHT DEEP WITHIIIIN...*
                if C3 == 1:
                    print('I finished the grave, and made a small hill of stones')
                    print('upon it as a monumet. As I grabed my things and wanted')
                    print('to leave, I noticed something strongly breathing in the bushes')
                    print('After a few seconds I recognised a bear sniffing the ground')
                    print('and coming in my direction. It suddenly stopped doing so,')
                    print('probably catching my smell. It didn\'t look very happy to')
                    print('see me and emerged a loud roar.')
                    print('-10 energy, -10 rags or any, +40 experience')
                    print()
                    print('Fight the beast (radioactive not mutant bear), then return to base')
                    to_base(1)

                elif C3 == 2:
                    to_base(10)

                else:
                    gotcha()

            elif C2 == 2:
                to_base(10)

            else:
                gotcha()

    # 2) SHOOT INTO AIR
    elif C1 == 2:
        CH = random.randint(1,2)
        
        if CH == 1:
            print('After a few minutes I heard a shot from a shotgun.')
            print('He is alive! I immediately started running to the sound\'s epicentre.')
            print('1) Keep going, \'hit ENTER\'')
            input()
            CH2 = random.randint(1,2)
            print()
            
            if CH2 == 1:
                print('I saw clouds of smoke between the trees and shortly after that')
                print('a small camp. The man was standing by the smoking campfire with')
                print('his shotgun ready to fire pointed straight to my direction,')
                print('but after I said what I\'m doing here and mentioned the names')
                print('of his comrades, he grabbed his backpack and came to me with a smile.')
                to_base(1)
                
            elif CH2 == 2:
                print('As I got nearer, I heard a man shout: \"There are wolfs under me, arm yourself!\"')
                print('And he shot from the shotgun again. No doubt that was the same shot,')
                print('but what with the \'under him\'? When I went nearer, I understood. He was sitting')
                print('on a tree and three wolves were patrolling around it, totally ignoring his shots.')
                print('After they noticed, that I arrived, they didn\'t hesitate and ran straight at me.')
                print('The guy jumped from the tree and rushed to help me.')
                print()
                print('Fight the beasts (3 radioactive wolves)')
                print()
                print('1) The man survived the battle')
                print('2) The man has fallen during the battle')
                C2 = int(input('Choose how did the fight end:  ',))
                print()

                # 1) THE MAN SURVIVED
                if C2 == 1:
                    print('The last wolf has fallen. The man had lots of questions and a loaded shotgun,')
                    print('but my answers showed him clearly, that I was a friend.')
                    to_base(1)

                # 2) THE MAN HAS FALLEN
                elif C2 == 2:
                    print('The last wolf made its last breath, but the guy has been severely injured.')
                    print('I need to heal him quickly or he\'ll die.')
                    print()
                    print('1) Treat the wounds (stuff used for lacerations)')
                    print('2) Search for herbs (5 bandages needed)')
                    print('3) Cauterize the wounds')
                    print()
                    C3 = int(input('Choose which option to heal him you want to use:  ', ))
                    print()

                    # 1) TREAT THE WOUNDS
                    if C3 == 1:
                        print('A few minutes passed since I treated him and he tried to stand up.')
                        print('I said that he should save powers, but replied that he doesn\'t want to stay')
                        print('here any longer. I silently agreed.')
                        print('-(stuff used for lacerations), +30 experience')
                        to_base(1)

                    # 2) SEARCH FOR HERBS   
                    elif C3 == 2:
                        print('I\'ve found some white man\'s foot and placed it cleaned on the wounds')
                        print('under the bandages. After about 30 minutes the man said that the wounds')
                        print('are closing and he feels much more stronger. Such an energic person.')
                        print('-5 bandages, got 2 white man\' foot, +20 experience')
                        to_base(1)

                    # 3) CAUTERIZE THE WOUNDS
                    elif C3 == 3:
                        print('I cauterized the wounds and let him rest. I stood on patrol for 5 hours')
                        print('and gave the guy some food. He wasn\'t in best shape, but ready to go.')
                        print('Transport and Walking speed is reduced by 40% for 12 hours')
                        print('-1 honey')
                        to_base(1)

                    else:
                        gotcha()
                   
                else:
                    gotcha()

        if CH == 2:
            print('As a feedback to my shot, I heard a horrible growl. Something like the mouth')
            print('of the creature was damaged.')
            print()
            print('1) Get closer')
            print('2) Hide in the bush')
            print('3) Get the hell out of here!')
            C2 = int(input('Write the number you want to choose:  ', ))
            print()
            
            # 1) GET CLOSER
            if C2 == 1:
                print('A radioactive bear showed in front of me and slowly bleeding from its chin.')
                print('I am too close, there\'s no other option then to fight it.')
                print('Fight the beast (radioactive not mutant bear),then continue search')
                print()
                print('As I suspected. Fifty metres from the battle field I\'ve found a corpse totally torn to shreds')
                print('by the monster. Even the bones were broken and thrown around. The remains of the passport')
                print('were enough to identify the body. Our guy had no chance to survive. His shotgun was lying nearby')
                print('broken on half. I got all remains together made him a mall grave with a stone circle on it.')
                print('I need to get out of here.')
                print('Get 2 screws, TT-33 damaged, 8 pistol ammo')
                
            # 2) HIDE IN THE BUSH
            elif C2 == 2:
                print('A mutant bear showed about 30 metres in front of me and slowly bleeding from its chin.')
                print('I stayed silent as night and observed the dreadful creature.')
                print('1) Stay hidden')
                print('2) Attack')
                C3 = int(input('Write the number you want to choose:  ', ))                
                print()

                CH2 = random.randint(1,2)
                # 1) STAY HIDDEN
                if C3 == 1 and CH2 == 1:
                    print('The bear didn\'t notice me and I could continue my search. As I suspected.')
                    print('Fifty metres from the hiding spot I\'ve found a corpse totally torn to shreds')
                    print('by the monster. Even the bones were broken and thrown around. The remains of the passport')
                    print('were enough to identify the body. Our guy had no chance to survive. His shotgun was lying nearby')
                    print('broken on half. I got all remains together made him a mall grave with a stone circle on it.')
                    print('Now I need to get out of here.')
                    print('Get 2 screws, TT-33 damaged, 8 pistol ammo')
                    to_base(1)

                elif C3 == 1 and CH2 == 2:
                    print('I ducked between the bushes and observed the creature. Suddenly, it began sniffing the air,')
                    print('then turned in my direction and emerged a load roar. It caught my smell. There\'s no other option')
                    print('then fight it.')
                    print('Fight the beast (radioactive not mutant bear), then continue search')
                    
                # 2) ATTACK
                elif C3 == 2:
                    print('The bear fell dead to the ground and I could continue my search. As I suspected.')
                    print('Fifty metres from the battle field I\'ve found a corpse totally torn to shreds')
                    print('by the monster. Even the bones were broken and thrown around. The remains of the passport')
                    print('were enough to identify the body. Our guy had no chance to survive. His shotgun was lying nearby')
                    print('broken on half. I got all remains together made him a mall grave with a stone circle on it.')
                    print('I need to get out of here.')
                    print('Get 2 screws, TT-33 damaged, 8 pistol ammo')
                    to_base(1)

                else:
                    gotcha()

            # 3) GET THE HELL OUT OF HERE
            elif C2 == 3:
                to_base(10)

            else:
                gotcha()

    # 3) LET THE WOLF TRACK THE SMELL
    elif C1 == 3 and WOLF == 'true' and cloth2 == 0:
        CH = random.randint(1,2)
        if CH == 1:
            print('The wolf catched the track nearly immediately, so there was no time to waste. After about five')
            print('minutes we reached a camp. A man was sitting near the fire with a shotgun. My wolf barked. ')
            print('The man automatically raised his gun ready to shoot. I shouted at him to calm down, that I will')
            print('explain everyhting. After I mentioned the names of his comrades, he lowered the gun, thanked me and my wolf.')
            to_base(1)
            
        else:
            print('The wolf started running after a few seconds. I could barely catch with him, but I did my best')
            print('After a few minutes of super running. , I saw a guy attacked my mutant centipedes. One just went down by')
            print('by a shot from his shotgun. As the second one dashed at his leg with its jaws, my wolf jumped out of the bush')
            print('and knocked it down. The next one\'s head was blewn apart by another shotgun round. The fourth and last one')
            print('probably realized that it has no chance and tried to retreat, but a good amed shot from my gun killed yhe beast.')
            print('The wolf then brought the biggest part left of his target to my feet. The man quickly raised his shotgun again.')
            print('I told him that his friends sent me to find him. He questioned me a bit more, but then managed to lower')
            print('his gun and go with us.')            
            to_base(1)

    else:
        gotcha()


print()
print('END of mission, smash ENTER to exit')
input()
