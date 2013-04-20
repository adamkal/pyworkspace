# -*- coding: utf-8 -*-
import os
import re


class ValidationError(Exception):
    pass


class PyWorkspace(object):

    def __init__(self, root=None):
        self.root = root or "."

    def create_package(self, name):
        """ Creates a python package """

        name = name.split('.')

        package = os.path.join(self.root, *name)
        os.makedirs(package)

        for i in xrange(len(name)):
            sub_pkg = name[:i + 1]
            init_path = [self.root] + sub_pkg + ['__init__.py']
            with open(os.path.join(*init_path), 'w') as f:
                pass

