"""coke"""
def main():
    """input"""
    p_old = int(input())
    cap = int(input())
    p_new = int(input())
    want_coke = int(input())

    taam_ma_taorai = want_coke // cap

    pay = ((want_coke - taam_ma_taorai) * p_old) + (taam_ma_taorai * p_new)
    print(pay)

main()

    #((จำนวนที่ต้องการ - จำนวนของแถม) * ราคาเดิม) + (จำนวนของแถม * ราคาใหม่)
    #จำนวนของแถม = จำนวนที่ต้องการ - จำนวนที่ซื้อ
    #ต้องการกี่ขวด -> เอาจำนวนขวดที่ซื้อเดิม + ขวดที่ได้แถม
    #1 ขวด ใช้ cap ฝา
    #เอาจำนวนทั้งหมดหาร cap 
    #ทั้งหมดมี 10 ขวด แลกขวดละ 4 ฝา -> คำตอบคือ 2 -> จากขวดทั้งหมด มีแถมมา 2 ขวด