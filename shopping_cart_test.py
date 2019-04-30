import pytest # for pytest.raises (see: https://docs.pytest.org/en/latest/assert.html)

from shopping_cart import TAX_RATE, to_usd, find_product

def test_tax_rate():
    assert(TAX_RATE) == 0.06

def test_to_usd():
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"