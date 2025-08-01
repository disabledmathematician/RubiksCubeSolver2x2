# -*- coding: utf-8 -*-
"""
Authored by Charles Thomas Wallace Truscott Watters, one day before Christmas 2022

4:47 A.M. 24/12/2022

Finally implemented a basic bitwise logic cipher with shifts, next permutation boxes like MD5,Serpent, DES, AES etc

runfile('C:/Users/Charles/Documents/alphabetic_cipher.py', wdir='C:/Users/Charles/Documents')
Simple encryption example authored by Charles Truscott Watters after 6.001x at the Massachusetts Institute of Technology

Enter plain-text to encrypt: Charles
The ciphertext is: [123145302311122, 30786325577976, 251, 74766790688971, 48378511622367, 17592186044657, 79164837200116]

Would you like to decrypt the ciphertext? Y / N
Y
[28, 7, 0, 17, 11, 4, 18]
[123145302311122, 30786325577976, 251, 74766790688971, 48378511622367, 17592186044657, 79164837200116] decrypted is Charles





"""

def trinary_repr(integer):
    tristr = ''
#    for x in range(integer, 0, -1):
    for n in range(16, -1, -1):
#        print("n: {}, integer: {}".format(n, integer))
        if (integer // ( 2 * (3 ** n))) == 1:
            tristr += '2'
            integer -= 2 * (3 ** n)
            continue
        if integer // 3 ** n == 1:
            tristr += '1'
            integer -= 3 ** n
            continue
        else:
            tristr += '0'
            continue
#    if integer / 2 == 1:
#        tristr += '2'
#        integer -= 2
#    elif integer / 1 == 1:
#        tristr += '1'
#        integer -= 1

        
    print(tristr)
    return tristr

def binary_repr(integer):
    return bin(integer)

def binary_print(integer):
    print("{:16b}".format(integer))
    pass

def decrypt(L):
    decrypt_ = []
    for d in L:
        decrypt_.append(int(d))
    alphabet_lower = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    alphabet_upper = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    space = tuple(" ")
    punctuation = ("~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "|", "\\", ":", ";", "\"", "\'",  ",", "<", ">", ".", "?", "/")
    L = list(alphabet_lower + alphabet_upper + space + punctuation)
    index = list(x for x in range(len(L)))
    charset_plain = list(zip(L, index))
    R = []
    key = "The Gold Bug"
    keytext = []
    for c in key:
        keytext.append(c)
    keynumber = []
    for c in key:
        for k in charset_plain:
            if k[0] == c:
                keynumber.append(k[1])
    for r in range(len(decrypt_)):
        temp = 0xff
        temp = decrypt_[r]
        temp_2 = 0xff
        temp_2 = keynumber[r % 12]
        temp ^= 0xFE
        temp ^= 0xCA
        temp ^= 0xEE
        temp ^= 0xFF
        temp ^= 0xDA
        temp ^= temp_2
        temp >>= 42
#        temp &= temp_2
        R.append(temp)
    print(R)
    plaintext = []
    for x in range(len(R)):
        for y in charset_plain:
            if R[x] == y[1]:
                plaintext.append(y[0])
    plaintext_str = ''
    for c in plaintext:
        plaintext_str += c
    return plaintext_str
def main():
    alphabet_lower = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    alphabet_upper = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    space = tuple(" ")
    punctuation = ("~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "|", "\\", ":", ";", "\"", "\'",  ",", "<", ">", ".", "?", "/")
    L = list(alphabet_lower + alphabet_upper + space + punctuation)
    index = list(x for x in range(len(L)))
    charset_plain = list(zip(L, index))
#    print(charset_plain)
#    for x in charset_plain:
#        binary_print(x[1])
#    plaintext = "Charles Thomas Wallace Truscott. Yay"
    print("Simple encryption example authored by Charles Truscott Watters after 6.001x at the Massachusetts Institute of Technology")
    plaintext = input("Enter plain-text to encrypt: ")
    numbertext = []
    for x in plaintext:
        for y in charset_plain:
            if y[0] == x:
                numbertext.append(y[1])
                break
#    for number in numbertext:
#        binary_print(number)
#    print(numbertext)
#    print("The trinary representation of the ciphertext is: ")
#    for number in numbertext:
#       trinary_repr(number)
    key = "The Gold Bug"
    keytext = []
    for c in key:
        keytext.append(c)
    keynumber = []
    for c in key:
        for k in charset_plain:
            if k[0] == c:
                keynumber.append(k[1])
    ciphertext = []
    for r in range(len(numbertext)):
        temp = 0xff
        temp = (numbertext[r])
        temp_2 = 0xff
        temp_2 = keynumber[r % 12]
#        temp &= temp_2
        temp <<= 42
        temp ^= temp_2
        temp ^= 0xDA
        temp ^= 0xFF
        temp ^= 0xEE
        temp ^= 0xCA
        temp ^= 0xFE
        ciphertext.append(temp)
    print("The ciphertext is: {}".format(ciphertext))
    choice = input("Would you like to decrypt the ciphertext? Y / N\n")
    if choice == "Y":
        print("{} decrypted is {}".format(ciphertext, decrypt(ciphertext)))
    elif choice == "N":
        print("Thank you, exiting")
    else:
        print("Answer not welcomed. Exiting")
#    decrypt(ciphertext)

if __name__ == "__main__": main()