import unittest
import os
import shutil


def create_file(x):
    os.makedirs(x)
    file = open(f'{x}/text.txt', 'w', encoding='utf-8')
    file.write('Вот он!')
    file.close()


class SimpleWidgetTestCase(unittest.TestCase):
    x = r'C:\Users\alina\OneDrive\Desktop\new_file'

    def setUp(self):
        create_file(self.x)

    def test_file(self):
        self.assertTrue(os.path.getsize(self.x) > 0)
        self.assertFalse(os.path.getsize(self.x) == 0)
        with open(f'{self.x}/text.txt', 'r', encoding='utf-8') as file:
            self.assertEqual(file.read, 'Вот он!')

    def tearDown(self):
        shutil.rmtree(self.x)


if __name__ == '__main__':
    unittest.main()
