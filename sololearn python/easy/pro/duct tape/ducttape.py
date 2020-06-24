import math

height = int(input())
width = int(input())

height *= 12
width *= 12

height /= 2

total = ((height * width)*2)/720

print(math.ceil(total))