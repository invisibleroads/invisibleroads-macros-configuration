from invisibleroads_macros_configuration import (
    load_attribute,
    load_attributes,
    load_json,
    SECRET_LENGTH)
from os.path import join
from types import FunctionType

from conftest import EXAMPLES_FOLDER


ATTRIBUTE_SPEC_TEXT = '''\
invisibleroads_macros_configuration.constants.SECRET_LENGTH
invisibleroads_macros_configuration.formats.load_attributes
invisibleroads_macros_configuration.formats.load_attribute
'''


def test_load_attributes():
    attributes = load_attributes(ATTRIBUTE_SPEC_TEXT)
    assert attributes[0] == SECRET_LENGTH
    assert isinstance(attributes[1], FunctionType)
    assert isinstance(attributes[2], FunctionType)


def test_load_attribute():
    attribute = load_attribute(
        'invisibleroads_macros_configuration.constants.SECRET_LENGTH')
    assert attribute == SECRET_LENGTH


def test_load_json():
    d = load_json(join(EXAMPLES_FOLDER, 'example.json'))
    assert d['text'] == 'whee'
