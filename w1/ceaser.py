import sys
from shift import shift, de_shift

def main():
    TUR_U= 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    TUR_L= 'abcçdefgğhıijklmnoöprsştuüvyz'
    text= "Kemal Gökçay"
    
    if len(sys.argv )> 1: 
        text = sys.argv[1]
    
    print(f"Input:     {text}")

    crypted = ceaser(TUR_U, TUR_L,text)
    print(f"Crypted:   {crypted}")

    uncrypted = de_ceaser(TUR_U, TUR_L, crypted)
    print(f"Uncrypted: {uncrypted}")

def ceaser(alphabet_U:str, alphabet_L: str, text:str):
    return shift(alphabet_U, alphabet_L, text, 3)

def de_ceaser(alphabet_U:str, alphabet_L: str, text:str):
    return de_shift(alphabet_U, alphabet_L, text, 3)

if __name__ == "__main__":
    main()