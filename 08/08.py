heads_tails = input()
tails = [0] * len(heads_tails)
i = 0
for side in heads_tails:
    if side == "р":
        i += 1
    if side == "о":
        tails[i] = tails[i] + 1
print(max(tails))
