"""Muddled Menu"""
course = []
last = []

def riang(x):
    """key"""
    return int(x[x.index("#") + 1:])

while True:
    order = input()
    if order == "SOMETHING'S WRONG":
        course.clear()
        last.clear()
        continue
    if order == "CLOSED":
        course.clear()
        last.clear()
        break
    if "Can't do: " in order:
        course = [food for food in course if order[10:] not in food]
        last = [food for food in last if order[10:] not in food]
        continue
    if order == "DONE":
        break

    if order[-1].isdigit():
        course.insert(riang(order) - 1, order)
    else:
        last.append(order)

course.extend(last)

course = [food[:food.index("#") - 1] for food in course]

print(f"Full Course: {course} Reversed: {course[::-1]}")
