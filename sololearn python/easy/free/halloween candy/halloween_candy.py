houses = int(input()) 
 
#your code goes here

dollar = (2.0/houses)*100 
integer_dollar = int(dollar)

rounding_differnce = dollar - integer_dollar
if rounding_differnce > 0.0:
    print(integer_dollar+1)
else:
    print(integer_dollar )