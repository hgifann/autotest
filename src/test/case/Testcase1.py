import pytest
 
class Test_case001:
    def test_001(self):
        x="hello"
        assert "h" in x
    def test_002(self):
        x="this"
        assert hasattr(x,"check")
    def test_003(self):
        a=10
        assert a<20
if __name__ == "__main__":
  pytest.main(["-q","Testcase1.py"])