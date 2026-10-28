import pytest
from module import Module


def make_mti():
    return Module("MTI", "Methods", coef=3, credit=5, hours_tp=1.5)


def test_total_hours():
    assert make_mti().total_hours == 45


def test_average_tp_only():
    m = make_mti()
    m.set_grade(tp=10, exam=12)
    assert m.calculate_average() == pytest.approx(11.2)


def test_average_tp_and_td():
    m = Module("F111", "Réseaux", 3, 6, 1.5, 1.5, 1.5)
    m.set_grade(tp=10, td=14, exam=10)
    assert m.calculate_average() == pytest.approx(10 * .2 + 14 * .2 + 10 * .6)


def test_missing_grades_count_as_zero():
    assert make_mti().calculate_average() == 0


def test_exam_only_module():
    m = Module("T111", "Cloud", 1, 1, 1.5, continous_percent=0, exam_percent=100)
    m.set_grade(exam=14)
    assert m.calculate_average() == 14


def test_credits_acquired_and_not():
    m = make_mti()
    m.set_grade(tp=10, exam=12)
    assert m.calculate_credits() == 5
    m.set_grade(tp=5, exam=6)
    assert m.calculate_credits() == 0


def test_invalid_grade():
    with pytest.raises(ValueError):
        make_mti().set_grade(tp=25)


def test_invalid_percentages():
    with pytest.raises(ValueError):
        Module("X", "X", continous_percent=50, exam_percent=60)


def test_get_grades_returns_copy():
    m = make_mti()
    g = m.get_grades()
    g["tp"] = 20
    assert m.get_grades()["tp"] is None
