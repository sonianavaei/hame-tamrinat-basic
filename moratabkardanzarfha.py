def max_faces_after_flip(plates):
    initial_count = sum(plates)
    max_count = 0  
    for start in range(len(plates)):
        for end in range(start, len(plates)):
            new_count = initial_count
            
            for i in range(start, end + 1):
                if plates[i] == 1:  
                    new_count -= 1  
                else:  
                    new_count += 1  
            max_count = max(max_count, new_count)

    return max_count

input_str = input()  
input_plates = list(map(int, input_str.split())) 

result = max_faces_after_flip(input_plates)  
print(result)  