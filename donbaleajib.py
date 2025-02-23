def get_nth_digit(n):
    index = 0   
    power_of_ten = 1   
    digit_pos = 0 
    
    while True:
        digits_count = len(str(power_of_ten))
        
        if digit_pos + digits_count >= n:
            current_number = str(power_of_ten)
            return current_number[n - digit_pos - 1]  
        
        digit_pos += digits_count
        power_of_ten *= 10  

n = int(input())
result = get_nth_digit(n)
print(result)
