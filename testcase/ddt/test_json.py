
import pytest
import json

def get_data():
    with open("test.json") as f:
        list = []
        data = json.load(f)
        list.extend(data["keys"])
        return list

#ddt测试
@pytest.mark.parametrize("name", get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    pytest.main(["-sv","test_json.py"])

