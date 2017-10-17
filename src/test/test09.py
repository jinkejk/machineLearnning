import unittest

class test(unittest.TestCase):

    def setUp(self):
        print("before...")

    def tearDown(self):
        print("after....")

    def test_init(self):
        print('init02...')
        d = {"jinke":12}
        self.assertEqual(d["jinke"], 12)

    def test_init2(self):
        print('init01.....')
        d = {"jinke":12}
        with self.assertRaises(KeyError):
            d["dsad"]

