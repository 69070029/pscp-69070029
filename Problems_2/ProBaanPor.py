"""คำนวณโปรโมชั่น"""
def main():
    """ใส่เลข"""
    #โปร
    x = int(input())
    y = int(input())
    #ราคาต่อคน
    a = int(input())
    #มากี่คน
    z = int(input())

    if z == x:
        price = y * a
    elif z > x and z % x:
        price = ((z // x) * y * a) + ((z % x) * a)
    elif z > x and not z % x:
        price = (z // x) * y * a
    else:
        price = z * a

    print(price)

main()
