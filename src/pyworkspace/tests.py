# -*- coding: utf-8 -*-
import os
import unittest
import tempfile
import shutil
import pyworkspace


exists = os.path.exists
join_path = os.path.join


class TestPyWorkspace(unittest.TestCase):

    def assertDirIsPackage(self, rel_path):
        abs_path = join_path(self.test_root, *rel_path)
        assert exists(join_path(abs_path)), "Package directory (%s) does not exist" % abs_path
        assert exists(join_path(abs_path, "__init__.py")), "Directory (%s) does not contain __init__.py and hence is not a package" % abs_path

    def setUp(self):
        self.test_root = tempfile.mkdtemp()
        self.pyworkspace = pyworkspace.PyWorkspace(self.test_root)

    def test_create_package(self):
        self.pyworkspace.create_package("mypkg")
        self.assertDirIsPackage(['mypkg'])

        self.pyworkspace.create_package("mypkg.subpkg1.subpkg2")
        self.assertDirIsPackage(['mypkg', 'subpkg1'])
        self.assertDirIsPackage(['mypkg', 'subpkg1', 'subpkg2'])

    def tearDown(self):
        shutil.rmtree(self.test_root)
