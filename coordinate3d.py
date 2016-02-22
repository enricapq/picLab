class Coordinate3d:
    """
    Represents the coordinates of a point in a 3-dimensional space
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "coordinate x:{0}, y:{1}, z:{2}".format(self.x, self.y, self.z)