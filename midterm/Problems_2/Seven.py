"""หลักหน่วยของยกกำลัง x"""
def main():
    """input"""
    x = int(input())
    power = [1, 7, 9, 3]

    ans = power[x % 4]

    print(ans)

main()
