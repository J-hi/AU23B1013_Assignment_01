from ice_cream import *
choice=int(input('Welcome, what would you like? press 1 for icream, and 2 for shake: '))
if choice==1:
    scoop=input('What scoop size would you like?')
    top=input('What about toppings?')   
    add_topping(scoop,top)
if choice==2:
    shake=int(input('What kind of shake would you prefer? press 3 for fuits, and 4 for nuts: '))
    make_shake(shake)
