"""triangle"""
def main():
    """input"""
    a = int(input())
    b = int(input())
    c = int(input())

    if not (a + b > c and a + c > b and b + c > a):
        print("NOT A TRIANGLE")
    else:
        if a == b == c:
            shape = "EQUILATERAL"
        elif a == b or b == c or a == c:
            shape = "ISOSCELES"
        else:
            shape = "SCALENE"

        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            print("RIGHT TRIANGLE")
        else:
            print(shape)

main()
