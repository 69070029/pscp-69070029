"""พี่มาแล้วน้อง"""
def main():
    """ใส่เลขนะจ๊ะ"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())

    answer = ((q1-p1)**2 + (q2-p2)**2)**(1/2)

    print(answer)

main()
