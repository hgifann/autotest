# __author__ = 'THTF'
# import pytest
import unittest
#
# class Test_AlienTest():
#     @classmethod
#     def setUpClass(cls):
#         print("TestCase  start running ")
#
#     def test_1_run(self):
#         print("hello world_1")
#
#     def test_2_run(self):
#         print("hello world_2")
#
#     def test_3_run(self):
#         print("hello world_3")
#         assert 1==0
#
# if __name__ == "__main__":
#     # pytest.main(['-q test_py1.py'])
#     pytest.main(['test_py1.py'])
#
#     # pytest.main('-q test_class.py')

import pytest

data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]


def add(a, b):
    return a + b


@pytest.mark.parametrize('a, b, expect', data_1)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数2数据为\n{}-{}'.format(a, b))
        assert add(a, b) == expect
#
# #
if __name__ == '__main__':
#     # pytest.main(['-s'])
# #     pytest.main('-s')
# #     pytest.main('-s','test_py1.py')
# #     pytest.main(['pytest.py -s test_py1.py'])
#     pytest.main(['-q','test_py1.py'])
    unittest.main(['-q','test_py1.py'])
