
# PEasyCrypt: A Very Small, Portable, Simple (~100 Lines!) Encryption Library

Here is a small library that I wrote just for fun. If you provide a key that is the same length as the file/bytes to be encrypted, this algorithm is unbreakable (see [XOR cipher](http://en.wikipedia.org/wiki/XOR_cipher) and [One Time Pad](http://en.wikipedia.org/wiki/One_time_pad)).


## The Code

    #!/usr/bin/python3.0

    class Key:
      
      def __init__(self, bytesKey):
        self.__key = bytesKey
      
      def getAt(self, x):
        x = x % len(self.__key)
        return self.__key[x]
      
    class Crypt_Xor:
      
      def __init__(self, key):
        self.__key = key
      
      def encrypt(self, bytesToCrypt):
        bytesCrypt = bytearray(len(bytesToCrypt))
        x = 0
        for byte in bytesToCrypt:
          key_node = self.__key.getAt(x)
          bytesCrypt[x] = byte ^ key_node
          x += 1    
        return bytesCrypt
        
      def decrypt(self, bytesToDecrypt):
        bytesDeCrypt = bytearray(len(bytesToDecrypt))
        x = 0
        lstDecrypted = []
        for char in bytesToDecrypt:
          key_node = self.__key.getAt(x)
          bytesDeCrypt[x] = bytesToDecrypt[x] ^ key_node
          x += 1
        
        return bytesDeCrypt
        
    def _test_crypt_object( crypt ):
      data_orig = b'I am a simple string to be encrypted.'
      print( 'data_orig: %s' % data_orig )

      testKey = b'My secret key... \x123\x456\x798'  
      
      crypt = crypt( Key(testKey) )
      data_encoded = crypt.encrypt(data_orig)
      print( 'data_encoded: %s' % data_encoded )
      data_decoded = crypt.decrypt(data_encoded)
      print( 'data_decoded: %s' % data_decoded )
      
      assert data_decoded == data_orig 

    def test_module():
      print( 'da_crypt test start' )
      _test_crypt_object(Crypt_Xor)
      print( 'da_crypt test end' )

    if __name__ == '__main__':
      test_module()


## Extension to Allow File Encryption
    #!/usr/bin/python3.0

    """
    Extensions that allow more complex 'stuff'.
    """

    import da_crypt

    class File_Crypt_Xor:
      
      def __init__(self, key):
        self.__byteCrypter = da_crypt.Crypt_Xor(key)
      
      def encrypt(self, fileToCrypt, fileOutput):
        fh = open(fileToCrypt, 'rb')
        bytes = fh.read()
        fh.close()
        bytes_encr = self.__byteCrypter.encrypt(bytes)
        fh = open(fileOutput, 'wb')
        fh.write(bytes_encr)
        fh.close()
        
      def decrypt(self, fileToDecrypt, fileoutDecr):
        fh = open(fileToDecrypt, 'rb')
        bytes = fh.read()
        fh.close()
        bytes_decr = self.__byteCrypter.decrypt(bytes)
        fh = open(fileoutDecr, 'wb')
        fh.write(bytes_decr)
        fh.close()

    def _test_file_crypt_object( crypt ):
      
      testKey = b'My secret key... \x123\x456\x798'  
      
      crypt = crypt( da_crypt.Key(testKey) )
      
      filename_before_encr = 'test_data.jpg'
      filename_encr = 'test_data.jpg.encrypted'
      filename_decr = 'test_data.decrypted.jpg'
      
      data_encoded = crypt.encrypt(filename_before_encr, filename_encr)
      data_decoded = crypt.decrypt(filename_encr, filename_decr)
      
      fh_be = open(filename_before_encr, 'rb')
      fh_ae = open(filename_decr, 'rb')
      
      assert fh_be.read() == fh_ae.read()

    def test_module():
      print( 'da_crypt test start' )
      _test_file_crypt_object(File_Crypt_Xor)
      print( 'da_crypt test end' )

    if __name__ == '__main__':
      test_module()

## Comments

The amazing thing is that it can be fully implemented with very little code (31 lines in this case). I got the idea reading the excellent book '[Computer Networks by Andrew S.Tanenbaum, section 8.1.4](http://books.google.com/books?id=Pd-z64SJRBAC&amp;lpg=PP1&amp;dq=Computer%20Networks%20by%20Andrew%20S.Tanenbaum&amp;pg=PP1#v=onepage&amp;q&amp;f=false).

## CMS

You can check the updated code at [google code](http://code.google.com/p/miscdev/source/browse/da_crypt/) or just clone it with mercurial:

    hg clone https://miscdev.googlecode.com/hg/ miscdev 

Be careful though: the implementation uses a circular key (for simplicity's sake). If you use a key that is not random or that is less than the size of the data to be encrypted, then it becomes relatively easy to crack.

Enjoy! Encrypt!

