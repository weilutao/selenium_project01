
import pytest
import csv

def get_data():
    with open('test.csv') as file:
        list = csv.reader(file)
        my_data = []
        for row in list:
            my_data.extend(row)
        return my_data

@pytest.mark.parametrize('name',get_data())
def test01(name):
    print(name)



if __name__ == '__main__':
    pytest.main(['-sv','test_csv.py'])
