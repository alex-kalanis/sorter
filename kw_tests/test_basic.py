from kw_sorter.sorter import Sorter, SortColumn, ISortColumn
from kw_tests.common_class import CommonTestClass


class ItemTest(CommonTestClass):

    def test_column(self):
        column = SortColumn()
        assert not column.get_key()
        assert ISortColumn.DIRECTION_ASC == column.get_direction()

        column.set_key('any')
        assert 'any' == column.get_key()
        assert ISortColumn.DIRECTION_ASC == column.get_direction()

        column.set_direction(ISortColumn.DIRECTION_DESC)
        assert ISortColumn.DIRECTION_DESC == column.get_direction()

        column.set_direction('bad')
        assert ISortColumn.DIRECTION_DESC == column.get_direction()

    def test_sorter_basic(self):
        sorter = Sorter()
        assert 1 > len(self._iterator_to_array(sorter.get_columns()))

        sorter.add(self._mock_column_1())
        sorter.add(self._mock_column_2())
        sorter.add(self._mock_column_3())

        assert 0 < len(self._iterator_to_array(sorter.get_columns()))

        sorter.clear()
        assert 1 > len(self._iterator_to_array(sorter.get_columns()))

    def test_sorter_removal(self):
        sorter = Sorter()

        sorter.add(self._mock_column_1())
        sorter.add(self._mock_column_3())
        sorter.add(self._mock_column_3())  # intentional

        assert 3 == len(self._iterator_to_array(sorter.get_columns()))

        sorter.remove(self._mock_column_3().get_key())
        assert 1 == len(self._iterator_to_array(sorter.get_columns()))

        sorter.clear()
        assert 1 > len(self._iterator_to_array(sorter.get_columns()))

    def test_sorter_order(self):
        sorter = Sorter()

        sorter.add(self._mock_column_1())
        sorter.add(self._mock_column_3())
        sorter.add(self._mock_column_2())

        result = self._iterator_to_array(sorter.get_columns())
        assert self._mock_column_1().get_key() == result[0].get_key()
        assert self._mock_column_3().get_key() == result[1].get_key()
        assert self._mock_column_2().get_key() == result[2].get_key()
