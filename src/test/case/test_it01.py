__author__ = 'THTF'
import pytest
# s=[(1,2),(3,4)]

# @pytest.mark.parametrize("s1,s2",s)
# @pytest.mark.parametrize("s1,s2",s)
# @pytest.fixture(scope="module")
#
#
# class test_it01:
#     # s1=1
#     # s2=3
#     # print(s1,s2)
#     @pytest.fixture
#     def test_01(self,s1=1,s2=2):
#         f1=s1+s2
#         f2=s1*s2
#         print(f1)
#         assert f1==3
#         return f1,f2
#
#     def test_02(self,test_01):
#         for x in test_01:
#             print(x)
#             assert x==1

@pytest.fixture
def test_01(s1=1,s2=2):
    f1=s1+s2
    f2=s1*s2
    print(f1)
    assert f1==3
    def www(f1):
        f4=f1+1
        print("x====")
        return f4
    return f1,f2,www(f1)

def test_02(test_01):
    # for x in test_01:
    #     print(x)
    #     s=test_01().www()
    #     print(s)
        print(test_01)
        assert test_01[0]==1

