"""Filter"""
import ast

score = ast.literal_eval(input())
score = dict(sorted(score.items()))
cut = float(input())

if all(value < cut for value in score.values()):
    print("Nope")
else:
    for rahus, value in score.items():
        if value >= cut:
            print(f"{rahus}\t{value:.2f}")
