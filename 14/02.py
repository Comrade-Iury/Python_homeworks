def space_game(text):
    sum = 0
    for char in text:
        if char == " ":
            sum += 1 
    if sum % 2 == 0:
        print("You win!")
    else:
        print("You lose :/")

    
    
space_game(input())    
