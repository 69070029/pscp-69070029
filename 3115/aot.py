"""arcade of time"""
def main():
    """input"""
    shop, check = map(int, input().split())

    for _ in range(shop):
        open, close = map(int, input().split())

    c_time = list(map(int, input().split()))
    print(len(c_time))
    #for _ in range(len(c_time))


main()
