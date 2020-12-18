from hypothesis import strategies as st
from hypothesis import given

def my_deduct(a, b):
    return (10**90 * a - 10**90 * b) / 10**90

@given(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=10))
def test_my_deduction(a, b):
    assert int(my_deduct(a, b)) == a - b