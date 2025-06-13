import pytest
import importlib
import class_inheritance as ci
import random

@pytest.fixture(autouse=True)
def reload_module():
    importlib.reload(ci)
    yield

def test_shape():
    s = ci.Shape()
    assert s.member_count == 1
    assert s.area() is None
    assert s.show_area() is None

@pytest.mark.parametrize(
    ("width", "height", "expected_area", "expected_output"),
    [
        (None, None, 0.5, "面積は0.5です"),
        (10, 5, 25, "面積は25.0です"),
    ]
)
def test_triangle(capsys, width, height, expected_area, expected_output):
    if width is None or height is None:
        t = ci.Triangle()
    else:
        t = ci.Triangle(base=width, height=height)
    assert t.area() == expected_area
    t.show_area()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output
    
@pytest.mark.parametrize(
    ("width", "height", "expected_area", "expected_output"),
    [
        (None, None, 1, "面積は1です"),
        (10, 5, 50, "面積は50です"),
    ]
)
def test_rectangle(capsys, width, height, expected_area, expected_output):
    if width is None or height is None:
        r = ci.Rectangle()
    else:
        r = ci.Rectangle(width=width, height=height)
    assert r.area() == expected_area
    r.show_area()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output

def test_shape_member_count():
    count = [random.randint(1, 10) for _ in range(2)]
    for _ in range(count[0]):
        ci.Rectangle()
    for _ in range(count[1]):
        ci.Triangle()

    assert ci.Shape.member_count == count[0] + count[1]
