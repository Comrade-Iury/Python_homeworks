JOKES_LIST = list()


def print_only_new(message):
    global JOKES_LIST
    if message not in JOKES_LIST:
        print(message)
        JOKES_LIST.append(message)
    else:
        pass
