"""thaiplus"""
def main():
    """input"""
    name = input()
    age = int(input())
    salary = int(input())
    status = input() #Y/N
    family = int(input())

    if age < 18:
        print(f"{name} NOT ELIGIBLE")
    else:
        if status == "Y" or salary <= 15000:
            if family >= 3:
                print(f"{name} GOLD 3500")
            else:
                print(f"{name} GOLD 3000")
        elif salary <= 30000:
            if family >= 3:
                print(f"{name} SILVER 2000")
            else:
                print(f"{name} SILVER 1500")
        else:
            print(f"{name} NOT ELIGIBLE")

main()
