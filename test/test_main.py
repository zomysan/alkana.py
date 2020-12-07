import unittest

import alkana


class TestMain(unittest.TestCase):
    def test_get_kana(self):
        self.assertEqual('ハロー', alkana.get_kana('hello'))

    def test_get_kana_upper_case(self):
        self.assertEqual('ワールド', alkana.get_kana("World"))

    def test_get_kana_none_case(self):
        self.assertEqual(None, alkana.get_kana("abcdefg"))


if __name__ == "__main__":
    unittest.main()
