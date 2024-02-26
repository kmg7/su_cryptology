def main():
    TUR_U= 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    TUR_L= 'abcçdefgğhıijklmnoöprsştuüvyz'
    print("Affine Cipher Simulation using Turkish Alphabet")

    keyA = int(input("Key A: "))
    keyB = int(input("Key B: "))
    text = input("Text: ")

    print("\n")
    check = check_affine(len(TUR_L), keyA)
    while check == -1:
        print(f"It is impossible to decypher with current key A:{keyA}")
        keyA = int(input("New Key A: "))
        check = check_affine(len(TUR_L), keyA)

    print("\n")
    print(f"Keys:      A:{keyA} B:{keyB}") 
    print(f"Input:     {text}")

    crypted = affine(TUR_U, TUR_L, text, keyA, keyB)
    print(f"Crypted:   {crypted}")

    uncrypted = de_affine(TUR_U, TUR_L, crypted, keyA, keyB)
    print(f"Uncrypted: {uncrypted}")


def affine(alphabet_U: str,alphabet_L: str, text:str, key_A:int, key_B:int):
    crypted = ""
    lenU = len(alphabet_U)
    lenL = len(alphabet_L)
    for letter in text:
        newLetter = "#"
        if letter.isalpha():
            if letter.isupper():
                i = (key_A * alphabet_U.index(letter) + key_B) % lenU
                newLetter = alphabet_U[i]
            else:
                i = (key_A * alphabet_L.index(letter) + key_B) % lenL
                newLetter = alphabet_L[i]
        else:
            newLetter = letter
        crypted += newLetter
    return crypted

def de_affine(alphabet_U: str,alphabet_L: str, text:str, key_A:int, key_B:int):
    lenA = len(alphabet_L)
    multiplicative_inverse = check_affine(lenA, key_A)
        
    if multiplicative_inverse == -1:
        return "Multiplicative Inverse Does not exists"

    decrypted = ""
    for letter in text:
        newLetter = "#"
        if letter.isalpha():
            if letter.isupper():
                i = (multiplicative_inverse * (alphabet_U.index(letter) - key_B)) % lenA
                newLetter = alphabet_U[i]
            else:
                i = (multiplicative_inverse * (alphabet_L.index(letter) - key_B)) % lenA
                newLetter = alphabet_L[i]
        else:
            newLetter = letter
        decrypted += newLetter
    return decrypted

def check_affine(alphabet_Length:int,  key_A:int):
    multiplicative_inverse = -1
    i = 0

    while i < alphabet_Length:
        if (key_A * i) % alphabet_Length == 1:
            multiplicative_inverse = i
            break
        i = i + 1 

    return multiplicative_inverse
    

if __name__ == "__main__":
    main()
