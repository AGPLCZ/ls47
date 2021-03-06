
import random

letters = "#_23456789abcdefghijklmnopqrstuvwxyz"
tiles = list(zip(letters, map(lambda x: (x // 6, x % 6), range(6 * 6))))
padding_size = 0
#přidá na konec zprávy x počet znaků

def check_key(key):
    if len(key) != len(letters):
        raise ValueError('Wrong key size')
    cnts = {}
    for c in letters:
        cnts[c] = 0
    for c in key:
        if not c in cnts:
            raise ValueError('Letter ' + c + ' not in LS46!')
        cnts[c] += 1
        if cnts[c] > 1:
            raise ValueError('Letter ' + c + ' duplicated in key!')


def find_ix(letter):
    m = [l for l in tiles if l[0] == letter]
    if len(m) != 1:
        raise ValueError('Letter ' + letter + ' not in LS46!')
    for (l, pos) in m:
        return pos


def find_pos(key, letter):
    p = key.find(letter)
    if p >= 0 and p < 6 * 6:
        return (p // 6, p % 6)
    raise ValueError('Letter ' + letter + ' not in key?!')


def add_pos(a, b):
    return ((a[0] + b[0]) % 6, (a[1] + b[1]) % 6)


def sub_pos(a, b):
    return ((a[0] - b[0]) % 6, (a[1] - b[1]) % 6)


def find_at_pos(key, coord):
    return key[coord[1] + coord[0] * 6]


def rotate_right(key, row, n):
    mid = key[6 * row:6 * (row + 1)]
    n = (6 - n % 6) % 6
    return key[:6 * row] + mid[n:] + mid[:n] + key[6 * (row + 1):]


def rotate_down(key, col, n):
    lines  = [key[i * 6:(i + 1) * 6] for i in range(6)]
    lefts  = [l[:col] for l in lines]
    mids   = [l[col] for l in lines]
    rights = [l[col + 1:] for l in lines]
    n = (6 - n % 6) % 6
    mids = mids[n:] + mids[:n]
    return ''.join(lefts[i] + mids[i] + rights[i] for i in range(6))


def rotate_marker_right(m, row, n):
    if m[0] != row:
        return (m[0], m[1])
    else:
        return (m[0], (m[1] + n) % 6)


def rotate_marker_down(m, col, n):
    if m[1] != col:
        return (m[0], m[1])
    else:
        return ((m[0] + n) % 6, m[1])


def derive_key(password):
    i = 0
    k = letters
    for c in password:
        (row, col) = find_ix(c)
        k = rotate_down(rotate_right(k, i, col), i, row)
        i = (i + 1) % 6
    return k

 # k dešifrování -----------------------------------------------
def encrypt(key, plaintext):
    check_key(key)
    mp = (0, 0)
    ciphertext = ''
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


def encrypt_pad(key, plaintext, signature):

    # TODO it would also be great to randomize the message length.

    check_key(key)
    padding = ''.join(map(lambda x: letters[random.randint(0,
                      len(letters) - 1)], range(padding_size)))

    return encrypt(key, padding + plaintext + '' + signature)


def decrypt_pad(key, ciphertext):
    check_key(key)
    return decrypt(key, ciphertext)[padding_size:]


if __name__ == '__main__':

    # a bit of test!

    print('letters in this implementation (line by line):')
    print(letters)
    # print('tiles positions: ' + str(tiles))

    key = derive_key("tohle_je_tajne_heslo") #heslo
    #key = ("_abcdefghijklmnopqrstuvwxyz.0123456689,-+*/:?!'()") #manualni zadani hesla

    print('test key: ' + key)
    enc = encrypt_pad(key, 'tajna_zprava',
                      '') #signature podpis

    print('encrypted test: ' + enc)
    dec = decrypt_pad(key, enc)
    print('decrypted test: ' + dec)
