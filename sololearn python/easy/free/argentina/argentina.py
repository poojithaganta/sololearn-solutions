pesos = int(input())
dollar = int(input())

answer = (pesos*2)/100
if answer<= dollar:
    print ("Pesos")
else:
    print("Dollars")