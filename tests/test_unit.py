import pytest
from module import Module
from unit import Unit


def make_unit():
    m1 = Module("MTI", "Methods", 3, 5, hours_tp=1.5)
    m2 = Module("AABD", "Database", 2, 4, hours_tp=1.5)
    m1.set_grade(tp=10, exam=12)   # 11.2
    m2.set_grade(tp=8, exam=6)     # 6.8
    return Unit("UEM11", "UE Méthodologie", [m1, m2])


def test_unit_coef_credit():
    u = make_unit()
    assert u.coef == 5 and u.credit == 9


def test_unit_average():
    assert make_unit().calculate_average() == pytest.approx((11.2 * 3 + 6.8 * 2) / 5)


def test_unit_not_acquired_sums_module_credits():
    u = make_unit()
    assert u.calculate_average() < 10
    assert u.calculate_credits() == 5                # only MTI


def test_no_shared_default_list():
    a, b = Unit("A", "a"), Unit("B", "b")
    a.add_module(Module("M", "m"))
    assert len(b.modules) == 0


def test_empty_unit():
    u = Unit("E", "empty")
    assert u.calculate_average() == 0 and u.calculate_credits() == 0


def test_unit_compensation_gives_all_credits():
    u = make_unit()
    u._modules[1].set_grade(tp=12, exam=12)   # raises unit average above 10
    assert u.calculate_average() >= 10
    assert u.calculate_credits() == 9
