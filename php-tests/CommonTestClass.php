<?php

use Sorter\SortColumn;


class CommonTestClass extends \PHPUnit\Framework\TestCase
{
    public function mockColumn1(): SortColumn
    {
        return (new SortColumn())->setKey('foo');
    }

    public function mockColumn2(): SortColumn
    {
        return (new SortColumn())->setKey('bar')->setDirection(SortColumn::DIRECTION_ASC);
    }

    public function mockColumn3(): SortColumn
    {
        return (new SortColumn())->setKey('baz')->setDirection(SortColumn::DIRECTION_DESC);
    }

}