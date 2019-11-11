import unittest
import pytest
import sys
# class AlienTest(unittest.TestCase):
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
# if __name__ == '__main__':
#     print("hel")
#     # pytest.main(['q','test_py2.py'])
#     # pytest.main(['-q test_py1.py'])
#     pytest.main()
#
class Test_runs:
    def run_tests(self):
            """Customized run"""

            # deferred import
            import pytest

            # run pytest with empty array so pytest.ini takes complete control
            # need to use [] because of https://github.com/pytest-dev/pytest/issues/1110
            errno = pytest.main([])
            sys.exit(errno)
