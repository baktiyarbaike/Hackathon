import json

FILEJSON = 'data.json'
def get_data():
    with open(FILEJSON) as file:
        return json.load(file)

def get_one_product():
    data = get_data()
    id = int(input('Введите id ноутбука: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if product:
        return product[0]
    else: 
        return 'Такого ноутбука нет!'


def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1

    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    try:
        product = {
            'id': get_id(),
            'brand': input('Введите марку: '),
            'model':input('Введите модель:'),
            'year of issue':int(input('Год выпуска:')),
            'description': input('Описание:'),
            'price': round(float(input('Введите цену: ')),2)
        }
    except ValueError:
        print('Вы ввели не число!')
        create_product()
    else:

        data.append(product)

        with open(FILEJSON, 'w') as file:
            json.dump(data, file, indent='')
        return 'Создан'

def update_product():
    data = get_data()
    flag = False
    id = int(input('Введите id ноутбука: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'Такого ноутбука нет!'
    index_ = data.index(product[0])

    choice = input('Что вы хотите изменить:\n1 - Марка\n2 - Модель\n3 - Год выпуска\n4- Описание\n5 - Цена\n')
    if choice == '1':
        data[index_]['brand'] = input('Введите новое название: ')
        flag = True
    elif choice == '2':
        data[index_]['model'] = input('Введите новую модель: ')
        flag = True
    elif choice == '3':
        data[index_]['year of issue'] = int(input('Введите новый год выпуска: '))
        flag = True
    elif choice == '4':
        data[index_]['description'] = input('Введите новое описание: ')
        flag = True
    elif choice == '5':
        data[index_]['price'] = round(float(input('Введите новую цену: ')),2)
        flag = True
    else:
        print('Такого поля нет!')

    with open(FILEJSON, 'w') as file:
        json.dump(data, file)
    if flag:
        return 'Обновлено'
    else:
        return 'Не обновляется'

def delete_product():
    data = get_data()
    id = int(input(' Введите id ноутбука: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'Такого ноутбука нет!'

    index_ = data.index(product[0])
    data.pop(index_)
    json.dump(data, open(FILEJSON, 'w'))
    return 'Удалено'