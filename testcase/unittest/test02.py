# testsuite测试套件演示
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')


if __name__ == '__main__':
    # 构造测试套件
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_02'))
    suite.addTest(MyTestCase('Test_01'))
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
