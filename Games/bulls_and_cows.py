import random
import sys
import os


def Title():
    title_width = 4
    title_char = '-'
    title_message = 'Bulls and Cows'
    print(title_width*title_char, title_message,
          title_width*title_char, sep='')
    title_menu = [' <1> Play', ' <2> Exit']
    for option in title_menu:
        print(option)
    print(title_width*title_char, title_char*len(title_message),
          title_width*title_char, sep='')
    input_prompt = '-->'
    while True:
        try:
            print(input_prompt, end=' ')
            choice = int(input())
            if choice == 2:
                sys.exit()
            for i in range(1, len(title_menu)+1):
                if choice == i:
                    UserGuess(SecretNumbers())
                    return
            print('Invalid Choice! Try again.')
            continue
        except ValueError:
            print('Invalid Type! Try again.')
            continue
        break


def SecretNumbers():
    secret_number = [0, 0, 0, 0]
    for i in range(4):
        secret_number[i] = random.randint(0, 9)
    for j in range(4):
        for i in range(4):
            if i == j:
                continue
            while secret_number[i] == secret_number[j]:
                secret_number[i] = random.randint(0, 9)
    return secret_number


def UserGuess(secret_number):
    os.system('cls')
    print('Farmer:\t \"O great wizard! Please help us overcame this great calamity! What should we do to calm the gods for their anger is wretched indeed!\"')
    print('You:\t \"And its only the beginning of only a greater crisis! But fear not! There still is a chance! Scarfice some cattle, for we could only hope its enough.\"')
    print('Farmer:\t \"Bless you wizard! How many should we --\"')
    while True:
        print('You:\t ', end='')
        user_guess = input()
        if len(user_guess) >= 5 or len(user_guess) < 4:
            print('Magic:\t ~~ Gibberish Gibberish ~~')
            print('Farmer:\t \"What?\"')
            print('(Your arcane readings hints at a 4-digit number)')
            continue
        try:
            for i in user_guess:
                if i != int(i):
                    None
        except:
            print('Magic:\t ~~ Gibberish Gibberish ~~')
            print('Farmer:\t \"What?\"')
            print('(Your arcane readings hints at a 4-digit number)')
            continue
        bull = 0
        cow = 0
        for i in range(len(user_guess)):
            for j in range(len(secret_number)):
                if user_guess[i] == str(secret_number[j]) and i != j:
                    cow = cow + 1
                elif user_guess[i] == str(secret_number[j]) and i == j:
                    bull = bull + 1
        if bull == 0 and cow == 0:
            print('Magic:\t ~~ Nothing ~~')
            print('Farmer:\t \"That..That can\'t be right!\"')
        elif bull == 0 and cow != 0:
            print('Magic:\t ~~', cow, 'Cows ~~')
            print('Farmer:\t \"There must be more we can do!\"')
        elif bull != 0 and cow != 0:
            print('Magic:\t ~~', cow, 'Cows and', bull, 'Bulls ~~')
            print('Farmer:\t \"I think we could afford a bit more!\"')
        elif bull == 4:
            print('Magic:\t ~~', bull, 'Bulls ~~')
            print(
                'Farmer:\t \"That should do! Thank you wizard! May the gods smile apon you!\"')
            break
        elif bull != 0 and cow == 0:
            print('Magic:\t ~~', bull, 'Bulls ~~')
            print('Farmer:\t \"There must be more we can do!\"')


Title()
