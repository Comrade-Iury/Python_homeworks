from random import choice
from sys import stdin

friends_list = list()
secret_friends_list = list()
for new_friend in stdin:
    friends_list.append(new_friend.strip())

unpicked_friends_list = friends_list.copy()
for friend in range(len(friends_list)):
    random_friend = choice(unpicked_friends_list)
    while friend == random_friend:
        random_friend = choice(unpicked_friends_list)
    else:
        secret_friends_list.append(random_friend)
        unpicked_friends_list.remove(random_friend)
for j in range(len(friends_list)):
    print(f"{friends_list[j]} - {secret_friends_list[j]}")