

class ISortColumn:
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

    def get_columns(self):
        """
         * Get columns in sorting
        """
        raise NotImplementedError('TBA')

    def add(self, column: ISortColumn):
        """
         * Add single column from input which will be used for sorting
        """
        raise NotImplementedError('TBA')

    def remove(self, column_key: str):
        """
         * Remove all columns containing that key
        """
        raise NotImplementedError('TBA')

    def clear(self):
        """
         * Clear sorting columns, be ready for another set
        """
        raise NotImplementedError('TBA')


class SortColumn(ISortColumn):
    """
     * Basic implementation of single column for sorting
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
        self._columns = []

    def get_columns(self):
        for column in self._columns:
            yield column

    def add(self, column: ISortColumn):
        self._columns.append(column)
        return self

    def remove(self, column_key: str):
        another = []
        for column in self._columns:
            if column.get_key() != column_key:
                another.append(column)
        self._columns = another
        return self

    def clear(self):
        self._columns = []
        return self
