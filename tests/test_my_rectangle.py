import pytest
from source.class_shapes import rectangle

@pytest.fixture
def rectangle_fixture():
    # Create a rectangle object with length 4 and width 3
    return rectangle(4, 3)

def test_area(rectangle_fixture):
    # Test the area calculation of a rectangle
    assert rectangle_fixture.area() == 12

def test_perimeter(rectangle_fixture):
    # Test the perimeter calculation of a rectangle
    assert rectangle_fixture.perimeter() == 14

def test_equal(rectangle_fixture):
    # Test the equality of two rectangles
    rect1 = rectangle(4, 3)
    rect2 = rectangle(4, 3)
    assert rect1 == rect2

def test_not_equal(rectangle_fixture):
    # Test the inequality of two rectangles
    rect1 = rectangle(4, 3)
    rect2 = rectangle(3, 4)
    assert rect1 != rect2
@pytest.mark.parametrize("length, width, expected_area", [
    (2, 5, 10),
    (3, 4, 12),
    (6, 2, 12)
])
def test_multiple_rectangle(length, width, expected_area):
    # Create a rectangle object with the given dimensions
    rect = rectangle(length, width)

    # Test the area calculation of the rectangle
    assert rect.area() == expected_area