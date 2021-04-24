import pytest
import xlrd

def get_data():
    filename = "data.xlsx"
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0) #第几个分页
    rows = sheet.nrows
    cols = sheet.ncols
    list = []

    for row in range(rows):
        for col in range(cols):
            cell_data = sheet.cell_value(row, col)
            list.append(cell_data)

    return list

@pytest.mark.parametrize("name", get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    pytest.main(['-sv',"test_excel.py"])

