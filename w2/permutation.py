import random
import string

def main():
    text = input("Text: ")
    if text == "":
        text = "Kemal Gökçay"

    keyinput = input("Key: ")
    fillKey = input("Fill Key: ")
    if fillKey == "":
        fillKey = "a"
    
    key = 0
    if keyinput == "":
        key = 4
    else:
        try:
            key = int(keyinput)
        except ValueError:
            print("Invalid key. Please enter an integer value for the key.")
            exit(1)

    keyList = createKey(key)
    textSplit = split_and_fill_text(key, fillKey, text)
    print(f"Key List: {keyList}") 
    print(f"Input:    {text}")

    
    crypted = permutation(textSplit, keyList)
    print(f"Crypted:   {crypted}")

    cryptedSplit = split_text(key, crypted)
    print(textSplit)
    print(cryptedSplit)

    uncrypted = de_permutation(cryptedSplit, keyList)
    print(f"Uncrypted: {uncrypted}")


def permutation(textList:list[str], keyList:list[int]):
    crypted = ""
    for text in textList:
        cryptedText = ""
        for i in keyList:
            cryptedText += text[i]
        crypted += cryptedText
    return crypted

def de_permutation(textList:str, keyList:list[int]):
    encrypted = ""
    for text in textList:
        decryptedText = list(text)
       
        for i in range(len(keyList)):
            decryptedText[keyList[i]] = text[i]
        encrypted += "".join(decryptedText)
    return encrypted

def split_and_fill_text(key: int, fill_char: str, text: str):
    text = text.translate(str.maketrans("", "", string.whitespace + string.punctuation))
    text = text.lower()
    lenght = len(text)
    if len(text) % key != 0:
        lenght = len(text) + (key - len(text) % key)
    filled_text = text.ljust(lenght,fill_char)
    splitted_text = split_text(key, filled_text)
   
    return splitted_text

def split_text(n: int, text: str):
    splitted_text = []
    for i in range(0, len(text), n):
        chunk = text[i:i+n]
        splitted_text.append(chunk)
    return splitted_text

def createKey(key: int):
    l = list(range(key))
    random.shuffle(l)
    return l

if __name__ == "__main__":
    main()
