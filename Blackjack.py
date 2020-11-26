# import the pygame module, so you can use it
import pygame
from time import sleep
import random
import os
import math
from multiprocessing import Process
import time

os.system('clear')


display_width = 1280
display_height = 720
global mx
global my
mx = 0
my = 0
#card dimension 411x561    2.5" x 3.5"




# initialize the pygame module
pygame.init()

running = True

# load and set the logo
#logo = pygame.image.load("logo.png")
#pygame.display.set_icon(logo)
pygame.display.set_caption("21 Blackjack - Sam McKid")


global startcolour
global scene
global buttonsDict
global ButtonLocationPrintHolder
global ButtonLocationFinder
global ButtonLocationPrintHolder
global stats
global Deck
global Playing_Colour
global SideBar
global Dealer_Threshold

buttonsDict = {}
startcolour = [255,0,0]
playcolour = [100,100,100]
betcolour = [0,0,0]
scene = "start"
ButtonLocationFinder = 1
ButtonLocationPrintHolder = "Else"
statslist = ["Wins", "Loses", "Cash", "Bet"]
stats = {
    "Wins" : 0,
    "Loses" : 0,
    "Cash" : 1000,
    "Bet" : 0
}
#Diamonds = D, Hearts = H, Clubs = C, Spades = S, Ten = T, Jacks = J, Queens = Q, Kings = K, Ace = A
Deck = [
"DA","D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ","DQ","DK",
"HA","H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ","HQ","HK",
"CA","C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ","CQ","CK",
"SA","S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ","SQ","SK"
]
Playing_Colour = [0,0,0]
SideBar = False
Dealer_Threshold = 17
Comp1_Threshold = 14
Comp2_Threshold = 18
Comp3_Threshold = 1
Insurance = False



global C
global S
global H
global D
C = pygame.image.load("C.png")
S = pygame.image.load("S.png")
H = pygame.image.load("H.png")
D = pygame.image.load("D.png")

Chip_1 = pygame.image.load("1.png")
Chip_5 = pygame.image.load("5.png")
Chip_25 = pygame.image.load("25.png")
Chip_50 = pygame.image.load("50.png")
Chip_100 = pygame.image.load("100.png")
Chip_500 = pygame.image.load("500.png")


def Shuffle():
    global Deck
    for x in range(100000):
        Shuffler_Number_1 = random.randint(0, 51)
        Shuffler_Holder_1 = Deck[Shuffler_Number_1]
        Shuffler_Number_2 = random.randint(0, 51)
        Shuffler_Holder_2 = Deck[Shuffler_Number_2]
        Deck[Shuffler_Number_2] = Shuffler_Holder_1
        Deck[Shuffler_Number_1] = Shuffler_Holder_2


def RainbowMachine(colour, a):
    #startcolour = colour
    startspeed = a
    if colour[0] >= 255 and colour[2] > 0:
        colour[0] = 255
        colour[2] -= startspeed
    elif colour[0] >= 255 and colour[1] < 255:
        colour[0] = 255
        colour[1] += startspeed
    elif colour[1] >= 255 and colour[0] > 0:
        colour[1] = 255
        colour[0] -= startspeed
    elif colour[0] <= 0 and colour[2] < 255:
        colour[0] = 0
        colour[2] += startspeed
    elif colour[2] >= 255 and colour[1] > 0:
        colour[2] = 255
        colour[1] -= startspeed
    elif colour[1] <= 0 and colour[0] < 255:
        colour[1] = 0
        colour[0] += startspeed

    #print(startcolour[0],startcolour[1],startcolour[2])

