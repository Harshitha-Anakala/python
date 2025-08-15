n = int(input( ))
def Fibonocci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonocci(n - 1) + Fibonocci(n - 2)
print(f"{Fibonocci(n)}")
