"""Frame"""
def main():
    """Input"""
    text = str(input())

    print("*" * (len(text) + 2))
    print(f"*{text}*")
    print("*" * (len(text) + 2))

main()
