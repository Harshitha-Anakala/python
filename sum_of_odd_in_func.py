n = int(input(" "))
arr = list(map(int, input(" ").split()))
def recursive_sum(arr, n):
    if n <= 0:
        return 0
    else:
        if arr[n - 1] % 2 != 0:
            return arr[n - 1] + recursive_sum(arr, n - 1)
        else:
            return recursive_sum(arr, n - 1)
print(f"{recursive_sum(arr, n)}")
