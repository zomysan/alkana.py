import unittest

from alkana.console import parse_args


class TestArgParser(unittest.TestCase):
    def test_argparser_help(self):
        with self.assertRaises(SystemExit, msg=0):
            parse_args(test=['-h'])

    def test_argparser_version(self):
        with self.assertRaises(SystemExit, msg=0):
            parse_args(test=['-v'])

    def test_argparser_invalid(self):
        with self.assertRaises(SystemExit, msg=1):
            parse_args(test=['-V'])

    def test_argparser_word(self):
        args = parse_args(test=['hello'])
        self.assertEqual(args.word, 'hello')

    def test_argparser_invalid_words(self):
        with self.assertRaises(SystemExit, msg=1):
            parse_args(test=['hello', 'world'])
