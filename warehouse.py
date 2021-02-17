def get_items():
    name,quantity,unit,unit_price = '{:15}'.format('Name'),'{:^15}'.format('Quantity'),'{:^15}'.format('Unit'),'{:^15}'.format('Unit price')
    print(f"{name}{quantity}{unit}{unit_price}")
    print('{:14}'.format('^'*4),'{:^15}'.format('^'*7),'{:^12}'.format('^'*4),'{:^16}'.format('^'*10))

    for i in items:
        position = items[i]
        nam,qua, uni, uni_pri = '{:15}'.format(i),'{:^13}'.format(position['quantity']), '{:^14}'.format(position['unit']), '{:^15}'.format(
            position['unit price'])
        print(nam, qua, uni, uni_pri)
    print(f'Inventory value:{inventory_value}')

def add_item(items):
   name = input('What would you like add to warehouse?\nItem name:')
   quantity = int(input('Item quantity:'))
   unit = input('item unit:')
   price = int(input('Item price:'))
   items.update({name:{'quantity':quantity,'unit':unit,'unit price':price}})

def get_item_to_sold_items(sold_items,name,quantity,unit,price):
    sold_items.update({name:{'quantity':quantity,'unit':unit,'unit price':price}})

def sell_item(items):
    item = input("Item name:")
    if item in items:
        quantity = int(input("Quantity to sell:"))
        price = items[item]['unit price'] * quantity
        items[item]['quantity'] -= quantity
        print(f'The sale is made!\nBilans: +{price}')

        price = items[item]['unit price']
        unit = items[item]['unit']
        return item, quantity, unit, price
    else:
        print('no goods or incorrect name')

def inv_value():
    inventory_value = 0
    for i in items:
        qua,pri = items[i]['quantity'],items[i]['unit price']
        inventory_value += qua*pri
    return inventory_value

def add_space(a):
    output = ''
    if " " in a:
        for i in a:

            if i == ' ':
                output += '_'
            else:
                output += i
    else:
        for i in a:

            if i == '_':
                output += ' '
            else:
                output += i

    return output

def convert_to_save(items,file):
    with open(file,'w') as save:

        for i in items:

            a,b,c,d = add_space(i),str(items[i]['quantity']),items[i]['unit'],str(items[i]['unit price'])

            wri = f'{a} {b} {c} {d}\n'
            save.write(wri)
    print('Save completed!')

def convert_to_program(items,file):
    with open(file, 'r') as load:
        for line in load:
            a,b,c,d = line.split()
            a = add_space(a)
            items.update({a:{'quantity':int(b),'unit':c,'unit price':int(d)}})


if __name__ == '__main__':

    items = dict()
    sold_items = dict()
    inventory_value = 0

    convert_to_program(items,'save_inventory.txt')

    while True:

        inventory_value = inv_value()

        option=input\
            ("""Menu:\nshow\nexit\nadd\nsell\nsave\nWhat are you want to do?:""")

        if option == 'exit':
            break

        if option == 'show':
            get_items()

        if option == 'add':
            add_item(items)

        if option == 'sell':
            name,quantity,unit,price = sell_item(items)
            get_item_to_sold_items(sold_items,name,quantity,unit,price)

        if option == 'save':
            convert_to_save(items,'save_inventory.txt')

    input("exiting... see you! (press Enter)")
