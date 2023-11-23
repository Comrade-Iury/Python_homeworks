scoring = {
    "Яблочко": 50,
    "Зелёное кольцо": 25,
    "Внутреннее кольцо": {
        1: 2,
        2: 9,
        3: 56,
        4: 40,
        5: 8,
        6: 17,
        7: 43,
        8: 12,
        9: 11,
        10: 15,
        11: 10,
        12: 13,
        13: 5,
        14: 21,
        15: 2,
        16: 19,
        17: 5,
        18: 14,
        19: 7,
        20: 3
    },
    "Внешнее кольцо": {
        1: 8,
        2: 6,
        3: 42,
        4: 39,
        5: 7,
        6: 16,
        7: 42,
        8: 11,
        9: 10,
        10: 14,
        11: 9,
        12: 12,
        13: 5,
        14: 20,
        15: 1,
        16: 18,
        17: 4,
        18: 13,
        19: 6,
        20: 50
    }
}


def score(sector: str, number: int = 0):
    if sector not in scoring or number < 0 or number > 20:
        return "input error"
    if not number:
        return scoring[sector]
    return scoring[sector][number]


print(score(sector="Яблочко"))
print(score(sector="Зелёное кольцо"))
print(score(sector="Внутреннее кольцо", number=3))
print(score(sector="Внешнее кольцо", number=20))
print(score(sector="Внешнее кольцо", number=21))