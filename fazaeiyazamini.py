name = input().strip()
char_count = {}

for char in name:
    if char.isalpha():  
        char = char.lower()  
        char_count[char] = char_count.get(char, 0) + 1

unique_non_repeated_count = sum(1 for count in char_count.values() if count == 1)

if unique_non_repeated_count % 2 == 1: 
    print("Alien")
else: 
    print("Human")