def printstart():
    global ButtonLocationFinder
    global buttonsDict
    #buttonsDict = {(X, -X, Y, -Y) : operation/number}

    buttonsDict = {
    (550,750,400,500) : "Play"
    }


    screen.fill((60,60,60))


    RainbowMachine(startcolour, 15)
    text1 = "Casino"
    font = pygame.font.Font('Pricedown.ttf', 300) #Font size
    text1 = font.render(text1, True, (startcolour[0]/10,startcolour[1]/10,startcolour[2]/10)) #Font colour
    textRect = text1.get_rect()
    textRect.center = ((display_width/2)+10, 150+10)
    screen.blit(text1, textRect)

    text1 = "Casino"
    font = pygame.font.Font('Pricedown.ttf', 300) #Font size
    text1 = font.render(text1, True, (startcolour[0],startcolour[1],startcolour[2])) #Font colour
    textRect = text1.get_rect()
    textRect.center = ((display_width/2), 150)
    screen.blit(text1, textRect)

    if ButtonLocationFinder == "Play":
        playcolour[0] = startcolour[0]
        playcolour[1] = startcolour[1]
        playcolour[2] = startcolour[2]

    else:
        playcolour[0] = 100
        playcolour[1] = 100
        playcolour[2] = 100


    text2 = "Play"
    font = pygame.font.Font('rageitalic.ttf', 100) #Font size
    text2 = font.render(text2, True, (playcolour[0]/10,playcolour[1]/10,playcolour[2]/10)) #Font colour
    textRect = text2.get_rect()
    textRect.center = ((display_width/2)+5, 450+5)
    screen.blit(text2, textRect)

    text2 = "Play"
    font = pygame.font.Font('rageitalic.ttf', 100) #Font size
    text2 = font.render(text2, True, (playcolour[0],playcolour[1],playcolour[2])) #Font colour
    textRect = text2.get_rect()
    textRect.center = ((display_width/2), 450)
    screen.blit(text2, textRect)

def Draw_Cards(number):
    for Card_Drawn in range(number):
        return Deck[Card_Drawn]

def Card_Info(Card):
    global Card_Suit
    global Card_Type
    global Card_Value


    Card_listed = list(Card)
    Card_Suit = Card_listed[0]
    Card_Type = Card_listed[1]
    #print(Card_Type)
    if Card_Type in "23456789":
        Card_Value = Card_listed[1]
    elif Card_Type in "TJQK":
        Card_Value = 10
    elif Card_Type in "Aa":
        Card_Value = 'Ace'

    #return str(Card_Suit)+"-"+str(Card_Type)+"-"+str(Card_Value)

def Shuffle(Deck):
    for x in range(100000):
        Shuffler_Number_1 = random.randint(0, (len(Deck)-1))
        Shuffler_Holder_1 = Deck[Shuffler_Number_1]
        Shuffler_Number_2 = random.randint(0, (len(Deck)-1))
        Shuffler_Holder_2 = Deck[Shuffler_Number_2]
        Deck[Shuffler_Number_2] = Shuffler_Holder_1
        Deck[Shuffler_Number_1] = Shuffler_Holder_2

def Hand_Value(Hand):
    global Card_Value
    Hand_Value = 0
    for i in Hand:
        Card_Info(i)
        #print(Hand_Value)
        if Card_Value == "Ace":
            if Hand_Value + 11 <= 21:
                Hand_Value += 11
            elif Hand_Value + 11 > 21:
                Hand_Value += 1
        elif Card_Value != 'Ace':
            Hand_Value += int(Card_Value)
    return Hand_Value

def setupdeck():
    global Current_Card
    global Deck
    global Player_Hand
    global Dealer_Hand
    global Comp1_Hand
    global Comp2_Hand
    global Comp3_Hand
    Current_Card = 0
    Shuffle(Deck)
    Player_Hand = []
    Dealer_Hand = []
    Comp1_Hand = []
    Comp2_Hand = []
    Comp3_Hand = []
    Player_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Dealer_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Comp1_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Comp2_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Comp3_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Player_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Dealer_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Comp1_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Comp2_Hand.append(Deck[Current_Card])
    Current_Card += 1
    Comp3_Hand.append(Deck[Current_Card])
    Current_Card += 1

