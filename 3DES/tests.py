import unittest
from tdea_encryption import *

class MyTestCase(unittest.TestCase):
    def test_PC_1(self):
        K = bytes_to_list(b'\x66\x66\x66\x66\x66\x66\x66\x66')
        PC1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(PC_1(K),PC1)

    def test_left_shift_1(self):
        B = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        B_shift = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

        self.assertEqual(left_shift(0,B),B_shift)

    def test_left_shift_2(self):
        B = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        B_shift = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

        self.assertEqual(left_shift(2,B),B_shift)

    def test_PC_2(self):
        CD = bytes_to_list(b'\x66\x66\x66\x66\x66\x66\x66')
        PC2 = [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0]

        self.assertEqual(PC_2(CD), PC2)

    def test_key_schedule(self):
        K_1 = b'\x88\x88\x88\x88\x88\x88\x88\x88'
        K_2 = b'\x88\x88\x88\x88\x88\x88\x88\x88'

        KEY = bytes_to_list(K_1) + bytes_to_list(K_2)

        PC1 = PC_1(KEY)
        C1 = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        D1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

        C2 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        D2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

        C3 = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
        D3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

        C4 = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        D4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        KEYS = [PC_2(C1+D1), PC_2(C2+D2), PC_2(C3+D3), PC_2(C4+D4)]

        self.assertEqual(key_schedule(KEY)[:4],KEYS)

    def test_reversible(self):
        P = b'\x00\x00\x08\x00\x00\x00\x00\x00'
        IV = b'\x80\x00\x00\x00\x00\x80\x00\x00'

        K = 8

        K_1 = b'\x08\x01\x01\x01\x01\x01\x01\x01'
        K_2 = b'\x08\x01\x01\x01\x01\x01\x01\x01'

        KEY = K_1 + K_2

        self.assertEqual(P.hex(), tcfb_decrypt(bytes.fromhex(tcfb_encrypt(P, K, IV, KEY)),K,IV,KEY))

    def test_variable_plaintext(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x80\x00\x00\x00\x00\x00\x00\x00'

        K=64

        K_1=b'\x01\x01\x01\x01\x01\x01\x01\x01'
        K_2=b'\x01\x01\x01\x01\x01\x01\x01\x01'

        KEY = K_1 + K_2

        result = b'\x95\xF8\xA5\xE5\xDD\x31\xD9\x00'.hex()
        self.assertEqual(result, tcfb_encrypt(P, K, IV, KEY))

    def test_variable_key(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        K = 64

        K_1 = b'\x80\x01\x01\x01\x01\x01\x01\x01'
        K_2 = b'\x80\x01\x01\x01\x01\x01\x01\x01'

        KEY = K_1 + K_2

        result = b'\x95\xa8\xd7\x28\x13\xda\xa9\x4d'.hex()

        self.assertEqual(result, tcfb_encrypt(P, K, IV, KEY))

    def test_permutation_operation(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        K = 64

        K_1 = b'\x10\x46\x91\x34\x89\x98\x01\x31'
        K_2 = b'\x10\x46\x91\x34\x89\x98\x01\x31'

        KEY = K_1 + K_2

        result = b'\x88\xD5\x5E\x54\xF5\x4C\x97\xB4'.hex()

        self.assertEqual(result, tcfb_encrypt(P, K, IV, KEY))

    def test_substitution_table(self):
        P = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        IV = b'\x01\xA1\xD6\xD0\x39\x77\x67\x42'

        K = 64

        K_1 = b'\x7C\xA1\x10\x45\x4A\x1A\x6E\x57'
        K_2 = b'\x7C\xA1\x10\x45\x4A\x1A\x6E\x57'

        KEY = K_1 + K_2

        result = b'\x69\x0F\x5B\x0D\x9A\x26\x93\x9B'.hex()

        self.assertEqual(result, tcfb_encrypt(P, K, IV, KEY))

if __name__ == '__main__':
    unittest.main()
