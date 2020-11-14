
from .interfaces import ISortEntry, ISorter


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
        yield from self._entries

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

    def get_default_item(self) -> ISortEntry:
        return SortByEntry()
