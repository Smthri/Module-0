from minitorch import operators
from hypothesis import given
from hypothesis.strategies import lists
from .strategies import small_floats, assert_close
import pytest


@pytest.mark.task0_1
@given(small_floats, small_floats)
def test_add_and_mul(x, y):
    assert_close(operators.mul(x, y), x * y)
    assert_close(operators.add(x, y), x + y)
    assert_close(operators.neg(x), -x)


@pytest.mark.task0_1
@given(small_floats)
def test_relu(a):
    if a > 0:
        assert operators.relu(a) == a
    else:
        assert operators.relu(a) == 0.0


## Task 0.2
## Property Testing


@pytest.mark.task0_2
@given(small_floats, small_floats)
def test_symmetric(x, y):
    """
    Write a test that ensures that :func:`minitorch.operators.mul` is symmetric, i.e.
    gives the same value regardless of the order of its input.
    """
    assert_close(operators.mul(x, y), operators.mul(y, x))


@pytest.mark.task0_2
@given(small_floats, small_floats, small_floats)
def test_distribute(x, y, z):
    r"""
    Write a test that ensures that your operators distribute, i.e.
    :math:`z \times (x + y) = z \times x + z \times y`
    """
    a = operators.mul(z, operators.add(x, y))
    b = operators.add(operators.mul(x, z), operators.mul(y, z))
    assert_close(a, b)


@pytest.mark.task0_2
@given(small_floats, small_floats, small_floats)
def test_other(x, y, z):
    """
    Write a test that ensures some other property holds for your functions.
    Associativity.
    """
    a = operators.mul(x, operators.mul(y, z))
    b = operators.mul(operators.mul(x, y), z)
    assert_close(a, b)


# HIGHER ORDER


@pytest.mark.task0_3
@given(small_floats, small_floats, small_floats, small_floats)
def test_zip_with(a, b, c, d):
    assert_close(operators.addLists([a, b], [c, d]), [a + c, b + d])


@pytest.mark.task0_3
@given(
    lists(small_floats, min_size=5, max_size=5),
    lists(small_floats, min_size=5, max_size=5),
)
def test_property(ls1, ls2):
    """
    Write a test that ensures that the sum of `ls1` plus the sum of `ls2`
    is the same as the sum of each element of `ls1` plus each element of `ls2`.
    """
    a = sum(ls1) + sum(ls2)
    b = sum([sum(z) for z in zip(ls1, ls2)])
    assert_close(a, b)


@pytest.mark.task0_3
@given(lists(small_floats))
def test_sum(ls):
    assert_close(operators.sum(ls), sum(ls))


@pytest.mark.task0_3
@given(small_floats, small_floats, small_floats)
def test_prod(x, y, z):
    assert_close(operators.prod([x, y, z]), x * y * z)
