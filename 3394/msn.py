"""message"""
n, first = map(int, input().split())
send_to = [int(input()) for _ in range(n)]

current = send_to[first-1] #เลขปจบ (เลขที่บอกว่าจะส่งไปที่ใคร)
current_idx = first - 1 #index เลขปจบ
sent = [] #เคยรับแล้ว
receive = 0 #ได้รับกี่คน

while True:
    if current_idx in sent:
        break

    sent.append(current_idx) #เพิ่มตำแหน่งที่เคยรับข้อความแล้ว
    receive += 1 # เพิ่มคนที่ได้รับ

    if not current:
        break

    current_idx = current - 1
    current = send_to[current - 1] #ส่งต่อไปที่ใคร

print(receive)
