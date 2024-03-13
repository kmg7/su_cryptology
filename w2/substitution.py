import random

def main():
    TUR_U= 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    TUR_L= 'abcçdefgğhıijklmnoöprsştuüvyz'
    text= "Kemal Gökçay"

    text = input("Text: ")
    print(f"To use random generated key leave it empty")
    key = input("Custom Key: ")
    if key == "":
        key = shuffle(TUR_L)

    print(f"Key:       {key}") 
    print(f"Input:     {text}")

    crypted = substitute(TUR_U, TUR_L, text, key)
    print(f"Crypted:   {crypted}")

    uncrypted = de_substitue(TUR_L, crypted, key)
    print(f"Uncrypted: {uncrypted}")


def substitute(alphabet_U: str,alphabet_L: str, text:str, key:str):
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

def de_substitue(alphabet_L: str, text:str, key:str):
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

def shuffle(text: str):
    text = list(text)
    random.shuffle(text)
    return "".join(text)

if __name__ == "__main__":
    main()
