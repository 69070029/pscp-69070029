"""input"""
a = int(input())
b = int(input())
goal = int(input())
b_bridge = b * 5

d = goal - (goal // b_bridge * 5)

print(d)
#ans = goal - d

#print(ans)
