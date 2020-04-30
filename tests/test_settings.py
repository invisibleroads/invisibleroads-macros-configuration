from invisibleroads_macros_configuration import fill_environment_variables
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
