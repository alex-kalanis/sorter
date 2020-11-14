import unittest
from kw_sorter.sorter import SortByEntry


class CommonTestClass(unittest.TestCase):

    def _mock_entry_1(self) -> SortByEntry:
        return SortByEntry().set_key('foo')

    def _mock_entry_2(self) -> SortByEntry:
        return SortByEntry().set_key('bar').set_direction(SortByEntry.DIRECTION_ASC)

    def _mock_entry_3(self) -> SortByEntry:
        return SortByEntry().set_key('baz').set_direction(SortByEntry.DIRECTION_DESC)
