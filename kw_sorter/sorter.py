

class ISortEntry:
    """
     * Basic necessity to sort anything
    """

    DIRECTION_ASC = 'ASC'
    DIRECTION_DESC = 'DESC'

    def get_key(self) -> str:
        """
         * Sort by which key
        """
        raise NotImplementedError('TBA')

    def get_direction(self) -> str:
        """
         * Sorting direction
         * Preferably use constants above
        """
        raise NotImplementedError('TBA')


class ISorter:
    """
     * Basic interface
     * Make your app dependant on this interface
    """

    def get_entries(self):
        """
         * Get entries in sorting
        """
        raise NotImplementedError('TBA')

    def add(self, entry: ISortEntry):
        """
         * Add single entry from input which will be used for sorting
        """
        raise NotImplementedError('TBA')

    def remove(self, entry_key: str):
        """
         * Remove all entries containing that key
        """
        raise NotImplementedError('TBA')

    def clear(self):
        """
         * Clear sorting entries, be ready for another set
        """
        raise NotImplementedError('TBA')


class SortByEntry(ISortEntry):
    """
     * Basic implementation of single entry for sorting
    """

    def __init__(self):
        self._key = ''
        self._direction = self.DIRECTION_ASC

    def set_key(self, key: str):
        self._key = key
        return self

    def get_key(self) -> str:
        return self._key

    def set_direction(self, direction: str):
        self._direction = direction if direction in [self.DIRECTION_ASC, self.DIRECTION_DESC] else self._direction
        return self

    def get_direction(self) -> str:
        return self._direction


class Sorter(ISorter):
    """
     * Simple sorter for determine order of result
     * No sorting inside allowed - the order IS important
    """

    def __init__(self):
        self._entries = []

    def get_entries(self):
        for entry in self._entries:
            yield entry

    def add(self, entry: ISortEntry):
        self._entries.append(entry)
        return self

    def remove(self, entry_key: str):
        another = []
        for entry in self._entries:
            if entry.get_key() != entry_key:
                another.append(entry)
        self._entries = another
        return self

    def clear(self):
        self._entries = []
        return self
