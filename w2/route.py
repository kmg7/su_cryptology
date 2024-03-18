from math import ceil

def main():
    text = 'Kemal Gokcay'
    key = 4
    
    key_input = input("Input Key: ")
    if key_input != "":
        try:
            key = int(key_input)
        except:
            print("Invalid key. Key must be an integer.")
            exit(1)
    
    text_input = input("Input Text: ")
    if text_input != "":
        text = text_input

    text = letters(text)
    print(f"Key:   {key}")

    cipher = route(key, text)
    print(f"Cipher: {cipher}")
    print(f"Decipher: {de_route(key, cipher)}")

def route(key:int, text:str):
    crypted = ""
    col= key

    row= ceil(len(text) / key)
    if row * col > len(text):
        text += "a" * (row * col - len(text))

    soi = spiral_order_indexes_b_l(row, col)

    for i in soi:
        crypted += text[(i[0] * col) + i[1]]

    return crypted

def de_route(key:int, ciphered:str):
    col= key
    row= ceil(len(ciphered) / key)
    uncrypted = list("#"*col*row)

    soi = spiral_order_indexes_b_l(row, col)
    j = 0
    for i in soi:
        index = (i[0] * col) + i[1]
        uncrypted[index]= ciphered[j]
        j += 1

    return "".join(uncrypted)

def letters(text:str):
    return "".join([i.lower() for i in text if i.isalpha()])

def spiral_order_indexes_b_l(m, n):
    result = []
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1

    # while len(result) < m * n:
    while top <= bottom and left <= right:
        # Go up
        for i in range(left,bottom + 1)[::-1]:
            result.append((i,left))
        left += 1

        # Go right
        for i in range(left,right + 1):
            result.append((top,i))
        top += 1

        # Go down
        for i in range(top,bottom + 1):
            result.append((i,right))
        right -= 1

        # Go left
        for i in range(left, right + 1)[::-1]:
            result.append((bottom,i))
        bottom -= 1

    return result[:m*n] # Remove extra elements sometimes added by accident

if __name__ == "__main__":
    main() 