from hypothesis import given
import hypothesis.strategies as st

from .increment import increment


@given(st.integers())
def test_increment(number):
    assert increment(number) == number + 1
