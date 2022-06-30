numbers = [23, 65, 78, 43, 36, 23]
def even_num(nums):
    # 1 Program To Find One Even Number from List
    for num in numbers:
        if num % 2 == 0:
            print("Found an Even Number....Breaking out of the loop")
            return  -1

def new_list_even_num(nums):
    # 2 Program To Find Even Numbers and Create New List With Even Numbers
    even_num = []
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)
    return even_num

even_num(numbers)
print(new_list_even_num(numbers))

input_str = input("Enter Input String - ")
input_str.casefold()

def count_vowels(input):
# 3 Take String from user and count vowels in it
    vowels = "aeiou"
    num_vowels = [vowel for vowel in input if vowel in vowels]
    print(f"The Vowels Are - {len(num_vowels)}")

def vowel_count(input):
    # 4 Count Number of times vowels are repeated
    vowels = "aeiou"
    vowel_count = {}.fromkeys(vowels, 0)
    for char in input_str:
        if char in vowels:
            vowel_count[char] += 1
    print(f"The Vowel Count Are - {vowel_count}")

count_vowels(input_str)
vowel_count(input_str)
