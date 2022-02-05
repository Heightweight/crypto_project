import unittest
from tdea_encryption import *

class MyTestCase(unittest.TestCase):
    def test_reversible(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x80\x00\x00\x00\x00\x00\x00\x00'

        K = 8

        K_1 = b'\x01\x01\x01\x01\x01\x01\x01\x01'
        K_2 = b'\x01\x01\x01\x01\x01\x01\x01\x01'

        KEY = K_1 + K_2

        self.assertEqual(P.hex(), tcfb_decrypt(bytes.fromhex(tcfb_encrypt(P, K, IV, KEY)),K,IV,KEY))

    def test_variable_plaintext(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x10\x00\x00\x00\x00\x00\x00\x00'

        K=8

        K_1=b'\x01\x01\x01\x01\x01\x01\x01\x01'
        K_2=b'\x01\x01\x01\x01\x01\x01\x01\x01'

        KEY = K_1 + K_2

        result = b'\x95\xF8\xA5\xE5\xDD\x31\xD9\x00'.hex()
        self.assertEqual(result, tcfb_encrypt(P, K, IV, KEY))

    def test_variable_key(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        K = 8

        K_1 = b'\x80\x01\x01\x01\x01\x01\x01\x01'
        K_2 = b'\x80\x01\x01\x01\x01\x01\x01\x01'

        KEY = K_1 + K_2

        result = b'\x95\xa8\xd7\x28\x13\xda\xa9\x4d'.hex()

        self.assertEqual(result, tcfb_encrypt(P, K, IV, KEY))

if __name__ == '__main__':
    unittest.main()
