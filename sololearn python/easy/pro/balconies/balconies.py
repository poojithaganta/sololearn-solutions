inp = list(map(int,input().strip().split(",")))
inp_two = list(map(int,input().strip().split(",")))

area_one = inp[0] * inp[1]
area_two = inp_two[0] * inp_two[1]

if area_one>area_two:
    print("Apartment A")
else:
    print("Apartment B")