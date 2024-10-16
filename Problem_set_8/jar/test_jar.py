import pytest
from jar import Jar

class TestJar:
    def test_init_with_default_capacity(self):
        jar = Jar()
        assert jar.capacity == 12
        assert jar.size == 0

    def test_init_with_custom_capacity(self):
        jar = Jar(capacity=20)
        assert jar.capacity == 20
        assert jar.size == 0

    def test_init_with_negative_capacity(self):
        with pytest.raises(ValueError):
            Jar(capacity=-5)

    def test_deposit_within_capacity(self):
        jar = Jar(capacity=10)
        jar.deposit(5)
        assert jar.size == 5

    def test_deposit_exceeding_capacity(self):
        jar = Jar(capacity=10)
        with pytest.raises(ValueError):
            jar.deposit(11)

    def test_withdraw_within_available_cookies(self):
        jar = Jar(capacity=10)
        jar.deposit(5)
        jar.withdraw(2)
        assert jar.size == 3

    def test_withdraw_more_cookies_than_available(self):
        jar = Jar(capacity=10)
        jar.deposit(5)
        with pytest.raises(ValueError):
            jar.withdraw(6)

    def test_capacity_and_size(self):
        jar = Jar(capacity=15)
        jar.deposit(8)
        assert jar.capacity == 15
        assert jar.size == 8