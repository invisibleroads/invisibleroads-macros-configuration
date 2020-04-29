import json
from invisibleroads_macros_log import get_log
from os.path import expandvars


L = get_log(__name__)


def expand_environment_variables(settings):
    return {
        k: expandvars(v) if isinstance(v, str) else v
        for k, v in settings.items()}


def set_default(settings, key, default, parse=None):
    value = settings.get(key, default)
    if key not in settings:
        L.warning(f'using default {key} = {value}')
    elif value in ('', None):
        L.warning(f'missing {key}')
    elif parse:
        value = parse(value)
    settings[key] = value
    return value


def load_json(path):
    return json.load(open(path, 'rt'))
