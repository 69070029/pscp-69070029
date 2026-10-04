"""plastic, can, glass"""
machine = int(input())
mat = ["Plastic", "Can", "Glass"]

for _ in range(machine):
    weight = list(map(float, input().split()))
    status = []

    for i,trash in enumerate(weight):
        if trash > 20:
            status.append(f"Check Type {mat[i]}")

    if sum(weight) > 50:
        status.insert(0, "Overloaded")

    print(f"{sum(weight):.1f}", *status, sep=", ")
