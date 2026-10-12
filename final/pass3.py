"""rahus mai sum gun"""
taorai = int(input())
password = list(map(int, input().split()))

ans = [x for x in password if password.count(x) == 1]

print(*sorted(ans))
