"""rabbit language"""
speak = input().lower()

if all(word in "it" for word in speak):
    print("unknown", len(speak))
else:
    ans = "yes"
    for i, word in enumerate(speak):
        if word not in "rabit":
            ans = "no"
            print(ans, i)
            break
        if word == "a":
            if not i or speak[i-1] not in "ra":
                ans = "no"
                print(ans, i)
                break
        if word == "r":
            if (i + 1 < len(speak) and speak[i + 1] not in "a") or i == len(speak) - 1:
                ans = "no"
                print(ans, i + 1)
                break
        if word == "b":
            if ((i + 1 < len(speak) and speak[i + 1] not in "it") or i == len(speak) - 1):
                ans = "no"
                print(ans, i + 1)
                break

    if ans == "yes":
        a_max = 0
        a_count = 0
        for i, word in enumerate(speak):
            if word == "a":
                a_count += 1
                a_max = max(a_max, a_count)
            else:
                a_count = 0

        print(ans, a_max)
