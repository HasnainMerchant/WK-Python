numbers = [23, 65, 78, 43, 36, 23]
# 1
for num in numbers:
    if num % 2 == 0:
        print("Found an Even Number....Breaking out of the loop")
        break

# 2
even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)

print(f"Even Number List Is - {even_num}")