def Betting_SideBar():
    global Card_Suit
    global Card_Type
    global Card_Value
    global Current_Card
    global Dealer_Value
    global Dealer_Hand
    global Comp1_Hand
    global Comp2_Hand
    global Comp3_Hand
    global Player_Value
    global Player_Hand
    global Comp1_Threshold
    global Comp2_Threshold
    global Comp3_Threshold
    global Dealer_Shown_Card
    Player_Value = 0

    s = pygame.Surface((1280,720)) # Size of Shadow
    s.set_alpha(100) # Alpha of Shadow
    s.fill((0,0,0)) # Color of Shadow
    screen.blit(s, (0, 0)) # Position of Shadow

    s = pygame.Surface((400,720)) # Size of Shadow
    s.set_alpha(200) # Alpha of Shadow
    s.fill((12, 52, 61)) # Color of Shadow
    screen.blit(s, (0, 0)) # Position of Shadow

    for i in Player_Hand:
        Card_Info(i)
        if Card_Value == "Ace":
            if Player_Value + 11 <= 21:
                Player_Value += 11
            if Player_Value + 11 > 21:
                Player_Value += 1
        else:
            Player_Value += int(Card_Value)
    Card_Info(Dealer_Hand[0])
    Dealer_Shown_Card = str(Card_Suit)+str(Card_Type)




    SideBar_List = [
    "Your Hand Value: ",
    str(Player_Value),
    "Dealer's Card: ",
    str(Dealer_Shown_Card),
    "Bob's Hand Value: ",
    str(Hand_Value(Comp1_Hand)),
    "Joe's Hand Value: ",
    str(Hand_Value(Comp2_Hand)),
    "Karen's Hand Value: ",
    str(Hand_Value(Comp3_Hand))
    ]

    #print(str(Hand_Value(Comp1_Hand)) +":"+ str(Comp1_Threshold))






    Y_Sidebar = 50
    for i in SideBar_List:
        text = str(i)
        font = pygame.font.Font('Economica-Regular.ttf', 50) #Font size
        text = font.render(text, True, (255,255,255)) #Font colour
        textRect = text.get_rect()
        textWidth = text.get_width()
        textRect.center = (200, Y_Sidebar)
        screen.blit(text, textRect)
        Y_Sidebar += 50



    text = "<"
    font = pygame.font.Font('Economica-Regular.ttf', 200) #Font size
    text = font.render(text, True, (255,255,255)) #Font colour
    textRect = text.get_rect()
    textWidth = text.get_width()
    textRect.center = (425, 360)
    screen.blit(text, textRect)


