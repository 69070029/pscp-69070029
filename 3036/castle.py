"""prasart"""
import math

def main():
    """input"""
    room = int(input())

    #หาแถวของเลขห้อง
    row = math.ceil(math.sqrt(room))

    if row % 2:
        if room % 2: #ห้องคี่
            wall = 2 * row - 2
        else: #ห้องคู่
            wall = 2 * row - 3
    else: #แถวคู่
        if room % 2: #ห้องคี่
            wall = 2 * row - 3
        else: #ห้องคู่
            wall = 2 * row - 2

    print(wall)

main()
