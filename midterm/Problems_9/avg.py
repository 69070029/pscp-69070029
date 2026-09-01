"""pass?"""
def main():
    """input"""
    howmuch = int(input())
    mark = []

    for _ in range(howmuch):
        score = int(input())
        mark.append(score)

    avg = sum(mark) / howmuch

    if min(mark) < 50 or avg < 60:
        ans = "FAIL"
    else:
        ans = "PASS"

    print(f"{avg:.1f}")
    print(ans)

main()
