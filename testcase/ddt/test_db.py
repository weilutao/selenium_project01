import MySQLdb
import pytest


conn = MySQLdb.connect(
    user = "",
    passwd = "",
    host = "",
    port = "",
    db = ""
)

def get_data():
    query_sql = ''  # select id,username,pwd from user_db
    list = []
    try:
        cursor = conn.cursor()
        cursor.execute(query_sql)
        read = cursor.fetchall()
        for x in read:
            u = (x[0], x[1], x[2])
            list.append(u)
        return list
    finally:
        cursor.close() # 关闭游标
        conn.close() # 关闭数据库

@pytest.mark.parametrize("id, name, pwd", get_data())
def test01(id, name, pwd):
    print(id, name, pwd)

if __name__ == '__main__':
    pytest.main(['-sv'])