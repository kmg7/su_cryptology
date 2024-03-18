from route import letters
import random

def main():
    text = input("Input Text: ")
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyzx'
    key_l = list(alphabet)
    random.shuffle(key_l)
    key = "".join(key_l)
    if text == "":
        text = "Kemal Gökçay"

    text = letters(text)
    cip = fsquare(text, alphabet, key)
    print(f"Key: {key}")
    print(f"Cipher: {cip}")
    print(f"Decipher: {de_fsquare(cip, alphabet, key)}")

def fsquare(text:str, alphabet:str, key:str):
    crypted = ""
    if len(text) %2 != 0:
        text += "a"
    
    text_chunks = []
    for i in range(0, len(text), 2):
        text_chunks.append(text[i:i+2])

    print(text_chunks)

    for chunk in text_chunks:
        a = index_of_char(chunk[0], alphabet)
        ax = a[0]
        b = index_of_char(chunk[1], alphabet)
        bx = b[0]
        crypted += char_of_index((bx, a[1]), key)+ char_of_index((ax, b[1]), key)

    return crypted

def de_fsquare(ciphered:str, alphabet:str, key:str):
    uncrypted = ""
    
    text_chunks = []
    for i in range(0, len(ciphered), 2):
        text_chunks.append(ciphered[i:i+2])

    print(text_chunks)

    for chunk in text_chunks:
        a = index_of_char(chunk[0], key)
        ax = a[0]
        b = index_of_char(chunk[1], key)
        bx = b[0]
        uncrypted += char_of_index((bx, a[1]), alphabet)+ char_of_index((ax, b[1]), alphabet)

    return uncrypted

def index_of_char(char:str, alphabet:str):
    i = alphabet.index(char)
    return (i // 5, i % 5)

def char_of_index(index:tuple, alphabet:str):
    return alphabet[index[0] * 5 + index[1]]

if __name__ == "__main__":
    main()