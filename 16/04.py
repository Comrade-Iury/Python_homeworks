receipt_number = 1
receipt_items = list()


def add_item(item_name, item_cost):
    global receipt_items
    receipt_items.append((item_name, item_cost))


def print_receipt():
    global receipt_items, receipt_number
    if not receipt_items:
        return
    sum = 0
    print("Чек" + str(receipt_number) + ". Всего предметов: " + str(len(receipt_items)))
    for item in receipt_items:
        print(item[0], "-", item[1])
        sum += item[1]
    print("Итого:", sum, "\n----")
    receipt_items.clear()
    receipt_number += 1


add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()

print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)