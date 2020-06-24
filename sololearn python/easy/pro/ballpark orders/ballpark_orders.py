inp = input().split()
total = 0

for i in inp:
    if i == 'Pizza' or i == 'Nachos':
        total+=6.00
    if i == 'Cheeseburger':
        total+=10.00
    if i== 'Water':
        total += 4.00
    if i == 'Coke':
        total+=5.00
    if i not in ['Pizza','Nachos','Cheeseburger','Water','Coke']:
        total+=5.00
print(total+(total*7/100))