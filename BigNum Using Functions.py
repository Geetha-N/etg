a = 5
b = 3
c = 7
def bigger_nums(a,b,c):
    if a < b and a < c:
        return b,c
    elif b < a and b < c:
        return a,c
    else:
        return a,b

print(bigger_nums(a,b,c))
    
