"""saitama Z"""
def main():
    """input"""
    pushup = int(input())
    situp = int(input())
    luknung = int(input())
    run = int(input())

    pu_day = int(input())
    su_day = int(input())
    run_day = int(input())
    ln_day = int(input())

    ans = max(pushup/pu_day, situp/su_day, luknung/ln_day, run/run_day)

    result = int(ans)
    if ans > result:
        result +=1

    print(result)

main()
