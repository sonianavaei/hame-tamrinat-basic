def permutation(char_list):

    if len(char_list) == 1:
        return [char_list]

    selected = char_list[0]
    permutation_list = permutation(char_list[1:])

    result = []

    for item in permutation_list:
        length = len(item) + 1
        for i in range(length):
            first_part = item[:i]
            second_part = item[i:]
            new_word = first_part + selected + second_part
            result.append(new_word)

    return result


desired_word = input("What's the word? ")
permutations = permutation(desired_word)

for word in permutations:
    print(word)

print(f"Total permutations: {len(permutations)}")
