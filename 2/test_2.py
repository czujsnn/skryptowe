import skrypt_2
import unittest
import re

class test_re(unittest.TestCase):
    def test_only_word(self):
        self.assertEqual(skrypt_2.text_extract("Ala"), ([],["Ala"]))

    def test_only_word2(self):
        self.assertEqual(skrypt_2.text_extract("Ala. ma. kota"), ([],["Ala","ma","kota"]))

    def test_only_number(self):
        self.assertEqual(skrypt_2.text_extract("123"), (["123"],[]))

    def test_only_number2(self):
        self.assertEqual(skrypt_2.text_extract("2137166677788899.999712463268731477"), (["2137166677788899","999712463268731477"],[]))

    def test_2word_number(self):
        self.assertEqual(skrypt_2.text_extract("Ala ma kota123456oraz psa"), (["123456"],["Ala","ma","kota","oraz","psa"]))

    def test_word_2number(self):
        self.assertEqual(skrypt_2.text_extract("1234Ala5678"), (["1234","5678"],["Ala"]))

    def test_word_number(self):
        self.assertEqual(skrypt_2.text_extract("Ala1234"), (["1234"],["Ala"]))

if __name__ == '__main__':
    unittest.main()