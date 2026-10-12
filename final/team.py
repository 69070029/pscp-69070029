"""ma pen team"""
group, mem = map(int, input().split())

total = 0
ans = []

for i in range(group):
    score = list(map(int, input().split()))

    if len(score) != mem or any(isinstance(x, str) for x in score):
        ans.append("no")
        break

    ans.append(f"Team {i + 1}: Average = {sum(score)/mem:.2f}, Max = {max(score)}")
    total += sum(score)

if "no" in ans:
    print("Data Incorrect")
else:
    print(*ans, sep="\n")
    print(f"Total Score of All Teams = {total}")
