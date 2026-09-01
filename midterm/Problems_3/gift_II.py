"""กระดาษห่อของขวัญ"""
def main():
    """input"""
    gift = list(map(float, input().split()))

    paper_w = gift[1] + (gift[0] * 2)
    paper_l = (2 * 3.14 * gift[0]) + gift[2]

    print(f"{paper_w:.2f} {paper_l:.2f}")

main()
