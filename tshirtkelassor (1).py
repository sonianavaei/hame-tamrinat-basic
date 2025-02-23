stock = list(map(int, input().split()))

n = int(input())

results = []

sizes = {'S': 0, 'M': 1, 'L': 2, 'XL': 3, 'XXL': 4}

for _ in range(n):
    desired_size = input()
    index = sizes[desired_size]
    
    if stock[index] > 0:
        results.append(desired_size)
        stock[index] -= 1  
    else:
        found = False
        for offset in range(1, 3):  
            if index + offset < len(stock) and stock[index + offset] > 0:
                results.append(list(sizes.keys())[index + offset])  
                stock[index + offset] -= 1
                found = True
                break
            if index - offset >= 0 and stock[index - offset] > 0:
                results.append(list(sizes.keys())[index - offset])  
                stock[index - offset] -= 1
                found = True
                break
        
        if not found:
            results.append("No Shirt")

for result in results:
    print(result)
