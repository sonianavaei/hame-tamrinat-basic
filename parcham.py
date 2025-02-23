def count_ways(n):
    if n == 1:
        return 2  
    elif n == 2:
        return 2  
    
    prev2 = 2  
    prev1 = 2  
    
    for i in range(3, n + 1):
        current = prev1 + prev2  
        prev2 = prev1
        prev1 = current

    return prev1  

def main():
    n = int(input().strip())
    result = count_ways(n)
    print(result)

main()
