#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import run_tests # set sys.path

import tempfile
import os

from kobo.decorators import *


class TestDecoratorsModule(unittest.TestCase):
    def setUp(self):
        self.tmp_file = tempfile.mktemp()

    def tearDown(self):
        os.remove(self.tmp_file)

    def test_log_traceback(self):
        @log_traceback(self.tmp_file)
        def foo_function():
            raise IOError("Some error")

        try:
            foo_function()
        except IOError:
            pass

        tb = open(self.tmp_file).read()
        self.assertTrue(tb.startswith("--- TRACEBACK BEGIN:"))


if __name__ == "__main__":
    unittest.main()