# -*- coding: utf-8 -*-
import uiautomator2 as u2
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.d = u2.connect()  # connect to device

    def tearDown(self):
        self.d.app_stop_all()

# if __name__ == '__main__':
#     unittest.main()
