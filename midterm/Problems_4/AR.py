""";งกลท"""
def main():
    """input"""
    rxy = input().split()
    #print(int(rxy[0]))

    if int(rxy[1])**2 + int(rxy[2])**2 > int(rxy[0])**2:
        print("OUT")
    elif int(rxy[1])**2 + int(rxy[2])**2 == int(rxy[0])**2:
        print("ON")
    else:
        print("IN")
main()
