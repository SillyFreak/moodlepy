from attr import has
from datetime import datetime
from typing import TypeVar, Any

from moodle.attr import asdict as asdict_attr

T = TypeVar("T")


def to_dict(data: dict, name: str = "") -> dict:
    """Properly format query string for webservice request
    The passed object itself must be a dict, but the returned value will be
    flattened to a dict with keys like `name[key]` or `name[index][key]`.

    Args:
        data (dict): Query to be formated
        name (str, optional): The key of the data. Defaults to "".

    Returns:
        dict: Formated data
    """

    result = {}
    def inner(prefix: str, data: Any) -> dict:
        pairs = None
        if isinstance(data, list):
            pairs = enumerate(data)
        elif isinstance(data, dict):
            pairs = data.items()
        elif has(data):
            pairs = asdict_attr(data).items()

        if pairs is not None:
            for key, value in pairs:
                inner(f"{prefix}[{key}]", value)
        else:
            if isinstance(data, datetime):
                data = datetime.timestamp(data)
            result[prefix] = data

    for key, value in data.items():
        inner(key, value)

    return result


def fromtimestamp(d: str):
    if not isinstance(d, str):
        return d
    elif not d.isdigit():
        return d
    return datetime.fromtimestamp(float(d))
