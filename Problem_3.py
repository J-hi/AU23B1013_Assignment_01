def get_order(orderlist):
    for i in range(len(orderlist)):
        print('Preparing your order - ',orderlist[i])

    dis=(input('ready to dispatch?(y/n): '))
    if dis=='y' or dis=='Y':
        print('The following orders have been dispatched')
        for i in range(len(orderlist)):
            print(orderlist[i])
    return




orders=[]
while(True):
    print('press 1 to place order / press 2 to escape :',end='')
    press=int(input())
    if press==1:
        orders.append(input('Your order: '))
    elif press==2:
        print()
        break
get_order(orders)