def printplaying():
    global ButtonLocationFinder
    global buttonsDict
    global Deck
    global Player_Hand
    global Dealer_Hand
    global Comp1_Hand
    global Comp2_Hand
    global Comp3_Hand
    global Comp1_Threshold
    global Comp2_Threshold
    global Comp3_Threshold
    global Playing_Colour
    global SideBar
    global Current_Card
    global Card_Suit
    global Card_Value
    global Card_Type
    global Dealer_Value
    global scene
    global Dealer_Shown_Card
    global Insurance
    global stats

    PlayingList = ["Hit", "Stand", "Split", "Insure", "Surndr"]
    #buttonsDict = {(X, -X, Y, -Y) : operation/number}


    Player_Value = 0

    buttonsDict = {
    (30,240,560,700) : "Hit",
    (280,490,560,700) : "Stand",
    (530,740,560,700) : "Split",
    (780,990,560,700) : "Insure",
    (1030,1240,560,700) : "Surrender",
    (0,50,320,400) : "SideBarOpen",
    (400,450,320,400) : "SideBarClose"
    }
    #print(str(mx) + "," + str(my))

    #buttonsDict = {
    #(0,400,0,720) : "Side"
    #}
    RainbowMachine(Playing_Colour, 15)

    screen.fill((12,52,61))

    pygame.draw.rect(screen, (0, 0, 0), (30, 560, 210, 140))#Black
    pygame.draw.rect(screen, (255, 255, 255), (32, 562, 206, 136)) #White

    pygame.draw.rect(screen, (0, 0, 0), (280, 560, 210, 140))#Black
    pygame.draw.rect(screen, (255, 255, 255), (282, 562, 206, 136)) #White

    pygame.draw.rect(screen, (0, 0, 0), (530, 560, 210, 140))#Black
    pygame.draw.rect(screen, (255, 255, 255), (532, 562, 206, 136)) #White

    pygame.draw.rect(screen, (0, 0, 0), (780, 560, 210, 140))#Black
    pygame.draw.rect(screen, (255, 255, 255), (782, 562, 206, 136)) #White

    pygame.draw.rect(screen, (0, 0, 0), (1030, 560, 210, 140))#Black
    pygame.draw.rect(screen, (255, 255, 255), (1032, 562, 206, 136)) #White

    #print(SideBar)

    #print(ButtonLocationPrintHolder)


    PlayngText_X = 135
    for PlayngText in PlayingList:
        PlayngText = str(PlayngText).upper()
        font = pygame.font.Font('Beon.otf', 50) #Font size
        PlayngText = font.render(PlayngText, True, (Playing_Colour[0],Playing_Colour[1],Playing_Colour[2])) #Font colour
        textRect = PlayngText.get_rect()
        textWidth = PlayngText.get_width()
        textRect.center = (PlayngText_X, 630)
        screen.blit(PlayngText, textRect)
        PlayngText_X += 250

    game = True

    Card_X = 2+20
    Card_Y = 2+20


    for a in Player_Hand:

        PrintCard(a, Card_X, Card_Y)
        Card_X += 152+20
    Card_X = 2



    for i in Player_Hand:
        Card_Info(i)
        if Card_Value == "Ace":
            if Player_Value + 11 <= 21:
                Player_Value += 11
            elif Player_Value + 11 > 21:
                Player_Value += 1
        else:
            Player_Value += int(Card_Value)


    Dealer_Value = 0
    for i in Dealer_Hand:
        Card_Info(i)
        if Card_Value == "Ace":
            if Dealer_Value + 11 <= 21:
                Dealer_Value += 11
            elif Dealer_Value + 11 > 21:
                Dealer_Value += 1
        else:
            Dealer_Value += int(Card_Value)

    if Dealer_Value < Dealer_Threshold:
        Dealer_Hand.append(Deck[Current_Card])
        Current_Card += 1

    Comp1_Value = Hand_Value(Comp1_Hand)
    Comp2_Value = Hand_Value(Comp2_Hand)
    Comp3_Value = Hand_Value(Comp3_Hand)
    if Comp1_Value < Comp1_Threshold:
        Comp1_Hand.append(Deck[Current_Card])
        Current_Card += 1
    if Comp2_Value < Comp2_Threshold:
        Comp2_Hand.append(Deck[Current_Card])
        Current_Card += 1
    if Comp3_Value < Comp3_Threshold:
        Comp3_Hand.append(Deck[Current_Card])
        Current_Card += 1


    if ButtonLocationPrintHolder == "Hit" and Player_Value < 21:
        Player_Hand.append(Deck[Current_Card])
        Current_Card += 1
        time.sleep(0.5)

    if Player_Value > 21:
        printend("You Bust")
        scene = "ending"

    if len(Player_Hand) >= 5 and Player_Value <= 21:
        printend("You Win")
        scene = "ending"

    if ButtonLocationPrintHolder == "Stand":
        if Dealer_Value > Player_Value and Dealer_Value <= 21:
            printend("Lose")
            scene = "ending"
        elif Dealer_Value == Player_Value:
            printend("Tie")
            scene = "ending"
        elif Dealer_Value < Player_Value:
            printend("Win")
            scene = "ending"
        elif Dealer_Value > 21:
            printend("Dealer Bust")
            scene = "ending"

    Card_Info(Dealer_Hand[0])
    Dealer_Shown_Card = str(Card_Suit)+str(Card_Type)

    if ButtonLocationPrintHolder == "Insure" and "A" in Dealer_Shown_Card and Insurance == False and stats["Cash"] >= 0.5*stats["Bet"]:
        Insurance = True
        if Dealer_Hand[1] in "KQJT": #picture or ten card
            stats["Cash"] += 0.5*stats["Bet"]
        else:
            stats["Cash"] -= 0.5*stats["Bet"]




    if ButtonLocationPrintHolder == "SideBarOpen":
         SideBar = True
    if ButtonLocationPrintHolder == "SideBarClose":
          SideBar = False




    if SideBar == False:
        text = ">"
        font = pygame.font.Font('Economica-Regular.ttf', 200) #Font size
        text = font.render(text, True, (255,255,255)) #Font colour
        textRect = text.get_rect()
        textWidth = text.get_width()
        textRect.center = (20, 360)
        screen.blit(text, textRect)

    if SideBar == True:
        Betting_SideBar()



