from route import letters

def main():
    text = input("Input Text: ")
    if text == "":
        text = "Kemal Gökçay"
    key_i = input("Input Key: ")
    key = 4

    if key_i != "":
        try:
            key = int(key_i) 
        except:
            print("Invalid key. Key must be an integer.")
            exit(1)
    text = letters(text)
    cip = zigzag(text,key)
    print(f"Cipher: {cip}")
    decip = de_zigzag(cip, key)
    print(f"Decipher: {decip}")


def zigzag(text:str, key:int):
    crypted = ""
    row = key
    col = len(text)
    grid = list("."*row * col)
    i = 0
    j= 0
    while j < col:
        while i < row:
            if j == col:
                break
            grid[(i * col) + j ] = text[j]
            i += 1
            j += 1
        i -= 2

        while i > 0:
            if j == col:
                break
            grid[(i * col) + j ] = text[j]
            i -= 1
            j += 1

    for i in range(row):
        for j in range(col):
            print(grid[(i * col) + j], end="")
        print() 

    for char in grid:
        if char != ".":
            crypted += char
    return crypted

def de_zigzag(text:str, key:int):
    uncrypted = ""
    row = key
    col = len(text)
    grid = list("."*row * col)
    crd = zigzag_coordinates(row, col)
    crd.sort()
    i = 0
    for c in crd:
        if i == len(text):
            break
        grid[(c[0] * col) + c[1]] = text[i]
        i += 1

    for i in range(row):
        for j in range(col):
            print(grid[(i * col) + j], end="")
        print()

    i = 0
    crd = zigzag_coordinates(row, col)
    for c in crd:
        if i == len(text):
            break
        uncrypted += grid[(c[0] * col) + c[1]]
    
    return uncrypted

def zigzag_coordinates(row:int, col:int):
    result = []
    i = 0
    j = 0
    while j < col:
        while i < row:
            if j == col:
                break
            result.append((i,j))
            i += 1
            j += 1
        i -= 2

        while i > 0:
            if j == col:
                break
            result.append((i,j))
            i -= 1
            j += 1
    return result

if __name__ == "__main__":
    main()
