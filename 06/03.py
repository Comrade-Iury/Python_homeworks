english_students = set()
german_students = set()
english_count = int(input())
german_count = int(input())

for _ in range(english_count):
    english_students.add(input())
for _ in range(german_count):
    german_students.add(input())

one_lang = english_students ^ german_students
if one_lang:
    print(len(one_lang))
else:
    print("No")
