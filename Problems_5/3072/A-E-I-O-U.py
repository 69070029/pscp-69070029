"""A-E-I-O-U"""
word = input().lower()
a = 0
e = 0
i = 0
o = 0
u = 0

for j in word:
    if j == "a":
        a += 1
    if j == "e":
        e += 1
    if j == "i":
        i += 1
    if j == "o":
        o += 1
    if j == "u":
        u += 1

if a > 0:
    print(f"a : {a}")
if e > 0:
    print(f"e : {e}")
if i > 0:
    print(f"i : {i}")
if o > 0:
    print(f"o : {o}")
if u > 0:
    print(f"u : {u}")
