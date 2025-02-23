def is_valid_bracket_string(s):
    stack = []  

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char) 
        elif char == ')' or char == ']' or char == '}':
            if not stack: 
                return False  
            top = stack.pop()  
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False 
    return len(stack) == 0  

input_string = input()
print(is_valid_bracket_string(input_string))
