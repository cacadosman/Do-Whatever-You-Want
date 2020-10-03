import random
from .character import Knight, Archer
from .interface import bar, clear, wait

def random_lawan():
    hp = random.randint(80, 100)
    atk = random.randint(10, 30)
    lawan = random.choice([
        Knight(hp=hp, atk=atk, name='Knight'), 
        Archer(hp=hp, atk=atk, name='Archer')
    ])

    bar()
    print('> Lawan telah muncul!\n')
    print('Jenis   : %s' % lawan.name)
    print('HP      : %d' % lawan.hp)
    print('Attack  : %d' % lawan.atk)
    bar()
    wait()

    return lawan

def start(player):
    clear()
    lawan = random_lawan()
    hp_player = player.hp
    menang = True
    turn = 1

    while player.hp > 0:
        bar()
        print('[ Turn %d ]\n' % turn)

        # player menyerang lawan
        hp_awal_lawan = lawan.hp
        player.attack(lawan)
        
        print('> %s menyerang lawan! (Damage: %d)' % (player.name, player.atk))
        print('HP lawan: %d -> %d' % (hp_awal_lawan, lawan.hp))

        if lawan.hp == 0:
            menang = True
            print('\nKamu menang!'); bar();
            break

        print()

        # lawan menyerang player
        hp_awal_player = player.hp
        lawan.attack(player)

        print('< Lawan menyerang %s! (Damage: %d)' % (player.name, lawan.atk))
        print('HP %s: %d -> %d' % 
            (player.name, hp_awal_player, player.hp))
        
        if player.hp == 0:
            menang = False
            print('\nKamu kalah!'); bar()
            break

        turn += 1
        bar()
        wait()

    player.hp = hp_player
    wait()
    clear()
    if menang:
        player.gain_exp(10)
