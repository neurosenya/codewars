# Returns True if A contains item and False otherwise
def binary_search(A, item):
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
        if A[middle] > item:
            return binary_search(A[:middle], item)
        else:
            return binary_search(A[middle + 1:], item)

numbers = [1, 2, 3, 5, 8, 22, 34, 42]
print(binary_search(numbers, 4))
print(binary_search(numbers, 42))

