import random
#Suit, Type, Value
Deck = [
"DA","D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ","DQ","DK",
"HA","H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ","HQ","HK",
"CA","C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ","CQ","CK",
"SA","S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ","SQ","SK"
]
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
    if Card_Type in "23456789":
        Card_Value = Card_listed[1]
    elif Card_Type in "TJQK":
        Card_Value = 10
    elif Card_Type == "A":
        Card_Value = 1

    return str(Card_Suit)+"-"+str(Card_Type)+"-"+str(Card_Value)

for x in range(100000):
    Shuffler_Number_1 = random.randint(0, (len(Deck)-1))
    Shuffler_Holder_1 = Deck[Shuffler_Number_1]
    Shuffler_Number_2 = random.randint(0, (len(Deck)-1))
    Shuffler_Holder_2 = Deck[Shuffler_Number_2]
    Deck[Shuffler_Number_2] = Shuffler_Holder_1
    Deck[Shuffler_Number_1] = Shuffler_Holder_2

for c in range(52):
    print(Card_Info(Deck[c]))
