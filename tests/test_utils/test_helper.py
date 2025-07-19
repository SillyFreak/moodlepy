import attr
from datetime import datetime

from moodle.utils.helper import to_dict

class TestHelper:
    def test_to_dict(self):
        # empty dict
        result = to_dict(dict())
        assert result == {}

        # dict with simple values
        result = to_dict(dict(a=1, b=2))
        assert result == { 'a': 1, 'b': 2 }

        # dict with lists
        result = to_dict(dict(a=[1], b=[2, 3]))
        assert result == { 'a[0]': 1, 'b[0]': 2, 'b[1]': 3 }

        # dict with lists of dicts
        result = to_dict(dict(a=[dict(x=1), dict(x=2)], b=[dict(y=2, z=3)]))
        assert result == { 'a[0][x]': 1, 'a[1][x]': 2, 'b[0][y]': 2, 'b[0][z]': 3 }

        # dict with nested dicts
        # result = to_dict(dict(a=dict(x=1, y=2), b=dict(z=3)))
        # assert result == { 'a[x]': 1, 'a[y]': 2, 'b[z]': 3 }

        # dict with lists of lists
        # result = to_dict(dict(a=[[1, 2], [3, 4]], b=[[5], [6, 7]]))
        # assert result == {
        #     'a[0][0]': 1, 'a[0][1]': 2, 'a[1][0]': 3, 'a[1][1]': 4,
        #     'b[0][0]': 5, 'b[1][0]': 6, 'b[1][1]': 7,
        # }

        # dict with list of nested dicts
        # result = to_dict(dict(a=[dict(x=1, nested=dict(y=2))]))
        # assert result == { 'a[0][x]': 1, 'a[0][nested][y]': 2 }

        @attr.s
        class MyAttrClass:
            x = attr.ib()
            y = attr.ib()

        # attr class
        result = to_dict(MyAttrClass(x=1, y=2))
        assert result == { 'x': 1, 'y': 2 }

        # dict with attr class
        # result = to_dict(dict(a=MyAttrClass(x=1, y=2)))
        # assert result == { 'a[x]': 1, 'a[y]': 2 }

        # dict with datetime
        # result = to_dict(dict(a=datetime(2025, 1, 1)))
        # assert result == { 'a': datetime(2025, 1, 1).timestamp() }

        # dict with list of datetimes
        result = to_dict(dict(a=[datetime(2025, 1, 1)]))
        assert result == { 'a[0]': datetime(2025, 1, 1).timestamp() }

    def test_fromtimestamp(self):
        pass
