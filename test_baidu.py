# -*- coding: utf-8 -*-
#！/usr/bin/env python

import unittest
import requests

class testfirst(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.baidu.com"

    def test_status(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code,200)

if __name__=="__main__":
    unittest.main()