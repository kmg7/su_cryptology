import sys

def main():
    TUR_U= 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    TUR_L= 'abcçdefgğhıijklmnoöprsştuüvyz'
    text= "Kemal Gökçay"
    key = 5

    if len(sys.argv )> 2:
        key = int(sys.argv[1])        
        text = sys.argv[2]

    print(f"Key:       {key}") 
    print(f"Input:     {text}")

    crypted = shift(TUR_U, TUR_L, text, key)
    print(f"Crypted:   {crypted}")

    uncrypted = de_shift(TUR_U, TUR_L, crypted, key)
    print(f"Uncrypted: {uncrypted}")


def shift(alphabet_U: str,alphabet_L: str, text:str, key:int):
    crypted = ""
    lenU = len(alphabet_U)
    lenL = len(alphabet_L)
    for letter in text:
        newLetter = "#"
        if letter.isalpha():
            if letter.isupper():
                i = (alphabet_U.index(letter) + key) % lenU
                newLetter = alphabet_U[i]
            else:
                i = (alphabet_L.index(letter) + key) % lenL
                newLetter = alphabet_L[i]
        else:
            newLetter = letter
        crypted += newLetter
    return crypted

def de_shift(alphabet_U: str,alphabet_L: str, text:str, key:int):
    return shift(alphabet_U, alphabet_L, text, -key)

if __name__ == "__main__":
    main()