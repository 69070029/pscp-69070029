"""Muddled Menu"""
course = []

while True:
    order = input()
    if order == "SOMETHING'S WRONG":
        course.clear()
        continue
    if order == "CLOSED":
        course.clear()
        break
    if "Cant't do: " in order:
        course.remove(food for food in course if food in order)
        continue
    if order == "DONE":
        break

    if order[-1].isdigit():
        course.insert(int(order[-1]), order[:-3])
    else:
        course.append(order[:-3])

print(course)