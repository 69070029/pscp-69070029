"""ตัวเลขโรมัน"""
def main():
    """input"""
    num = int(input())

    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    if num > 9 or not num:
        ans = "Error : Out of range"
    elif num < 0:
        ans = "Error : Please input positive number"
    else:
        ans = roman[num - 1]

    print(ans)
main()
