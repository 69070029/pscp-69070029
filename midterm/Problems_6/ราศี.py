"""ราศี"""
def main():
    """input"""
    day = int(input())
    month = int(input())

    if month == 12:
        ans = "capricorn" if (day >= 22) else "sagittarius"
    elif month == 1:
        ans = "capricorn" if (day <= 19) else "aquarius"
    elif month == 2:
        ans = "aquarius" if (day <= 18) else "pisces"
    elif month == 3:
        ans = "pisces" if (day <= 20) else "aries"
    elif month == 4:
        ans = "aries" if (day <= 19) else "taurus"
    elif month == 5:
        ans = "taurus" if (day <= 20) else "gemini"
    elif month == 6:
        ans = "gemini" if (day <= 21) else "cancer"
    elif month == 7:
        ans = "cancer" if (day <= 22) else "leo"
    elif month == 8:
        ans = "leo" if (day <= 22) else "virgo"
    elif month == 9:
        ans = "virgo" if (day <= 22) else "libra"
    elif month == 10:
        ans = "libra" if (day <= 23) else "scorpio"
    else:
        ans = "scorpio" if (day <= 21) else "sagittarius"

    print(ans)

main()
