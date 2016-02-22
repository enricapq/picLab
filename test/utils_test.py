import unittest
from utils import *



class TestUtils(unittest.TestCase):

    def test_check_path_validity(self):
        self.assertTrue(check_path_validity('../test'))
        self.assertFalse(check_path_validity('../fake'))
        self.assertFalse(check_path_validity(123))
        self.assertFalse(check_path_validity(' '))
        self.assertFalse(check_path_validity('../test,../../mosaic_folder'))
        with self.assertRaises(TypeError):
            check_path_validity('../test','../mosaic_folder')


    def test_check_path_validity_traversable(self):
        self.assertTrue(check_path_validity_traversable('../test','../mosaic_folder'))
        self.assertTrue(check_path_validity_traversable('../test'))
        self.assertFalse(check_path_validity_traversable(' '))
        self.assertFalse(check_path_validity_traversable('../test',' '))
        self.assertFalse(check_path_validity_traversable('../test','../../mosaic_folder'))


if __name__ == '__main__' :
    unittest.main()