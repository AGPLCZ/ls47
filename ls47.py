#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This software is hereby released into public domain. Use it wisely.
#
# Originally written by Mirek Kratochvil (2017)
# Python3 port by Bernhard Esslinger (Feb 2018)
# inputy, překlad, by AGPL (2018)

import random
letters = "_abcdefghijklmnopqrstuvwxyz.0123456789,-+*/:?!@()"
tiles = list(zip(letters, map(lambda x: (x // 7, x % 7), range(7 * 7))))
padding_size = 0 #počet přidaných znaků které se generují náhodně 


print ('Zdar, mám pro tebe zprávu, ne-máme moc času, tak se soustřeď.Skaut je největší světové hnutí, žes o nás nikdy neslyšel? SKAUT – To jsou kamarádi, přátelé, společenství lidí, kteří sdílejí podobné hodnoty a společně se snaží tvořit lepší svět.\n \n Situace je kritická, proto jsme se rozhodli oslovit právě tebe. Svět potřebuje nás, a my potřebujeme tvoji pomoc. Cvičíme stovky skautů, ale to nestačí. Potřebujeme víc. Je jedno kolik ti je, odkud jsi, nebo jaké máš známky. Skautem se nenarodíš, skautem se stáváš. Staň se skautem a ukaž co v tobě je. Staň se skautem a zachraň svět. \n \n Výcvik skautů probíhá každý týden ve ve Čtvrtek od 17:00 do 18:00. Sraz je na Orlovně v prvním patře. Získáš znalosti i dovednosti a dozvíš se jak můžeš pomáhat. \n \n  Skaut není hra, světu hrozí reálná hrozba! Přidej se a pomáhej. V každé misi mohou působit jen ti způsobilí, proto nejdřív musíš projít výcvikem které si mise žádá. \n \n MISE 1 \n Vidíš li někoho, kdo si chce koupit petláhev, zeptej se ho proč si jí kupuje, a případně se zeptej jestli by se bez ní neobešel. Vysvětli mu důvod. \n \n ')

print('VSTUP')
print('-------------------------------------------------------------------------')

pasw = input("Zadej heslo které nakonfiguruje klíč šifry. \n ") #získá od uživatele heslo a uloží jej do proměnné
text = input("Zadejtext pro zašifrování.  \n Pokud chceš dešifrovat zprávu, nech toto pole prázdné. \n") #získá od uživatele text k šifrování a uloží jej do proměnné  
dekodovani = input("Zadejtext pro dešifrování: \n Pokud jsi již zadal text k zašifrování, nech toto pole prázdné. \n ") #získá od uživatele text k šifrování a uloží jej do proměnné  
print('-------------------------------------------------------------------------')
print('\n \n')



def check_key(key):
    if len(key) != len(letters):
        raise ValueError('Wrong key size')
    cnts = {}
    for c in letters:
        cnts[c] = 0
    for c in key:
        if not c in cnts:
            raise ValueError('Letter ' + c + ' not in LS47!')
        cnts[c] += 1
        if cnts[c] > 1:
            raise ValueError('Letter ' + c + ' duplicated in key!')


def find_ix(letter):
    m = [l for l in tiles if l[0] == letter]
    if len(m) != 1:
        raise ValueError('Letter ' + letter + ' not in LS47!')
    for (l, pos) in m:
        return pos


def find_pos(key, letter):
    p = key.find(letter)
    if p >= 0 and p < 7 * 7:
        return (p // 7, p % 7)
    raise ValueError('Letter ' + letter + ' not in key?!')


def add_pos(a, b):
    return ((a[0] + b[0]) % 7, (a[1] + b[1]) % 7)


def sub_pos(a, b):
    return ((a[0] - b[0]) % 7, (a[1] - b[1]) % 7)


def find_at_pos(key, coord):
    return key[coord[1] + coord[0] * 7]


def rotate_right(key, row, n):
    mid = key[7 * row:7 * (row + 1)]
    n = (7 - n % 7) % 7
    return key[:7 * row] + mid[n:] + mid[:n] + key[7 * (row + 1):]


def rotate_down(key, col, n):
    lines  = [key[i * 7:(i + 1) * 7] for i in range(7)]
    lefts  = [l[:col] for l in lines]
    mids   = [l[col] for l in lines]
    rights = [l[col + 1:] for l in lines]
    n = (7 - n % 7) % 7
    mids = mids[n:] + mids[:n]
    return ''.join(lefts[i] + mids[i] + rights[i] for i in range(7))


def rotate_marker_right(m, row, n):
    if m[0] != row:
        return (m[0], m[1])
    else:
        return (m[0], (m[1] + n) % 7)


def rotate_marker_down(m, col, n):
    if m[1] != col:
        return (m[0], m[1])
    else:
        return ((m[0] + n) % 7, m[1])


    
def derive_key(password):
    i = 0
    k = letters
    for c in password:
        (row, col) = find_ix(c)
        k = rotate_down(rotate_right(k, i, col), i, row)
        i = (i + 1) % 7
    return k

def encrypt(key, plaintext):
    check_key(key)
    mp = (0, 0)
    #----------------------------------------------------------------------------
    ciphertext = ('' + dekodovani) #Zde zadej text k dešifrování
    #-----------------------------------------------------------------------------
    for p in plaintext:
        pp = find_pos(key, p)
        mix = find_ix(find_at_pos(key, mp))
        cp = add_pos(pp, mix)
        c = find_at_pos(key, cp)
        ciphertext += c

        key = rotate_right(key, pp[0], 1)
        cp = find_pos(key, c)
        key = rotate_down(key, cp[1], 1)
        mp = add_pos(mp, find_ix(c))
    return ciphertext


def decrypt(key, ciphertext):
    check_key(key)
    mp = (0, 0)
    plaintext = ''
    for c in ciphertext:
        cp = find_pos(key, c)
        mix = find_ix(find_at_pos(key, mp))
        pp = sub_pos(cp, mix)
        p = find_at_pos(key, pp)
        plaintext += p

        key = rotate_right(key, pp[0], 1)
        cp = find_pos(key, c)
        key = rotate_down(key, cp[1], 1)
        mp = add_pos(mp, find_ix(c))
    return plaintext


def encrypt_pad(key, plaintext):

    # TODO it would also be great to randomize the message length.

    check_key(key)
    padding = ''.join(map(lambda x: letters[random.randint(0,
                      len(letters) - 1)], range(padding_size)))

    return encrypt(key, padding +  plaintext)


def decrypt_pad(key, ciphertext):
    check_key(key)
    return decrypt(key, ciphertext)[padding_size:]




if __name__ == '__main__':

    # a bit of test!
    print('KONFIGURACE')
    print('-------------------------------------------------------------------------')
    print('Písmena v této implementaci:')
    print('Základní rozložení:   ' + letters)
    #pasw = "tohle_je_tajne_heslo"   #Zadej heslo, to ovlivní rozležení tabulky
    
    # zakomentuj key = derive_key ('' + pasw) pokud chceš aktivovat ruční zadávání abecedy
    key = derive_key ('' + pasw) 
    
    #key = ('abcdefghijklmnopqrstuvwxyz.0123456789,-+*/:?!@()_') #odkomentuj key pokud chceš ručně zadávat abecedu

    #key = derive_key ('' + pasw)
    print('Klíč šifry:           ' + key)
    print('Heslo šifry:          ' + pasw)
    enc = encrypt_pad(key, '' + text) #Zde zadej text k zašifrování
    print('-------------------------------------------------------------------------')
    print('\n \n ')
    print('POZICE KARTIČEK  + string')
    print('-------------------------------------------------------------------------')
    print(str(tiles))
    print('\n \n ')
    print('VÝSTUP')
    print('-------------------------------------------------------------------------')
    print('Šifrováný text:     ' + enc)
    dec = decrypt_pad(key, enc)
    print('Dešifrovaný text:   ' + dec)
    print('-------------------------------------------------------------------------')

