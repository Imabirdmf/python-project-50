# gendiff/formatters/__init__.py
from gendiff.formatters.stylish import format as stylish

FORMATTERS = {
    'stylish': stylish
}

DEFAULT_FORMAT = 'stylish'


def get_formatter(name: str | None):
    if name is None:
        name = DEFAULT_FORMAT

    if name not in FORMATTERS:
        raise ValueError(f'Unknown format: {name}')

    return FORMATTERS[name]
