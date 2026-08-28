"""Password Generator"""
def main():
    """input"""
    name = str(input())
    surname = str(input())
    age = str(input())

    if len(name) >= 5 and len(surname) >= 5:
        print(f"{name[:2]}{surname[-1:]}{age[-1:]}")
    else:
        print(f"{name[:1]}{age}{surname[-1:]}")

main()
