import unittest
from pixelcolor import PixelColor

class TestPixelColor(unittest.TestCase):

    def test_check_color(self):
        self.assertTrue(PixelColor.is_valid_color(0))
        self.assertTrue(PixelColor.is_valid_color(255))
        self.assertTrue(PixelColor.is_valid_color(5))
        self.assertFalse(PixelColor.is_valid_color(256))
        self.assertFalse(PixelColor.is_valid_color(-1))
        self.assertFalse(PixelColor.is_valid_color('s'))
        self.assertFalse(PixelColor.is_valid_color(''))
        self.assertFalse(PixelColor.is_valid_color(2.43))
        self.assertFalse(PixelColor.is_valid_color('#ff0000'))
        self.assertTrue(PixelColor.is_valid_color(0X21))


    def test_returns_triple(self):
        color = PixelColor(121, 12, 14)
        self.assertEquals(color.as_triple(), (121, 12, 14))


    def test_object_init(self):
        self.assertIsInstance(PixelColor(121, 12, 14), PixelColor)
        self.assertRaises(ValueError, PixelColor(259, 12, 0))


if __name__ == '__main__':
    unittest.main()