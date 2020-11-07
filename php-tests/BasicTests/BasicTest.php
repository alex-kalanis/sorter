<?php

namespace BasicTests;

use CommonTestClass;
use Sorter\Sorter;
use Sorter\SortColumn;
use Sorter\ISortColumn;


class BasicTest extends CommonTestClass
{

    public function testColumn(): void
    {
        $column = new SortColumn();
        $this->assertEmpty($column->getKey());
        $this->assertEquals(ISortColumn::DIRECTION_ASC, $column->getDirection());

        $column->setKey('any');
        $this->assertEquals('any', $column->getKey());
        $this->assertEquals(ISortColumn::DIRECTION_ASC, $column->getDirection());

        $column->setDirection(ISortColumn::DIRECTION_DESC);
        $this->assertEquals(ISortColumn::DIRECTION_DESC, $column->getDirection());

        $column->setDirection('bad');
        $this->assertEquals(ISortColumn::DIRECTION_DESC, $column->getDirection());
    }

    public function testSorterBasic(): void
    {
        $sorter = new Sorter();
        $this->assertEmpty(iterator_to_array($sorter->getColumns()));

        $sorter->add($this->mockColumn1());
        $sorter->add($this->mockColumn2());
        $sorter->add($this->mockColumn3());

        $this->assertNotEmpty(iterator_to_array($sorter->getColumns()));

        $sorter->clear();
        $this->assertEmpty(iterator_to_array($sorter->getColumns()));
    }

    public function testSorterRemoval(): void
    {
        $sorter = new Sorter();

        $sorter->add($this->mockColumn1());
        $sorter->add($this->mockColumn3());
        $sorter->add($this->mockColumn3()); // intentional

        $this->assertEquals(3, count(iterator_to_array($sorter->getColumns())));

        $sorter->remove($this->mockColumn3()->getKey());
        $this->assertEquals(1, count(iterator_to_array($sorter->getColumns())));

        $sorter->clear();
        $this->assertEmpty(iterator_to_array($sorter->getColumns()));
    }

    public function testSorterOrder(): void
    {
        $sorter = new Sorter();

        $sorter->add($this->mockColumn1());
        $sorter->add($this->mockColumn3());
        $sorter->add($this->mockColumn2());

        $result = iterator_to_array($sorter->getColumns());
        $this->assertEquals($this->mockColumn1()->getKey(), $result[0]->getKey());
        $this->assertEquals($this->mockColumn3()->getKey(), $result[1]->getKey());
        $this->assertEquals($this->mockColumn2()->getKey(), $result[2]->getKey());
    }
}
