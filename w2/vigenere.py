from route import letters

def main():
    text = input("Text: ")
    if text == "":
        text = "Kemal Gökçay"
    key = input("Input Key: ")
    if key == "":
        key = "vigenere"

    key = letters(key)
    text = letters(text)
    cip = vigenere(text, key)
    print(f"Cipher: {cip}")    
    print(f"Decipher: {de_vigenere(cip, key)}")

def vigenere(text:str, key:str):
    alphabet= 'abcçdefgğhıijklmnoöprsştuüvyz'
    len_alphabet = len(alphabet)
    crypted = ""
    len_text = len(text) 
    len_key = len(key)

    if len_text % len_key != 0:
        text += "a" * (len_key - (len_text % len_key))

    key_indexes = vigenere_key_indexes(key)

    text_chunks = []
    for i in range(0, len_text, len_key):
        text_chunks.append(text[i:i+len_key])

    print(text_chunks)

    for chunk in text_chunks:
        for i, char in enumerate(chunk):
            crypted += alphabet[(alphabet.index(char) + key_indexes[i]) % len_alphabet]
    return crypted

def de_vigenere(ciphered:str, key:str):
    alphabet= 'abcçdefgğhıijklmnoöprsştuüvyz'
    len_alphabet = len(alphabet)
    uncrypted = ""
    len_ciphered = len(ciphered) 
    len_key = len(key)
    key_indexes = vigenere_key_indexes(key)

    text_chunks = []
    for i in range(0, len_ciphered, len_key):
        text_chunks.append(ciphered[i:i+len_key])

    print(text_chunks) 
    for chunk in text_chunks:
        for i, char in enumerate(chunk):
            uncrypted += alphabet[(alphabet.index(char) - key_indexes[i]) % len_alphabet]
    return uncrypted
    
def vigenere_key_indexes(key:str):
    alphabet= 'abcçdefgğhıijklmnoöprsştuüvyz'
    key_indexes = []
    for i in key:
        key_indexes.append(alphabet.index(i))
    return key_indexes

if __name__ == "__main__":
    main()