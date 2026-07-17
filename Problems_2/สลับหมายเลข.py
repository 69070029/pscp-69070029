"""สลับหมายเลข"""
def main():
    """input"""
    num_1 = input()
    num_2 = num_1[::-1]
    op = input()

    if op == "+" and num_1[-1] != "0":
        ans = int(num_1) + int(num_2)
        print(f"{num_1} + {num_2} = {ans}")
    elif op == "+" and num_1[-1] == "0":
        ans = int(num_1) + int(num_2)
        print(f"{num_1} + {num_2[-1]} = {ans}")

    if op == "*" and num_1[-1] != "0":
        ans = int(num_1) * int(num_2)
        print(f"{num_1} * {num_2} = {ans}")
    elif op == "*" and num_1[-1] == "0":
        ans = int(num_1) * int(num_2)
        print(f"{num_1} * {num_2[-1]} = {ans}")

main()
