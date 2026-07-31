"""BASIC ATM"""
def main():
    """input"""
    money = int(input())

    grey = 0
    purple = 0
    red = 0

    if money % 100:
        print("ERROR")
    else:
        while 100 <= money <= 20000:
            if not money % 1000:
                pun = money / 1000
                grey += pun
            elif 
main()
