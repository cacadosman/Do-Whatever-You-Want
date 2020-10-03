from . import battle
from .character import Knight, Archer
from .interface import bar, clear

PLAYER = None

MENU = '''
---------------------------------------
|             Pilih Menu              |
---------------------------------------

(1) Bertarung
(2) Inventory [BELUM TERSEDIA]
(3) Mall [BELUM TERSEDIA]
(4) Simpan game [BELUM TERSEDIA]
(5) Kembali

> Pilihan (1/2/.../5): '''

PILIH_KARAKTER = '''
---------------------------------------
|           Pilih Karakter            |
---------------------------------------

(1) Knight
(2) Archer

> Pilihan (1/2): '''

STATS = '''
---------------------------------------
|              Statistik              |
---------------------------------------

Nama   : %s
Level  : %d
Exp    : %d
HP     : %d
Attack : %d'''

def pilih_karakter():
    clear()
    NAMA_KARAKTER = '> Masukkan nama karakter anda: '

    player = None
    char = input(PILIH_KARAKTER)
    name = input(NAMA_KARAKTER)
    
    if char == '1':
        player = Knight(name=name)
    elif char == '2':
        player = Archer(name=name)

    return player

def stats():
    print(STATS % (
        PLAYER.name, 
        PLAYER.level, 
        PLAYER.exp,
        PLAYER.hp,
        PLAYER.atk)
    )

def start():
    global PLAYER
    PLAYER = pilih_karakter()
    
    clear()
    opt = '0'
    while opt not in ['1', '2', '3']:
        stats()
        opt = input(MENU)
        if opt == '1':
            battle.start(PLAYER)
        elif opt in ['2', '3', '4']:
            clear()
            bar()
            print('PILIHAN %s BELUM TERSEDIA!\n' % opt)
            print('Silakan pilih menu lain.')
            bar()
        elif opt == '5':
            clear()
            break
        else:
            clear()
            bar()
            print('PILIHAN %s TIDAK ADA!\n' % opt)
            print('Silakan pilih menu lain.')
            bar()
        opt = '0'
