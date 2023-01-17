# Checks to see if your customer can buy a drink based on 
# age and number of drinks (has to be under max of 4)

a = 24
ds = 3

if a < 21:
    not_old = True
else:
    not_old = False

if (not not_old==True) and (ds < 4):
    print('can buy a drink')
