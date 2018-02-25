#imports
from affine import Affine
from caesar import Caesar
from mykeyword import Keyword
from transposition import Transposition

def run_cipher():
    #print welcome and available ciphers
    print("Welcome to myCipher. We can encrypt or decrypt using the following ciphers: \n")
    print(" -Affine Cipher\n")
    print(" -Caesar Cipher\n")
    print(" -Keyword Cipher\n")
    print(" -Transposition Cipher\n")


    #variables
    cipher_invalid = True
    valid_ciphers = ["affine", "caesar", "keyword", "transposition"]
    e_or_d_invalid = True


    #Loop until valid cipher is chosen
    while cipher_invalid:
        cipher = input("Which cipher would you like to use? ").lower()
        if cipher in valid_ciphers:
            cipher_invalid = False
        else:
            print("\nNot valid cipher")


    #loop until encrypt or decrypt is chosen
    while e_or_d_invalid:
        encrypt_or_decrypt = input("Excellent choice! Are you encrypting or decrypting? Type E/d ").lower()
        if encrypt_or_decrypt == "e" or encrypt_or_decrypt == "d":
            e_or_d_invalid = False
        else:
            print("\n Not sure whether to encrypt or decrypt! Type E/d?")


    #give message to encrypt or decrypt
    msg = input("What is your message? ")


    #encrypt or decrypt branching
    if encrypt_or_decrypt == "e":
        if cipher == "caesar":
            e_msg = Caesar().encrypt(msg)
        elif cipher == "affine":
            e_msg = Affine().encrypt(msg)
        elif cipher == "keyword":
            keyword = input("What is your keyword? ")
            e_msg = Keyword(keyword).encrypt(msg)
        elif cipher == "transposition":
            e_msg = Transposition().encrypt(msg)

        print(e_msg)

    else:
        if cipher == "caesar":
            d_msg = Caesar().decrypt(msg)
        elif cipher == "affine":
            d_msg = Affine().decrypt(msg)
        elif cipher == "keyword":
            keyword = input("What is your keyword? ")
            d_msg = Keyword(keyword).decrypt(msg)
        elif cipher == "transposition":
            d_msg = Transposition().decrypt(msg)

        print(d_msg)

#only run when actually meant to run
if __name__ == "__main__":
    run_cipher()
