items ={'coal':{'quanity':160,'unit':'t','unit price':1500},
        'coal eco peas':{'quanity':210,'unit':'t','unit price':1000},
        'culm':{'quanity':260,'unit':'t','unit price':650}}

def get_items():
    name,quanity,unit,unit_price = '{:15}'.format('Name'),'{:^15}'.format('Quanity'),'{:^15}'.format('Unit'),'{:^15}'.format('Unit price')
    print(f"{name}{quanity}{unit}{unit_price}")
    print('{:14}'.format('^'*4),'{:^15}'.format('^'*7),'{:^12}'.format('^'*4),'{:^16}'.format('^'*10))

    for i in items:
        position = items[i]
        nam,qua, uni, uni_pri = '{:15}'.format(i),'{:^13}'.format(position['quanity']), '{:^14}'.format(position['unit']), '{:^15}'.format(
            position['unit price'])
        print(nam, qua, uni, uni_pri)


if __name__ == '__main__':
    while True:
        option=input\
            ("""Menu:\nshow\nexit\nWhat are you want to do?:""")

        if option == 'exit':
            break

        if option == 'show':
            get_items()

    input("exiting... see you! (press Enter)")