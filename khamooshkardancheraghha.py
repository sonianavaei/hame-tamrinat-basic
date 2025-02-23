press_counts = [list(map(int, input().split())) for _ in range(3)]

final_state = [[1]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if press_counts[i][j] % 2 == 1: 
            final_state[i][j] = 1 - final_state[i][j]  
            if i > 0:
                final_state[i-1][j] = 1 - final_state[i-1][j]  
            if i < 2:
                final_state[i+1][j] = 1 - final_state[i+1][j]  
            if j > 0:
                final_state[i][j-1] = 1 - final_state[i][j-1]  
            if j < 2:
                final_state[i][j+1] = 1 - final_state[i][j+1]  

for row in final_state:
    print(*row)
