text = input()
count = 0

for i in text:
    if (i=='a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i=='I'):
        count+=1
print(count)