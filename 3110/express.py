"""EXPRESS"""
def main():
    """input"""
    path = input().split()
    weight = float(input())

    schedule = {
        "BKK": {"CNX": "10 30", "PKT": "25 50"},
        "CNX": {"UBP": "15 40"},
        "UBP": {"BKK": "20 40", "PKT": "40 70"},
        "PKT": {"CNX": "30 60"}
    }

    if path[0] in schedule and path[1] in schedule[path[0]]:
        result = schedule[path[0]][path[1]]

        pay = int(result[:2]) + int(result[-2:]) * weight

        print(f"{pay:.2f}")
    else:
        print("Error")

main()
