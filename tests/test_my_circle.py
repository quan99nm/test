import math
import pytest
from source.class_shapes import Shape, Circle



class TestCircle:
    def setup_method(self, method):
        # This method is called before each test method in the class
        self.circle = Circle(5)

    def teardown_method(self, method):
        # This method is called after each test method in the class
        self.circle = None

    def test_area(self):
        # Test the area calculation of a circle
        assert math.isclose(self.circle.area(), 78.53981633974483, rel_tol=1e-9)

    def test_perimeter(self):
        # Test the perimeter calculation of a circle
        assert math.isclose(self.circle.perimeter(), 31.41592653589793, rel_tol=1e-9)
    "test area of rectangle compare with area of circle"
class TestShape:
    def setup_method(self, method):
        # This method is called before each test method in the class
        self.shape = Shape()

    def teardown_method(self, method):
        # This method is called after each test method in the class
        self.shape = None

    def test_area(self):
        # Test the area method of the Shape class
        assert self.shape.area() == None

    def test_perimeter(self):
        # Test the perimeter method of the Shape class
        assert self.shape.perimeter() == None