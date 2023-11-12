def print_document(pages):
    bills = True
    for page in pages:
        if "Секретно" in page:
            bills = False
            print("Дальнейщие материалы засекречены")
            break
        print(page)
    if bills:
        print("Напечатано без купюр")


print_document(["Обычная страница", "И ещё страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print_document(["Пустой трёп", "который", "никому не интересен"])