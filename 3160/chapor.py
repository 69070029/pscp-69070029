"""jamnuan chapor"""
def main():
    """input"""
    start, end = map(int, input().split())

    total = 0
    prime = []

    for i in range(start, end + 1):
        if i < 2:
            continue
        for j in range(2, i):
            if not i % j:
                break
        else:
            total += 1
            prime.append(i)

    if prime:
        print(*prime)
    print(f"Total primes: {total}")

main()
