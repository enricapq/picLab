class PixelColor:

    def __init__(self, red, green, blue):
        """
        Represents color of a single pixel in RGB space
        """
        if self.is_valid_color(red) and self.is_valid_color(blue) and self.is_valid_color(green):
            self.red = red
            self.green = green
            self.blue = blue
        else:
            raise ValueError('Color values are not valid')

    @staticmethod
    def is_valid_color(color):
        if not isinstance(color, int):
            return False
        try:
            return True if 0 <= color <= 255 else False
        except:
            return False

    def as_triple(self):
        return (self.red, self.green, self.blue)


    def __str__(self):
        return "color {0}, {1}, {2}".format(self.red, self.green, self.blue)