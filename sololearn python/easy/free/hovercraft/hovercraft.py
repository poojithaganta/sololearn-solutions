sales = int(input())

investment = 10 * 2000000 + 1000000
sales_month = sales * 3000000 

if sales_month < investment  :
    print("Loss")
elif sales_month == investment :
    print ("Broke Even")
elif sales_month > investment :
    print("Profit")