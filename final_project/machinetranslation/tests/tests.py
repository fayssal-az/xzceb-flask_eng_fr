import unittest

import translator

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        #self.assertEqual(translator.english_to_french())
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):
        #self.assertEqual(translator.french_to_english())
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')




if __name__ == '__main__':
    unittest.main()