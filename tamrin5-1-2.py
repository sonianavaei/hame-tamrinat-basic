
def binary_search(arr, target):
    """Perform binary search to determine if target exists in a sorted list.
   
    Args:
    arr (list of int): Sorted list of employee IDs.
    target (int): The employee ID to search for.

    Returns:
    str: "Yes" if target exists in the list, otherwise "No".
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return "Yes"  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Discard left half
        else:
            right = mid - 1  # Discard right half

    return "No"  # Target not found

# Input Reading
n = int(input())  # Number of employees
arr = [int(input()) for _ in range(n)]  # Sorted employee IDs
target = int(input())  # ID to search for

# Perform binary search and print result
print(binary_search(arr, target))

