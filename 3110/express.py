"""EXPRESS"""
def main():
    """input"""
    path = input().split()
    weight = float(input())

    start = ['BKK', 'CNX', 'UBP', 'BKK', 'PKT', 'UBP']
    end = ['CNX', 'UBP', 'BKK', 'PKT', 'CNX', 'PKT']

    print(start.index(path[0]))
main()
