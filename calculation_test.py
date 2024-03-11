import pytest
import area_calculation


@pytest.mark.parametrize('string, exp_res', [
    ("3 4 5", "Area of your right triangle: 6.0"),
    ('3 4 10', 'Incorrect Input.'),
    ("3 -4 5", "Incorrect Input. Enter the correct number or numbers."),
])
def test_area(string, exp_res):
    assert area_calculation.area(string) == exp_res
    assert area_calculation.area() == "Incorrect Input."


@pytest.mark.parametrize('x1, x2, x3, exp_res', [
    (3, 4, 5, "Area of your right triangle: 6.0")
])
def test_Triangle(x1, x2, x3, exp_res):
    x = area_calculation.Triangle()
    assert x.area(x1, x2, x3) == exp_res
