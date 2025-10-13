import pytest

from h2_gelinkte_lijsten.rekenmachine import (    
    evalueer_postfix,
    infix_naar_postfix,
    rekenmachine,
)

@pytest.mark.timeout(2)
@pytest.mark.parametrize("postfix, expected", [
    (["3", "5", "+"],   8.0),    # 3 + 5
    (["3", "5", "*"],   15.0),   # 3 * 5
    (["3", "5", "-"],   -2.0),   # 3 - 5
    (["3", "5", "/"],   0.6),    # 3 / 5
    (["3", "5", "+", "2", "*"], 16.0),  # (3 + 5) * 2
    (["3", "5", "*", "2", "-"], 13.0),  # 3*5 - 2
    (["3", "5", "2", "*", "-"], -7.0),  # 3 - (5*2)
])
def test_evalueer_postfix_dodona(postfix, expected):
    assert evalueer_postfix(postfix) == pytest.approx(expected)


@pytest.mark.timeout(2)
@pytest.mark.parametrize("infix, expected_postfix", [
    (["3", "+", "5"], ['3', '5', '+']),
    (["3", "*", "5"], ['3', '5', '*']),
    (["3", "*", "5", "+", "2"], ['3', '5', '*', '2', '+']),
    (["3", "+", "5", "*", "2"], ['3', '5', '2', '*', '+']),
    (["(", "3", "+", "5", ")", "*", "2"], ['3', '5', '+', '2', '*']),
    (["(", "(", "3", "+", "5", ")", ")", "*", "2"], ['3', '5', '+', '2', '*']),
    (["(", "1", "*", "(", "2", "+", "3", ")", ")", "*", "4"], ['1', '2', '3', '+', '*', '4', '*']),
    (["3","-","5","+","6"], ['3', '5', '-', '6', '+']),
])
def test_infix_naar_postfix_dodona(infix, expected_postfix):
    assert infix_naar_postfix(infix) == expected_postfix


@pytest.mark.timeout(2)
@pytest.mark.parametrize("expr, expected", [
    ("3 + 5", 8.0),
    ("3 + 5 * 2", 13.0),
    ("( 3 + 5 ) * 2", 16.0),
    ("( ( 3 + 5 ) / 8 ) * 2", 2.0),
    ("( 1 + 2 ) * ( 3 + 4 )", 21.0),
    (" 1 + 2  * ( 3 + 4 )", 15.0),
    (" 1 + 2  *  3 + 4 ", 11.0),
    (" ( 1 + ( ( 2  *  3 ) + 4 ) )", 11.0),
    ("10 / 2 * 3", 15.0),
])
def test_rekenmachine_dodona(expr, expected):
    assert rekenmachine(expr) == pytest.approx(expected)




