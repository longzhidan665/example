import pytest

class Testcase():
    def test_01(self):
        print("用例一")



if __name__ == '__main__':
    pytest.main(['-s','class.py','--alluredir','./report/xml'])