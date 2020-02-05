"""
Unit and regression test for the molecool.measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import numpy as np

def test_calculate_distance():
    """Tests if distances between points are calculated correctly"""
    r1 = np.array([0., 0., 0.])
    r2 = np.array([0., 1., 0.])

    expected_distance = 1.0

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

#Testing expected exceptions
def test_calculate_distance_typeerror():
    r1 = [0., 0., 0.]
    r2 = [1., 0., 0.]

    with pytest.raises(TypeError):
        molecool.calculate_distance(r1, r2)

# in quotes ar ethe variables that need to change for every test using calculate_angle
@pytest.mark.parametrize('p1, p2, p3, expected_angle', [
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, 0]), np.array([1, 0, 0]), 45),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)
])
def test_calculate_angle(p1, p2, p3, expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)
    assert expected_angle == pytest.approx(calculated_angle)
