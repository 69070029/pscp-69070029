"""สมดุลย์ชีวิต"""
total = int(input())

time = []
day = 0
current_hr = 0

for _ in range(total):
    time.append(int(input()))

while len(time) > 0:
    if current_hr > 18:
        if min(time) <= 18:
            current_hr = min(time)
            time.remove(min(time))
        else:
            current_hr = 0
    else:
        current_hr = max(time)
        time.remove(max(time))

    day += 1

print(day)
