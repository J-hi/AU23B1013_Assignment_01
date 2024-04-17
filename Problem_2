def get_tshirt(brand_name,brand_size):
    brands=['Allen Solly','Van Huesen','Nike','Peter England','Puma','Adidas']
    sizes=[['s','m','l','xl'],['xs','s','m','l','xl'],['s','m','l','xl','xxl'],['s','m','l',],['m','l','xl','xxl','xxxl'],['xs','s','m','l','xl']]
    found=0
    for i in range(len(brands)):
        if brands[i]==brand_name:
            for f in range(len(sizes[i])):
                if sizes[i][f]==brand_size:
                    print('Hi',get_name(),', the brand you are looking for is available in our store in your desired size.')
                    break
                else:
                    print('Hi',get_name(),', the brand you are looking for is available in our store but unfortunately your desired size is not.')
                    break
            found=1
            break
    if found==0:
        print('Hi',get_name(),', Unfortunately the brand you are looking for is not available in our store.')
    return
    
def get_name():
    name=input('Hello user, please enter your name:')
    return name

brand=input('Enter the name of brand you are looking for:')
size=input('What size are you looking for? ')
get_tshirt(brand,size)
