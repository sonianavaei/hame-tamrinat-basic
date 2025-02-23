def compress_string(string):
    compressed = ""
    count = 0

    for i in range(len(string)):
        count += 1
        
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed += string[i]
            if string[i] != ' ':  
                compressed += str(count)
            count = 0  
    return compressed

input_string = input()
output_string = compress_string(input_string)
print(output_string)
