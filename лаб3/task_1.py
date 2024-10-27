# TODO Напишите функцию для поиска индекса товара
def poisk_indexa(list, item):
    trig = False
    find_index = None
    counter = 0
    for t in list:
        if t == item:
            trig = True
            find_index = counter
            break
        else:
            counter += 1
    return find_index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk_indexa(items_list, find_item)   # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
