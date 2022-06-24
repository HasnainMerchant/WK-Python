numbers = [23, 65, 78, 43, 36, 23]
# 1 Program To Find One Even Number from List
for num in numbers:
    if num % 2 == 0:
        print("Found an Even Number....Breaking out of the loop")
        break

# 2 Program To Find Even Numbers and Create New List With Even Numbers
even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)

print(f"Even Number List Is - {even_num}")

# 3