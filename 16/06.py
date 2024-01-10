translated_text = None


def translate(text):
    global translated_text
    text_list = text.split()
    i = 0
    for word in text_list:
        word = map(is_consonant, word)
        new_list = list()
        for char in word:
            new_list.append(char)
        word = ""
        for char in new_list:
            if char != "":
                word = word + char
        text_list[i] = word
        i += 1
    i = 0
    for _ in range(len(text_list)):
        if text_list[i] == "":
            text_list.remove(text_list[i])
        else:
            i += 1

    translated_text = " ".join(text_list)


def is_consonant(char):
    if char.lower() in "бвгджзйклмнпрстфхцчшщъь":
        return char
    return ""




