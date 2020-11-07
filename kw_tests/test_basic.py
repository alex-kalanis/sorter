from kw_sorter.sorter import Sorter, SortByEntry, ISortEntry
from kw_tests.common_class import CommonTestClass


class ItemTest(CommonTestClass):

    def test_entry(self):
        entry = SortByEntry()
        assert not entry.get_key()
        assert ISortEntry.DIRECTION_ASC == entry.get_direction()

        entry.set_key('any')
        assert 'any' == entry.get_key()
        assert ISortEntry.DIRECTION_ASC == entry.get_direction()

        entry.set_direction(ISortEntry.DIRECTION_DESC)
        assert ISortEntry.DIRECTION_DESC == entry.get_direction()

        entry.set_direction('bad')
        assert ISortEntry.DIRECTION_DESC == entry.get_direction()

    def test_sorter_basic(self):
        sorter = Sorter()
        assert 1 > len(self._iterator_to_array(sorter.get_entries()))

        sorter.add(self._mock_entry_1())
        sorter.add(self._mock_entry_2())
        sorter.add(self._mock_entry_3())

        assert 0 < len(self._iterator_to_array(sorter.get_entries()))

        sorter.clear()
        assert 1 > len(self._iterator_to_array(sorter.get_entries()))

    def test_sorter_removal(self):
        sorter = Sorter()

        sorter.add(self._mock_entry_1())
        sorter.add(self._mock_entry_3())
        sorter.add(self._mock_entry_3())  # intentional

        assert 3 == len(self._iterator_to_array(sorter.get_entries()))

        sorter.remove(self._mock_entry_3().get_key())
        assert 1 == len(self._iterator_to_array(sorter.get_entries()))

        sorter.clear()
        assert 1 > len(self._iterator_to_array(sorter.get_entries()))

    def test_sorter_order(self):
        sorter = Sorter()

        sorter.add(self._mock_entry_1())
        sorter.add(self._mock_entry_3())
        sorter.add(self._mock_entry_2())

        result = self._iterator_to_array(sorter.get_entries())
        assert self._mock_entry_1().get_key() == result[0].get_key()
        assert self._mock_entry_3().get_key() == result[1].get_key()
        assert self._mock_entry_2().get_key() == result[2].get_key()
