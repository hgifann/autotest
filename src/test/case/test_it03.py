# import pytest
#
# @pytest.fixture
# def make_customer_record():
#     def _make_customer_record(name):
#         return {"name": name, "orders": []}
#     return _make_customer_record
#
#     # print(_make_customer_record)
#
#
# def test_customer_records(make_customer_record):
#     customer_1 = make_customer_record("Lisa")
#     customer_2 = make_customer_record("Mike")
#     customer_3 = make_customer_record("Meredith")
#     print(customer_1,customer_2,customer_3)
#     assert customer_3==1


import src.utils.testjson1
import src.test.common.register
import json
import pytest
import pytest



# lista=[0,1,2,3,4,5]
excelinfo= src.utils.testjson1.Read_excel().read_excel()

@pytest.fixture(params=excelinfo)
def test_data(request):
    # s=()
    s=(request.param)
    return s

def test_not_2(test_data):
    print('test_data: %s' % test_data)
    ss=test_data[0]+"hello"
    print("ss====",ss)
    assert ss != 2