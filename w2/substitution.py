import math
import random
from route import letters

def main():
    text = input("Text: ")
    if text == "":
        text = "Kemal Gökçay"

    text = letters(text)
    key = 4
    key_input = input("Input Key: ")
    if key_input != "":
        try:
            key = int(key_input)
        except:
            print("Invalid key. Key must be an integer.")
            exit(1)
    
    print(f"Input:     {text}")

    crypted = substitute(text, key)
    print(f"Crypted:   {crypted}")

    uncrypted = de_substitue(crypted, key)
    print(f"Uncrypted: {uncrypted}")


def substitute(text:str, key:str):
    crypted = ""
    col = key
    row = math.ceil(len(text) / key)
    if row * col > len(text):
        text += "a" * (row * col - len(text))

    text_chunks = []
    for i in range(0, len(text), col):
        text_chunks.append(text[i:i+col])

    for i in range(col):
        for j in range(row):
            crypted += text_chunks[j][i]

    return crypted

def de_substitue(text:str, key:str):
    uncrypted = ""
    row = key
    col = len(text) // key

    text_chunks = []
    for i in range(0, len(text), col):
        text_chunks.append(text[i:i+col])

    for i in range(col):
        for j in range(row):
            uncrypted += text_chunks[j][i]

    return uncrypted

def shuffle(text: str):
    text = list(text)
    random.shuffle(text)
    return "".join(text)

if __name__ == "__main__":
    main()
