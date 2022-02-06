# -*- coding: utf-8 -*-
"""
testy
"""

from nghh import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        m = "abc"
        our = SHA_512_256(m)
        
        official = 0x53048E2681941EF99B2E29B76B4C7DABE4C2D0C634FC6D46E0E2F13107E7AF23
        self.assertEqual(our, official)
        self.assertEqual(hex(our), hex(official))
        
    def test_2(self):
        m = "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
        our = SHA_512_256(m)
        official = 0x3928E184FB8690F840DA3988121D31BE65CB9D3EF83EE6146FEAC861E19B563A
        self.assertEqual(our, official)
        self.assertEqual(hex(our), hex(official))



if __name__ == '__main__':
    unittest.main()
