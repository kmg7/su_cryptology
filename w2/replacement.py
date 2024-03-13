import random
import string

def main():
    TUR_U= 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    TUR_L= 'abcçdefgğhıijklmnoöprsştuüvyz'
    KEY_LIST = list(TUR_L)
    random.shuffle(KEY_LIST)
    KEY = ''.join(KEY_LIST)
    text = input("Text: ")
    if text == "":
        text = "Kemal Gökçay"

    print("To use random generated key leave it empty")
    keyinput = input("Input Key: ")
    if keyinput != "":
        if len(keyinput) != len(TUR_L):
            print("Invalid key. Key length does not match with alphabet length.")
            exit(1)

    print(f"Input: {text}")
    print(f"Key:   {KEY}") 

    
    crypted = replacement(TUR_U, TUR_L, text, KEY)
    print(f"Crypted:   {crypted}")

    uncrypted = de_replacement(TUR_L,crypted, KEY)
    print(f"Uncrypted: {uncrypted}")


def replacement(alphabet_U:str, alphabet_L:str, text:str, key:str):
    crypted = ""
    lenL = len(alphabet_L)

    if len(key) != lenL:
        return "Key length does not match with alphabet length"

    for letter in text:
        newLetter = "#"
        if letter.isalpha():
            if letter.isupper():
                i = alphabet_U.index(letter)
                newLetter = key[i]
            else:
                i = alphabet_L.index(letter)
                newLetter = key[i]
        else:
            newLetter = ""
        crypted += newLetter
    return crypted

def de_replacement(alphabet_L:str, text:str, key:str):
    encrypted = ""
    lenL = len(alphabet_L)

    if len(key) != lenL:
        return "Key length does not match with alphabet length"

    for letter in text:
        newLetter = "#"
        if letter.isalpha():
            i = key.index(letter)
            newLetter = alphabet_L[i]
        else:
            newLetter = ""
        encrypted += newLetter
    return encrypted


if __name__ == "__main__":
    main()