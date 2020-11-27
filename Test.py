Players = ["Scott", "Malcolm", "Tony", "Kevin", "Julia", "John", "Paul", "Bob"]
Players_nottaken = ["Scott", "Malcolm", "Tony", "Kevin", "Julia", "John", "Paul", "Bob"]

Player_Thresholds = {
"Scott" : 4,
"Malcolm" : 13,
"Tony" : 40,
"Kevin" : 9,
"Julia" : 17,
"John" : 21,
"Paul" : 15,
"Bob" : 14
}




Comp1_Player = 1
Comp2_Player = 2
Comp3_Player = 3
Comp1_Threshold = Player_Thresholds[Players[Comp1_Player-1]]
Comp1_Threshold = Player_Thresholds[Players[Comp2_Player-1]]
Comp1_Threshold = Player_Thresholds[Players[Comp3_Player-1]]






for i in range(6):
    Players_taken = [Players[Comp3_Player-1], Players[Comp2_Player-1], Players[Comp1_Player-1]]
    for i in Players_taken:
        if i in Players_nottaken:
            Players_nottaken.remove(i)

    

    print(Players)
    print(Players_taken)
    print(Players_nottaken)
    print("\n")
    Comp1_Player += 1
    print(Comp1_Player)
