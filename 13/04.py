coord_dict = dict()
for _ in range(int(input())):
    coord = input().split()
    for _ in range(1):
        coord[0], coord[1] = str(int(coord[0]) // 10), str(int(coord[1]) // 10)
    dict_ix = "".join(coord)
    if dict_ix not in coord_dict:
        coord_dict[dict_ix] = 1
    else:
        coord_dict[dict_ix] += 1

print(max(coord_dict.values()))