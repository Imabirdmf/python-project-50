from gendiff.formatters.json_f import format_json as json_f
from gendiff.formatters.plain import format_plain as plain
from gendiff.formatters.stylish import format_stylish as stylish

FORMATTERS = {"stylish": stylish, "plain": plain, "json": json_f}

DEFAULT_FORMAT = "stylish"


def get_formatter(name: str | None):
    if name is None:
        name = DEFAULT_FORMAT

    if name not in FORMATTERS:
        raise ValueError(f"Unknown format: {name}")

    return FORMATTERS[name]
