"""pod"""
def main():
    """input"""
    ppl = list(map(int, input().split()))

    box = [0] * ppl[1]

    for _ in range(ppl[0]):
        row = int(input())
        box[row - 1] += 1

        if all(box):
            for i in range(ppl[1]):
                box[i] -= 1

    print(sum(box))

main()
