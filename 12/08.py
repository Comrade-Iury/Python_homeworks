symbols_set = set()
symbols_list = list()
flags_list = list()
for symbol in input().lower():
    if symbol != " ":
        symbols_set.add(symbol)
        symbols_list.append(symbol)
uniq_symbols_list = list()
for symbol in symbols_set:
    uniq_symbols_list.append(symbol)
uniq_symbols_list.sort()
for symbol in uniq_symbols_list:
    flag = 0
    for char in symbols_list:
        if char == symbol:
            flag += 1
    flags_list.append(flag)

print(*uniq_symbols_list, "----", *flags_list)
print(uniq_symbols_list[flags_list.index(max(flags_list))])