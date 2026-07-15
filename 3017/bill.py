"""ค่าอาหาร"""
def main():
    """ค่าอาหารทั้งหมด"""
    cost = int(input())
    service = cost * 0.1

    if cost > 10000:
        total = cost + 1000 + ((cost + 1000) * 0.07)
    elif cost < 500:
        total = cost + 50 + ((cost + 50) * 0.07)
    else:
        total = cost + service + ((cost + service) * 0.07)

    print(f"{total:.2f}")

main()
