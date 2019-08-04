#!/usr/bin/python3
# -*- coding: utf8 -*-

#--------------------------------------------------------------
#	This script can be used to encrypt, decrypt or bruteforce
#	strings using the caesar cryptography
#--------------------------------------------------------------

def decaesarcrypt(ciphered, key):
    alfabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    alfabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    deciphered = ''
    for letter in ciphered:
        if letter in alfabet_lower:
            index = alfabet_lower.index(letter)
            deciphered += alfabet_lower[index - key]
        elif letter in alfabet_upper:
            index = alfabet_upper.index(letter)
            deciphered += alfabet_upper[index - key]
        else:
            deciphered += letter

    return deciphered

def caesarcrypt(cleartxt, key):
    alfabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    alfabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    ciphered = ''
    for letter in cleartxt:
        if letter in alfabet_lower:
            index = alfabet_lower.index(letter)
            if index + key > 25:
                ciphered += alfabet_lower[index - 26 + key]
            else:
                ciphered += alfabet_lower[index + key]
        elif letter in alfabet_upper:
            index = alfabet_upper.index(letter)
            if index + key > 25:
                ciphered += alfabet_upper[index - 26 + key]
            else:
                ciphered += alfabet_upper[index + key]
        else:
            ciphered += letter

    return ciphered


def main():
    print("-----------------------------")
    print("Choose the type of operation:")
    print("-----------------------------")
    print("1 - Encrypt")
    print("2 - Decrypt with the key")
    print("3 - Decrypt without the key")
    print("[ANY] - QUIT")
    print("-----------------------------")

    try:
        choose = int(input("| ~~> "))
    except:
        print("Bye.")
        exit()
    print()
    if choose  < 1 or choose > 3:
        print("Bye.")
        exit()
    elif choose == 1:
        print("Type or paste the cleartext:")
        clear = input()
        print()
        print("Type the key:")
        key = int(input())
        encrypted = caesarcrypt(clear, key)
        print("---------------------------------")
        print(encrypted)
        print("---------------------------------")
    elif choose == 2:
        print("Type or paste the ciphered text:")
        ciphered = input()
        print()
        print("Type the key:")
        key = int(input())
        decrypted = decaesarcrypt(ciphered, key)
        print("---------------------------------")
        print(decrypted)
        print("---------------------------------")
    elif choose == 3:
        print("Type or paste the ciphered text:")
        ciphered = input()

        i = 1
        correct = 'n'
        while correct == 'n' and i < 27:
            print("------------------------------")
            print("         KEY {}".format(i))
            print("------------------------------")
            print(decaesarcrypt(ciphered, i))
            print("------------------------------\n")
            
            print("Do this make sense? [ENTER] -> NO | y -> YES")
            correct = input()
            if correct == '':
                correct = 'n'
            i += 1

main()
