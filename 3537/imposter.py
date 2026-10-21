"""amogus"""
import ast

station = {}

while True:
    member = input()

    if member == "Start":
        break

    member = ast.literal_eval(member)

    station.update(member)

kicked = {}

while True:
    vote = input()

    if vote == "End":
        break

    if vote in station:
        kicked[vote] = station.pop(vote)

station = dict(sorted(station.items()))
kicked = dict(sorted(kicked.items()))

print(f"{sum(1 for x in station.values() if x == 'Impostor')} Impostor Remains")

print("***Alive***")
for ppl, role in station.items():
    print(f"{ppl} : {role}")

print("***Dead***")
for ppl, role in kicked.items():
    print(f"{ppl} : {role}")
