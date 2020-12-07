import unittest
import os

import alkana


class TestExternalData(unittest.TestCase):
    def test_add_external_data(self):
        self.assertEqual(None, alkana.get_kana('mmmmm'))
        file_path = os.path.join(os.path.dirname(__file__), 'sample_external_data.csv')
        alkana.add_external_data(file_path)
        self.assertEqual('テスト', alkana.get_kana('mmmmm'))
