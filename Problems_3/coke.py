"""coke"""
def main():
    """input"""
    p_old = int(input())
    cap = int(input())
    p_new = int(input())
    want_coke = int(input())

    taam_ma_taorai = want_coke // cap

    pay = (want_coke - taam_ma_taorai) * p_old + (taam_ma_taorai * p_new)

    print(pay)


main()
