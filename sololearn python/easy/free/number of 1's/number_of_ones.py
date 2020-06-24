from collections import Counter
number = int(input())

binary_number = bin(number)

result = Counter(binary_number)

res = result.get("1")

print(res)