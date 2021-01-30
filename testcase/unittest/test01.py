import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('-----------setUp-----------')

    def test01(self):
        print('test01')
        self.assertEqual(1, 2)

    def test02(self):
        print('test02')
        self.assertGreaterEqual(2, 4)

    def tearDown(self) -> None:
        print('------------tearDown------------')

if __name__ == '__main__':
    unittest.main()
