
from collections import deque

def min_knight_moves(n, x1, y1, x2, y2):
    """Calculate the minimum number of knight moves from start to end on a chessboard.

    Args:
    n (int): Size of the chessboard (n x n).
    x1 (int): Starting x-coordinate of the knight.
    y1 (int): Starting y-coordinate of the knight.
    x2 (int): Ending x-coordinate (destination).
    y2 (int): Ending y-coordinate (destination).

    Returns:
    int: Minimum number of moves to reach the target, or -1 if unreachable.
    """
    # Directions representing knight's possible moves
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (2, 1), (1, 2), (-1, 2), (-2, 1)]
   
    # If start and end are the same
    if x1 == x2 and y1 == y2:
        return 0

    # Initialize visited matrix
    visited = [[False] * n for _ in range(n)]
    # Queue for BFS
    queue = deque([(x1, y1, 0)])
    visited[x1][y1] = True

    while queue:
        current_x, current_y, moves = queue.popleft()

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy

            # Check if next position is within bounds and not yet visited
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if nx == x2 and ny == y2:
                    return moves + 1  # Found the target position
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1  # If unreachable

# Example usage:
n = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(min_knight_moves(n, x1, y1, x2, y2))


