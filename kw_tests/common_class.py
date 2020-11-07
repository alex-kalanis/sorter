import unittest
from kw_sorter.sorter import SortColumn


class CommonTestClass(unittest.TestCase):

    def _mock_column_1(self) -> SortColumn:
        return SortColumn().set_key('foo')

    def _mock_column_2(self) -> SortColumn:
        return SortColumn().set_key('bar').set_direction(SortColumn.DIRECTION_ASC)

    def _mock_column_3(self) -> SortColumn:
        return SortColumn().set_key('baz').set_direction(SortColumn.DIRECTION_DESC)

    def _iterator_to_array(self, iter):
        cont = []
        for content in iter:
            cont.append(content)
        return cont