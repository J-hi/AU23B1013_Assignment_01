def add_topping(scoop_size, topping):
    scoops=['single','double','triple']
    toppings=['sprinkles','hot fudge','whipped cream','crushed nuts','no']
    i=0
    while i<len(toppings):
        if topping==toppings[i]:
            break
        i+=1
    if i==len(toppings):
        print('Sorry, the requested topping is not available')       
    else:
        return print('Your order is ready')

def make_shake(choice):
    nuts=['almond','cashew','pistachio']
    fruits=['mango','banana','apple','pineapple','strawberry','blueberry']
    
    available=0
    if choice==4:
        t=input('Enter your preferred nut: ')
        for i in range(len(nuts)):
            if nuts[i]==t:
                available=1
                break
    elif choice==3:
        t=input('Enter your preferred fruit: ')
        for i in range(len(fruits)):
            if fruits[i]==t:
                available=2
                break

    if available==0:
        return print('Sorry, the requested shake is not available.')
    
    else:
        return print('Your order is ready.')
