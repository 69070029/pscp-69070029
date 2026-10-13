"""ma pen team"""
group, mem = map(int, input().split())

total = 0
ans = []

if group < 1 or group > 10 or mem < 1 or mem > 20:
    print("Data Incorrect")
else:
    for i in range(group):
        score = list(map(int, input().split()))

        ans.append(f"Team {i + 1}: Average = {sum(score)/mem:.2f}, Max = {max(score)}")
        total += sum(score)

    print(*ans, sep="\n")
    print(f"Total Score of All Teams = {total}")
