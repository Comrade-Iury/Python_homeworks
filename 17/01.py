def parrot(word):
    if word in words:
        print(word)
    words.add(word)


words = set()


parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")
