"""RECTANGLEAREA"""
def main():
    """input"""
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # x,y มุมซ้ายล่าง กว้าง สูง

    width = max(0,min(A[0] + A[2], B[0]  + B[2]) - max(A[0],B[0]))
    length = max(0,min(A[1] + A[3], B[1]  + B[3]) - max(A[1],B[1]))

    area = width * length

    if area > 0:
        ans = area
    else:
        ans = "no overlapping"

    print(ans)

main()
