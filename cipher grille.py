import numpy as np

def masking(cipher_grille, ciphered_password):
    passw = []
    for i in range(len(cipher_grille)):
        for j in range(len(cipher_grille[i])):
            if cipher_grille[i][j] == 'X':
                passw.append(ciphered_password[i][j])
    return passw
    
def recall_password(cipher_grille, ciphered_password):
    
    sg1 = []
    for i in cipher_grille:
        sg1.append([j for j in i])

    sg1 = np.array(sg1)
    
    password = []
    for i in range(4):
        password.append(masking(sg1, ciphered_password))
        sg1 = np.rot90(sg1, k=3)
    res = []
    for i in password:
        for j in i:
            res.append(j)
    return ''.join(res)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
