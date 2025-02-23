def hanoi(n, source, destination, auxiliary):
    """
    Solves the Tower of Hanoi problem using recursion.

    Args:
        n: The number of disks.
        source: The source peg (A, B, or C).
        destination: The destination peg (A, B, or C).
        auxiliary: The auxiliary peg (A, B, or C).
    """
    if n == 1:
        print(f"{source}>{destination}")
    else:
        hanoi(n - 1, source, auxiliary, destination)
        print(f"{source}>{destination}")
        hanoi(n - 1, auxiliary, destination, source)

# Get input from user
n = int(input())

# Call the function to print the steps
hanoi(n, 'A', 'C', 'B')
