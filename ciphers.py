class Cipher:
    #cipher class that raises errors if encrypt and decrypt methods arent
    #implemented in subclasses
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
