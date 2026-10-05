"""array hahey"""
num = []
for i in range(3):
    num.append(int(input()))
    print(f"Input number {i + 1} stored.")

ascend = sorted(num)
descend = sorted(num, reverse=True)

while True:
    cmd = int(input())

    if not cmd:
        break
    if cmd == 1:
        print("Original order:", *num)
    elif cmd == 2:
        print("Descending order:", *descend)
    else:
        print("Ascending order:", *ascend)
