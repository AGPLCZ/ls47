#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This software is hereby released into public domain. Use it wisely.
#
# Originally written by Mirek Kratochvil (2017)
# Python3 port by Bernhard Esslinger (Feb 2018)
# input, překlad,design by AGPL (2018)


import random
letters = "_abcdefghijklmnopqrstuvwxyz.0123456789,-+@/:?!'()"
tiles = list(zip(letters, map(lambda x: (x // 7, x % 7), range(7 * 7))))


text = ('')
dekodovani = ('')


print('\nKONSTANTNÍ PARAMETRY')
print("Základní rozložení klíče 7x7:" + letters +"")

print('\nZADEJ VSTUPNÍ DATA')

def nacti_cislo():
    spatne = True
    while spatne:
        odpoved = input("Kolik chcete přidat na začátek náhodných znaků:")
        try:
            cislo = int(odpoved)
            spatne = False
        except ValueError:
            pass  
    else:
        return odpoved


padding_size = int(nacti_cislo())


pasw = input("Zadej expanzní heslo, nebo soukromý klíč:\n")  # získá od uživatele heslo a uloží jej do proměnné
x = len(pasw) #kolik zadaných znaků


zadanyklic = pasw
jetoheslo = 0
countklic_a = 0
countklic_b = 0
countklic_c = 0
countklic_d = 0
countklic_e = 0
countklic_f = 0
countklic_g = 0
countklic_h = 0
countklic_i = 0
countklic_j = 0
countklic_k = 0
countklic_l = 0
countklic_m = 0
countklic_n = 0
countklic_o = 0
countklic_p = 0
countklic_q = 0
countklic_r = 0
countklic_s = 0
countklic_t = 0
countklic_u = 0
countklic_v = 0
countklic_w = 0
countklic_x = 0
countklic_y = 0
countklic_z = 0
countklic_tecka = 0
countklic_0 = 0
countklic_1 = 0
countklic_2 = 0
countklic_3 = 0
countklic_4 = 0
countklic_5 = 0
countklic_6 = 0
countklic_7 = 0
countklic_8 = 0
countklic_9 = 0
countklic_carka = 0
countklic_minus = 0
countklic_plus = 0
countklic_zavinac = 0
countklic_lomeno = 0
countklic_dvoutecka = 0
countklic_otaznik = 0
countklic_vykricnik = 0
countklic_uvozovka = 0
countklic_lzavorka = 0
countklic_pzavorka = 0





for char in zadanyklic:
    if char == 'a':
        countklic_a += 1    
    if char == 'b':
        countklic_b += 1
    if char == 'c':
        countklic_c += 1
    if char == 'd':
        countklic_d += 1
    if char == 'e':
        countklic_e += 1
    if char == 'f':
        countklic_f += 1
    if char == 'g':
        countklic_g += 1
    if char == 'h':
        countklic_h += 1
    if char == 'i':
        countklic_i += 1
    if char == 'j':
        countklic_j += 1
    if char == 'k':
        countklic_k += 1
    if char == 'l':
        countklic_l += 1
    if char == 'm':
        countklic_m += 1
    if char == 'n':
        countklic_n += 1
    if char == 'o':
        countklic_o += 1
    if char == 'p':
        countklic_p += 1
    if char == 'q':
        countklic_q += 1
    if char == 'r':
        countklic_r += 1
    if char == 's':
        countklic_s += 1
    if char == 't':
        countklic_t += 1
    if char == 'u':
        countklic_u += 1
    if char == 'v':
        countklic_v += 1
    if char == 'w':
        countklic_w += 1
    if char == 'x':
        countklic_x += 1
    if char == 'y':
        countklic_y += 1
    if char == 'z':
        countklic_z += 1
    if char == '.':
        countklic_tecka += 1
    if char == '0':
        countklic_0 += 1
    if char == '1':
        countklic_1 += 1
    if char == '2':
        countklic_2 += 1
    if char == '3':
        countklic_3 += 1
    if char == '4':
        countklic_4 += 1
    if char == '5':
        countklic_5 += 1
    if char == '6':
        countklic_6 += 1
    if char == '7':
        countklic_7 += 1
    if char == '8':
        countklic_8 += 1
    if char == '9':
        countklic_9 += 1
    if char == ',':
        countklic_carka += 1
    if char == '-':
        countklic_minus += 1
    if char == '+':
        countklic_plus += 1
    if char == '@':
        countklic_zavinac += 1
    if char == '/':
        countklic_lomeno += 1
    if char == ':':
        countklic_dvoutecka += 1
    if char == '?':
        countklic_otaznik += 1
    if char == '!':
        countklic_vykricnik += 1
    if char == "'":
        countklic_uvozovka += 1
    if char == '(':
        countklic_lzavorka += 1
    if char == ')':
        countklic_pzavorka += 1
  

if (countklic_a > 1 or countklic_b > 1 or countklic_c > 1 or countklic_d > 1 or countklic_e > 1 or countklic_f > 1 or countklic_g > 1 or countklic_h > 1 or countklic_i > 1 or countklic_j > 1 or countklic_k > 1 or countklic_l > 1 or countklic_m > 1 or countklic_n > 1 or countklic_o > 1 or countklic_p > 1 or countklic_q > 1 or countklic_r > 1 or countklic_s > 1 or countklic_t > 1 or countklic_u > 1 or countklic_v > 1 or countklic_w > 1 or countklic_x > 1 or countklic_y > 1 or countklic_z > 1 or countklic_tecka > 1 or countklic_0 > 1 or countklic_1 > 1 or countklic_2 > 1 or countklic_3 > 1 or countklic_4 > 1 or countklic_5 > 1 or countklic_6 > 1 or countklic_7 > 1 or countklic_8 > 1 or countklic_9 > 1 or countklic_carka > 1 or countklic_minus > 1 or countklic_plus > 1 or countklic_zavinac > 1 or countklic_lomeno > 1 or countklic_dvoutecka > 1 or countklic_otaznik > 1 or countklic_vykricnik > 1 or countklic_uvozovka > 1 or countklic_lzavorka > 1 or countklic_pzavorka > 1):
    jetoheslo = 2

if (x < 49 or x > 49 or jetoheslo > 1):
    plan = "heslo"
    print('Vstup použit jako expanzní heslo! ') 
else:
    plan = "klic"
    print("Byl zadán soukromý klíč s permutací!")

if (x == 49 and jetoheslo > 1):
    print("Nezada-li jste špatně soukromý klíč?")

    
pokracovat = True
while pokracovat:
    zadani = input("Chceš šifrovat (s) nebo dešifrovat (d)?")
    if (zadani == "s" or zadani == "d"):
        if (zadani == "s"):
          text = input("Zadej text pro zašifrování:")  
        else:
          dekodovani = input("Zadejtext pro dešifrování:")

        pokracovat = False
    else:
        pass # nic se nestane


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
    lines = [key[i * 7:(i + 1) * 7] for i in range(7)]
    lefts = [l[:col] for l in lines]
    mids = [l[col] for l in lines]
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
    # ----------------------------------------------------------------------------
    ciphertext = ('' + dekodovani)  # Zde zadej text k dešifrování
    # -----------------------------------------------------------------------------
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

    return encrypt(key, padding + plaintext)


def decrypt_pad(key, ciphertext):
    check_key(key)
    return decrypt(key, ciphertext)[padding_size:]


if __name__ == '__main__':
    # a bit of test!
    #plan = (input("Zadali jste heslo nebo klic?"))
    if (plan == "heslo"):
        key = derive_key('' + pasw) # heslo
    elif (plan == "klic"):  
        key = ('' + pasw) # manualni zadání
    else:
      print("chyba")

    print('\n')
    print('KONFIGURACE')

    print('Základní rozložení:   ' + letters)
    print('Klíč šifry:           ' + key)
    if (plan == "heslo"):
        print('Heslo šifry:          ' + pasw)
    enc = encrypt_pad(key, '' + text)  # Zde zadej text k zašifrování

    print('\n')
    #print('POZICE KARTIČEK  + string')

    #print(str(tiles))

    print('VÝSTUP')

    print('Zašifrováný text:' + enc)
    dec = decrypt_pad(key, enc)
    print('Dešifrovaný text:' + dec)

