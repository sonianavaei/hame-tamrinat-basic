list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

if len(list_a) != len(list_b):
    print("NO")
else:
    differences = [b - a for a, b in zip(list_a, list_b)]
    
    start = None
    end = None
    
    for i in range(len(differences)):
        if differences[i] != 0:
            if start is None:
                start = i
            end = i
            
    if start is not None and end is not None:
        k = differences[start]
        if k < 0:
            print("NO")
        else:
            for i in range(start, end + 1):
                if differences[i] != k:
                    print("NO")
                    break
            else:
                print("YES")
    else:
        print("YES")
