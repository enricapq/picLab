import unittest
from image_utils import *
from PIL import Image


class TestImageUtils(unittest.TestCase):

    def test_open_image_equals(self):
        image = Image.open('parrot.jpg')
        image_to_test = open_image('parrot.jpg')
        self.assertEqual(image, image_to_test)

    def test_open_image_different(self):
        image = Image.open('cat.jpg')
        image_to_test = open_image('parrot.jpg')
        self.assertNotEquals(image, image_to_test)

    def test_open_image_image_mode_different(self):
        image = Image.open('parrot.jpg')
        image_to_test = open_image('parrot.jpg', image_mode='CMYK')
        self.assertNotEqual(image, image_to_test)

    def test_open_image_image_mode(self):
        image = Image.open('parrot.jpg').convert('CMYK')
        image_to_test = open_image('parrot.jpg', image_mode='CMYK')
        self.assertEqual(image, image_to_test)


if __name__ == '__main__' :
    unittest.main()
