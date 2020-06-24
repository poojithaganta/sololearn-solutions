def landho(num):
    time = 10
    if num<20:
        return time
    while num>=20:
        num -= 20
        time += 20
        if num<20 and num>0:
             break
    return time 
n = int(input())
print(landho(n))