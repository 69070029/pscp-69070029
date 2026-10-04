"""plastic, can, glass"""
machine = int(input())
mat = ["Plastic", "Can", "Glass"]

for _ in range(machine):
    weight = list(map(float, input().split()))
    status = []

    for i in range(len(weight)):
        if weight[i] > 20:
            status.append(f"Check Type {mat[i]}")

    if sum(weight) > 50:
        status.append("Overloaded")

    status.reverse()

    print(sum(weight), *status, sep=", ")
