items ={'coal':{'quantity':160,'unit':'t','unit price':1500},
        'coal eco peas':{'quantity':210,'unit':'t','unit price':1000},
        'culm':{'quantity':260,'unit':'t','unit price':650}}

def get_items():
    name,quantity,unit,unit_price = '{:15}'.format('Name'),'{:^15}'.format('Quantity'),'{:^15}'.format('Unit'),'{:^15}'.format('Unit price')
    print(f"{name}{quantity}{unit}{unit_price}")
    print('{:14}'.format('^'*4),'{:^15}'.format('^'*7),'{:^12}'.format('^'*4),'{:^16}'.format('^'*10))

    for i in items:
        position = items[i]
        nam,qua, uni, uni_pri = '{:15}'.format(i),'{:^13}'.format(position['quantity']), '{:^14}'.format(position['unit']), '{:^15}'.format(
            position['unit price'])
        print(nam, qua, uni, uni_pri)

def add_item(items):
   name = input('What would you like add to warehause?\nItem name:')
   quantity = input('Item quantity:')
   unit = input('item unit:')
   price = input('Item price:')
   items.update({name:{'quantity':quantity,'unit':unit,'unit price':price}})

if __name__ == '__main__':
    while True:
        option=input\
            ("""Menu:\nshow\nexit\nadd\nWhat are you want to do?:""")

        if option == 'exit':
            break

        if option == 'show':
            get_items()

        if option == 'add':
            add_item(items)

    input("exiting... see you! (press Enter)")