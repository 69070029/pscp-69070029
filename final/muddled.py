"""Muddled Menu"""
course = []

while True:
    order = input()
    if order == "CLOSED":
        course.clear()
        break
    if order == "DONE":
        break

    if order == "SOMETHING'S WRONG":
        course.clear()
        continue

    if order.startswith("Can't do: "):
        food_name = order[len("Can't do: "):]
        course = [food for food in course if food.split("#")[0].strip() != food_name]
        continue

    food, num = order.split("#")
    food = food.strip()

    if order[-1] == "N":
        course.append(food)
    else:
        course.insert(int(num) - 1, food)

print(f"Full Course: {course} Reversed: {course[::-1]}")
