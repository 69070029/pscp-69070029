"""สอบ"""
def main():
    """กระตุ่ย"""
    count = int(input())
    list_score = []
    for _ in range(count):
        score = int(input())
        list_score.append(score)
    most = max(list_score)
    print(most)
    print(list_score.count(most))
main()
