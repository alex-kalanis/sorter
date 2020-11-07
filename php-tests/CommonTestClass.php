<?php

use Sorter\SortByEntry;


class CommonTestClass extends \PHPUnit\Framework\TestCase
{
    public function mockEntry1(): SortByEntry
    {
        return (new SortByEntry())->setKey('foo');
    }

    public function mockEntry2(): SortByEntry
    {
        return (new SortByEntry())->setKey('bar')->setDirection(SortByEntry::DIRECTION_ASC);
    }

    public function mockEntry3(): SortByEntry
    {
        return (new SortByEntry())->setKey('baz')->setDirection(SortByEntry::DIRECTION_DESC);
    }

}