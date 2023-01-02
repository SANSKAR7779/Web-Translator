import unittest

class TestMyModule(unittest.TestCase):

    def englishtofrench(self):

        self.assertNotEqual(englishtofrench("None"), "")

        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

    def frenchtoenglish(self):

        self.assertNotEqual(frenchtoenglish("None"), "")

        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()