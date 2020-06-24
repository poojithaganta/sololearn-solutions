text = input().split()
total = 0

for i in text:
    if i=='Lettuce':
        total+=5
    if i=='Carrot':
        total+=4
    if i=='Mango':
        total+=9
    if i=='Cheeseburger':
        total+=0
if total>=10:
    print('Come on Down!')
else:
    print("Time to wait")