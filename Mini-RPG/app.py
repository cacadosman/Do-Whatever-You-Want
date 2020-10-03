from module.interface import bar, clear

HOME = '''
------------------------------------------
|       Selamat datang di Mini-RPG!      |
------------------------------------------

(1) Game baru
(2) Lanjutkan game [BELUM TERSEDIA]
(3) Keluar

> Pilihan (1/2/3): '''

def main():
    clear()
    opt = '0'
    while opt not in ['1', '2', '3']:
        opt = input(HOME)
        if opt == '1':
            from module import game
            game.start()
        elif opt == '2':
            clear()
            bar()
            print('PILIHAN %s BELUM TERSEDIA!\n' % opt)
            print('Silakan pilih menu lain.')
            bar()
        elif opt == '3':
            clear()
            bar(); print('Terima kasih sudah bermain!'); bar()
            break
        else:
            clear()
            bar()
            print('PILIHAN %s TIDAK ADA!\n' % opt)
            print('Silakan pilih menu lain.')
            bar()
        opt = '0'

if __name__ == '__main__':
    main()
