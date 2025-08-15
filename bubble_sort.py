a = list(map(int,input().split()))
def bubble_sort(a):
    n = len(a)
    for i in range(n): 
        for j in range(i + 1, n):  
            if a[i] > a[j]:  
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
print(bubble_sort(a))