"""นับจำนวน d"""
def main():
    """input"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    ans = 0

    for i in range(A, B+1):
        if i % d == r:
            ans += 1

    print(ans)

main()
