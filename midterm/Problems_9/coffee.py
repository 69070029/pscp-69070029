"""coffee"""
def main():
    """input"""
    day = int(input())

    box = []

    for _ in range(day):
        sold = int(input())
        box.append(sold)

    avg = sum(box) / day

    print(sum(box))
    print(max(box))
    print(min(box))
    print(f"{avg:.1f}")

main()
