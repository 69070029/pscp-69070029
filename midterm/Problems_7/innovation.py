"""งบ"""
def main():
    """input"""
    school = input()

    first = ord(school[0].upper())
    last = ord(school[-1].upper())

    password = []

    for i in range(10):
        #1
        if (i + 1) % 2:
            ans = i + first
        else:
            ans = last - i

        #2
        ans = ans % len(school)

        ans = ans % 10

        password.append(ans)

    #3
    result = password[2:8]

    print(*result, sep = " ")

main()
