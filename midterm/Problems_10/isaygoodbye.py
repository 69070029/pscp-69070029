"""samliam"""
def main():
    """input"""
    taorai = int(input())

    for i in range(1, taorai + 1):

        if i in  [1, taorai]:
            tri = "0" * i
        else:
            tri = "0" + ("1" * (i - 2))+"0"

        print(tri)
main()
