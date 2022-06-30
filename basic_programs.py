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

# 3 Take String from user and count vowels in it
input_str = input("Enter Input String - ")
input_str.casefold()
vowels = "aeiou"
length = 0

num_vowels = [vowel for vowel in input_str if vowel in vowels]
print(f"The Vowels Are - {len(num_vowels)}")

# 4 Count Number of times vowels are repeated
vowel_count = {}.fromkeys(vowels, 0)

for char in input_str:
    if char in vowels:
        vowel_count[char] += 1

print(f"The Vowel Count Are - {vowel_count}")
