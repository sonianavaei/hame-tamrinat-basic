import copy


def absolute(num, tree, first):
    if 2 ** len(first) == len(tree):
        return max(tree)

    for i in range(len(num)):
        current_num = num[i]
        new_tree = []

        for k in range(len(tree)):
            add = tree[k] + current_num
            absl = abs(tree[k] + current_num)

            new_tree.append(add)
            new_tree.append(absl)

        new_num = num[:i] + num[i + 1 :]
        return absolute(new_num, new_tree, first)


num_of_lists = int(input())
lists = []
for _ in range(num_of_lists):
    given_numbers = list(map(int, input().split()))
    lists.append(given_numbers)

tree = [0]
results = []
for given_numbers in lists:
    first = given_numbers.copy()
    result = absolute(given_numbers, tree, first)
    results.append(result)

results = list(map(str, results))
print("\n".join(results))
