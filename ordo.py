def find_missing_number(numbers):
    n = len(numbers)  
    total_sum = (n + 1) * (n + 2) // 2  
    current_sum = sum(numbers)  
    missing_number = total_sum - current_sum  
    return missing_number

input_numbers = list(map(int, input().split()))
missing_number = find_missing_number(input_numbers)
print(missing_number)
