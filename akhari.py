def max_possible_c(test_cases):
    results = []
    for a in test_cases:
        c = 0
        for num in a:
            # محاسبه دو حالت ممکن
            c_with_abs = abs(c + num)
            c_without_abs = c + num
            # انتخاب حالتی که بیشترین مقدار را دارد
            c = max(c_with_abs, c_without_abs)
        results.append(c)
    return results

# تست‌های ورودی:
input_data = [
    [10, -9, -3, 4],
    [1, 4, 3, 4, 1, 4, 3, 4],
    [-1, -2, -3],
    [-1000000000, 1000000000, 1000000000, 1000000000],
    [1, 9, 8, 4],
    [-1, -1, 0, -1, 1, 1],
    [-1, -1, 0, 1, -1, -1, 1],
    [-5, 2, 4, -11, 7, 2]
]

# محاسبه و نمایش خروجی‌ها
results = max_possible_c(input_data)
for result in results:
    print(result)
    