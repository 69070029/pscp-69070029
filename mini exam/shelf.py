"""book shelf"""
shelf = list(input().split())
take = input()

if take not in shelf:
    print("There are no book with that name on this shelf")
else:
    shelf.remove(take)
    print(*shelf)
