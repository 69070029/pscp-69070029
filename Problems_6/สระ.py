"""สระ"""
def main():
    """input"""
    loop = int(input())
    count = 0
    for _ in range(loop):
        letter = input().upper()
        if letter in ['A' , 'E' , 'I' , 'O' , 'U']:
            count += 1
    print(count)
main()
