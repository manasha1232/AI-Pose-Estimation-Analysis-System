from src.geometry import calculate_angle

def test_calculate_angle():
    assert int(calculate_angle((0,1), (0,0), (1,0))) == 90
