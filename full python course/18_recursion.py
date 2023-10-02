def factiorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factiorial_recursive(n-1)

print(factiorial_recursive(5))