"""GG-EZ"""
game = input()
diff = int(input())

if game == "Valorant":
    if diff >= 7:
        print("GGEZ")
    else:
        print("GGWP")
else:
    if diff >= 2:
        print("GGEZ")
    else:
        print("GGWP")
