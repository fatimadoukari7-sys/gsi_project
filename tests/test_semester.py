import pytest
from academicelement import AcademicElement
from main import build_semester1, build_semester2, find_module


def test_semester_is_academic_element():
    assert isinstance(build_semester1(), AcademicElement)


def test_cannot_instantiate_abstract():
    with pytest.raises(TypeError):
        AcademicElement("a", "b")


@pytest.mark.parametrize("builder", [build_semester1, build_semester2])
def test_canvas_totals(builder):
    s = builder()
    assert s.coef == 17
    assert s.credit == 30


def test_semester1_hours():
    assert build_semester1().total_hours == 360


def test_all_grades_20_gives_30_credits():
    s = build_semester1()
    for u in s.units:
        for m in u.modules:
            m.set_grade(tp=20, td=20, exam=20)
    assert s.calculate_average() == pytest.approx(20)
    assert s.calculate_credits() == 30


def test_no_grades_gives_zero():
    s = build_semester2()
    assert s.calculate_average() == 0
    assert s.calculate_credits() == 0


def test_compensation_at_semester_level():
    s = build_semester1()
    for u in s.units:
        for m in u.modules:
            m.set_grade(tp=12, td=12, exam=12)
    find_module(s, "F112").set_grade(tp=0, exam=0)
    assert s.calculate_average() >= 10
    assert s.calculate_credits() == 30
