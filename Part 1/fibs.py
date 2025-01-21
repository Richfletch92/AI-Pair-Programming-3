def fibs(n):
    result = [0, 1]  # Corrected initial values
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

print(fibs(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]