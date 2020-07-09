""" check the export list to ensure only the public API is exported by pgpy2.__init__
"""
import pytest

import importlib
import inspect


modules = ['pgpy2.constants',
           'pgpy2.decorators',
           'pgpy2.errors',
           'pgpy2.pgp',
           'pgpy2.symenc',
           'pgpy2.types',
           'pgpy2.packet.fields',
           'pgpy2.packet.packets',
           'pgpy2.packet.types',
           'pgpy2.packet.subpackets.signature',
           'pgpy2.packet.subpackets.types',
           'pgpy2.packet.subpackets.userattribute']


def get_module_objs(module):
    # return a set of strings that represent the names of objects defined in that module
    return { n for n, o in inspect.getmembers(module, lambda m: inspect.getmodule(m) is module) } | ({'FlagEnum',} if module is importlib.import_module('pgpy2.types') else set())  # dirty workaround until six fixes metaclass stuff to support EnumMeta in Python >= 3.6


def get_module_all(module):
    return set(getattr(module, '__all__', set()))


def test_pgpy_all():
    import pgpy2
    # just check that everything in pgpy2.__all__ is actually there
    assert set(pgpy2.__all__) <= { n for n, _ in inspect.getmembers(pgpy2) }


@pytest.mark.parametrize('modname', modules)
def test_exports(modname):
    module = importlib.import_module(modname)

    assert get_module_all(module) == get_module_objs(module)
