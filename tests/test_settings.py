from invisibleroads_macros_configuration import (
    fill_environment_variables,
    fill_secrets,
    resolve_attribute,
    SECRET_LENGTH)
from os import environ


def test_fill_environment_variables():
    settings = {'x': '$INVISIBLEROADS_MACROS_CONFIGURATION_TEST_X'}

    assert 'INVISIBLEROADS_MACROS_CONFIGURATION_TEST_X' not in environ
    fill_environment_variables(settings)
    assert settings['x'] == '$INVISIBLEROADS_MACROS_CONFIGURATION_TEST_X'

    text = 'a'
    environ['INVISIBLEROADS_MACROS_CONFIGURATION_TEST_X'] = text
    fill_environment_variables(settings)
    assert settings['x'] == text


def test_fill_secrets():
    settings = {'a.secret': ''}
    fill_secrets(settings)
    assert len(settings['a.secret']) == SECRET_LENGTH


def test_resolve_attribute():
    x = resolve_attribute(
        'invisibleroads_macros_configuration.constants.SECRET_LENGTH')
    assert x == SECRET_LENGTH
