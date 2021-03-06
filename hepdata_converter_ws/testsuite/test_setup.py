# -*- encoding: utf-8 -*-
import os
import subprocess
import sys
from hepdata_converter.testsuite.test_writer import WriterTestSuite

__author__ = 'Michał Szostak'

import unittest


class SetupTestCase(WriterTestSuite):
    def test_setup(self):
        # Test installation in a temp directory
        r = subprocess.call([sys.executable, 'setup.py', 'install', '--root', self.current_tmp])
        self.assertEqual(r, 0)