def printbetting():
    global ButtonLocationFinder
    global buttonsDict
    global ButtonLocationPrintHolder
    global stats
    buttonsDict = {
    (450,600,500,650) : "1",
    (600,750,500,650) : "5",
    (750,900,500,650) : "25",
    (900,1050,500,650) : "50",
    (1050,1200,500,650) : "100",
    (1100,1250,300,500) : "500",
    (71,335,458,538) : "clear",
    (501,791,65,207) : "Bet"
    }


    screen.fill((12,52,61))
    pygame.draw.rect(screen, (19, 79, 92), (0, 0, 400, 720)) # Location, location, size, size

    text = "Your Stats"
    font = pygame.font.Font('Economica-Regular.ttf', 40) #Font size
    text = font.render(text, True, (255,255,255)) #Font colour
    textRect = text.get_rect()
    textRect.center = (200, 75)
    screen.blit(text, textRect)

    pygame.draw.rect(screen, (255, 255, 255), (25, 100, 350, 1))

    screen.blit(Chip_1, (450, 500))
    screen.blit(Chip_5, (600, 500))
    screen.blit(Chip_25, (750, 500))
    screen.blit(Chip_50, (900, 500))
    screen.blit(Chip_100, (1050, 500))
    screen.blit(Chip_500, (1100, 350))

    if ButtonLocationPrintHolder in "1250100500" and (stats["Cash"] - int(ButtonLocationPrintHolder))>=0:
        stats["Bet"] += int(ButtonLocationPrintHolder)
        stats["Cash"] -= int(ButtonLocationPrintHolder)
        time.sleep(0.1)
    elif ButtonLocationPrintHolder == "clear":
        stats["Cash"] += stats["Bet"]
        stats["Bet"] = 0

    for timesthru in range(4):
        text = statslist[timesthru]+": "
        font = pygame.font.Font('Economica-Regular.ttf', 40) #Font size
        text = font.render(text, True, (255,255,255)) #Font colour
        textRect = text.get_rect()
        textWidth = text.get_width()
        textRect.center = (10 + (textWidth/2), 200+50*timesthru)
        screen.blit(text, textRect)

    for timesthru in range(4):
        if statslist[timesthru] == "Cash" or statslist[timesthru] == "Bet":
            text = "$" + str(stats[statslist[timesthru]])
        else:
            text = str(stats[statslist[timesthru]])
        font = pygame.font.Font('Economica-Regular.ttf', 40) #Font size
        text = font.render(text, True, (255,255,255)) #Font colour
        textRect = text.get_rect()
        textWidth = text.get_width()
        textRect.center = (120 + (textWidth/2), 200+50*timesthru)
        screen.blit(text, textRect)

    text = "clear bet"
    font = pygame.font.Font('Economica-Regular.ttf', 100) #Font size
    text = font.render(text, True, (255,255,255)) #Font colour
    textRect = text.get_rect()
    textWidth = text.get_width()
    textRect.center = (200, 500)
    screen.blit(text, textRect)


    #if ButtonLocationFinder == "Bet":
    RainbowMachine(betcolour, 17)

    text1 = "BET"
    font = pygame.font.Font('Pricedown.ttf', 200) #Font size
    text1 = font.render(text1, True, (betcolour[0]/10,betcolour[1]/10,betcolour[2]/10)) #Font colour
    textRect = text1.get_rect()
    textRect.center = ((display_width/2)+10, 150+10)
    screen.blit(text1, textRect)

    text1 = "BET"
    font = pygame.font.Font('Pricedown.ttf', 200) #Font size
    text1 = font.render(text1, True, (betcolour[0],betcolour[1],betcolour[2])) #Font colour
    textRect = text1.get_rect()
    textRect.center = ((display_width/2), 150)
    screen.blit(text1, textRect)


