"""B - Fully Pair?"""
ppl = input()

pair = list(ppl)

if all(not pair.count(x) % 2 for x in pair):
    print("fully paired")
else:
    result = ""

    alr_count = []

    for alpha in pair:
        current_alpha = ""
        count = 0

        if alpha in alr_count:
            continue

        current_alpha = alpha
        count = pair.count(alpha)

        if count % 2:
            result += alpha

        alr_count.append(current_alpha)

    print(result)
