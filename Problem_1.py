def get_tshirt(brand_name):
    brands=['Allen Solly','Van Huesen','Nike','Peter England','Puma','Adidas']
    found=0
    for i in brands:
        if i==brand_name:
            print('Hi',get_name(),', the brand you are looking for is available in our store.')
            found=1
            break
    if found==0:
        print('Hi',get_name(),', Unfortunately the brand you are looking for is not available in our store.')
        return
    
def get_name():
    name=input('Hello user, please enter your name:')
    return name

brand=input('Enter the name of brand you are looking for:')
get_tshirt(brand)