def printend(ending):
    sleep(0.3)
    global Dealer_Hand
    global Dealer_Value
    global Player_Hand
    global Player_Value
    global buttonsDict
    global scene
    global stats
    screen.fill((60,60,60))
    buttonsDict = {
    (0,1280,0,720) : "Play"
    }

    if ending == "You Bust":
        text1 = "You Bust"
        stats["Loses"] += 1
    elif ending == "Lose":
        text1 = "You Lose"
        stats["Loses"] += 1
    elif ending == "Tie":
        text1 = "Tie"
        stats["Cash"] += stats["Bet"]
    elif ending == "Win":
        text1 = "You Win"
        stats["Wins"] += 1
        stats["Cash"] += 2*(stats["Bet"])
    elif ending == "Dealer Bust":
        text1 = "Dealer Bust"
        stats["Wins"] += 1
        stats["Cash"] += 2*(stats["Bet"])
    else:
        text1 = "IDK"
        stats["Cash"] += stats["Bet"]
    stats["Bet"] = 0

    RainbowMachine(startcolour, 15)
    text2 = text1
    font = pygame.font.Font('Pricedown.ttf', 300) #Font size
    text1 = font.render(text1, True, (15,15,15)) #Font colour
    textRect = text1.get_rect()
    textRect.center = ((display_width/2)+10, 150+10)
    screen.blit(text1, textRect)

    text1 = text2
    font = pygame.font.Font('Pricedown.ttf', 300) #Font size
    text1 = font.render(text1, True, (150,150,150)) #Font colour
    textRect = text1.get_rect()
    textRect.center = ((display_width/2), 150)
    screen.blit(text1, textRect)

    Player_Value = 0
    for i in Player_Hand:
        Card_Info(i)
        if Card_Value == "Ace":
            if Player_Value + 11 <= 21:
                Player_Value += 11
            if Player_Value + 11 > 21:
                Player_Value += 1
        else:
            Player_Value += int(Card_Value)


    End_PrintList = [
    "Your Hand: " + str(Player_Hand),
    "Your Value: " + str(Player_Value),
    "Dealer Hand: " + str(Dealer_Hand),
    "Dealer Value: " + str(Dealer_Value),
    "Click to play again"
    ]

    Y= 350
    for i in End_PrintList:
        text1 = i
        font = pygame.font.Font('Beon.otf', 50) #Font size
        text1 = font.render(text1, True, (255,255,255)) #Font colour
        textRect = text1.get_rect()
        textRect.center = ((display_width/2), Y)
        screen.blit(text1, textRect)
        Y += 50



    #scene = "betting"





def PrintCard(Card, x, y):
    Card_Info(Card)
    global Card_Suit
    global Card_Type
    global Card_Value
    global C
    global S
    global H
    global D
    #print(Card_Type)
    Suits = {
    "C" : C,
    "S" : S,
    "H" : H,
    "D" : D
    }
    SuitsDimensionsY = {
    "C" : 72,
    "S" : 58,
    "H" : 79,
    "D" : 56
    }

    pygame.draw.rect(screen, (0, 0, 0), (x-1, y-1, 152, 212))#Black
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 150, 210)) #White
    screen.blit(Suits[Card_Suit], (x+25, y+SuitsDimensionsY[Card_Suit]))

    text = str(Card_Type).upper()
    font = pygame.font.Font('PokerInOctoberDemo-Dxm3.otf', 50) #Font size
    text = font.render(text, True, (255,255,255)) #Font colour
    textRect = text.get_rect()
    textWidth = text.get_width()
    textRect.center = (x+75, y+120)
    screen.blit(text, textRect)





### SREEN AND CLOCK ###
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

while running == True:



    mx, my = pygame.mouse.get_pos()



    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False


    for ButtonLocations in buttonsDict:
        xlimithigh = ButtonLocations[0]
        xlimitlow = ButtonLocations[1]
        ylimithigh = ButtonLocations[2]
        ylimitlow = ButtonLocations[3]

        if mx > xlimithigh and mx < xlimitlow and my > ylimithigh and my < ylimitlow:
            ButtonLocationFinder = buttonsDict[ButtonLocations]
            #print(ButtonLocationFinder)



    if event.type == pygame.MOUSEBUTTONDOWN:       #From Alexander Henry Photios
        #print("x: " + str(mx) + "  y: " + str(my))

        #ButtonLocationPrintHolder = "Else" #This is the mouse position with a click
        for ButtonLocations in buttonsDict:
            xlimithigh = ButtonLocations[0]
            xlimitlow = ButtonLocations[1]
            ylimithigh = ButtonLocations[2]
            ylimitlow = ButtonLocations[3]

            if mx > xlimithigh and mx < xlimitlow and my > ylimithigh and my < ylimitlow:
                ButtonLocationPrintHolder = buttonsDict[ButtonLocations]
                #print(ButtonLocationPrintHolder)

    if scene == "start":
        printstart()
        if ButtonLocationPrintHolder == "Play":
            scene = "betting"

    if scene == "betting":
        printbetting()
        #print(ButtonLocationPrintHolder)
        if ButtonLocationPrintHolder == "Bet":
            setupdeck()
            scene = "playing"

    if scene == "playing":
        printplaying()
    #print(scene)

    if scene == "ending":
        if ButtonLocationPrintHolder == "Play":
            scene = "betting"




    #PrintCard(Deck[0])

    ButtonLocationPrintHolder = "Else"
    ButtonLocationFinder = "Else"   #This is the mouse position without a click
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)



pygame.quit()
