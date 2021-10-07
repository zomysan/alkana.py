import unittest
import os

import alkana


class TestExternalData(unittest.TestCase):
    def tearDown(self):
        alkana.data.data.pop("mmmmm")

    def test_add_external_data_default(self):
        self.assertEqual(None, alkana.get_kana('mmmmm'))
        file_path = os.path.join(os.path.dirname(
            __file__), 'sample_external_data.csv')
        alkana.add_external_data(file_path)
        self.assertEqual('テスト', alkana.get_kana('mmmmm'))

    def test_add_external_data_shiftJIS(self):
        self.assertEqual(None, alkana.get_kana('mmmmm'))
        file_path = os.path.join(os.path.dirname(
            __file__), 'sample_external_data_shiftJIS.csv')
        alkana.add_external_data(file_path, "shift_jis")
        self.assertEqual('テスト', alkana.get_kana('mmmmm'))

    def test_add_external_data_utf8(self):
        self.assertEqual(None, alkana.get_kana('mmmmm'))
        file_path = os.path.join(os.path.dirname(
            __file__), 'sample_external_data_utf8.csv')
        alkana.add_external_data(file_path, "utf-8")
        self.assertEqual('テスト', alkana.get_kana('mmmmm'))
