import pytest
from case.test_case import Test_A


class Test_AA:
    def test_dd(self):
        lp = Test_A()
        lp.test_a()


if __name__ == '__main__':
    pytest.main('-s', './')

