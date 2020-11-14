<?php

namespace BasicTests;

use CommonTestClass;
use Sorter\Interfaces\ISortEntry;
use Sorter\SortByEntry;
use Sorter\Sorter;


class BasicTest extends CommonTestClass
{

    public function testEntry(): void
    {
        $entry = new SortByEntry();
        $this->assertEmpty($entry->getKey());
        $this->assertEquals(ISortEntry::DIRECTION_ASC, $entry->getDirection());

        $entry->setKey('any');
        $this->assertEquals('any', $entry->getKey());
        $this->assertEquals(ISortEntry::DIRECTION_ASC, $entry->getDirection());

        $entry->setDirection(ISortEntry::DIRECTION_DESC);
        $this->assertEquals(ISortEntry::DIRECTION_DESC, $entry->getDirection());

        $entry->setDirection('bad');
        $this->assertEquals(ISortEntry::DIRECTION_DESC, $entry->getDirection());
    }

    public function testSorterBasic(): void
    {
        $sorter = new Sorter();
        $this->assertEmpty(iterator_to_array($sorter->getEntries()));

        $this->assertInstanceOf('\Sorter\SortByEntry', $sorter->getDefaultItem());

        $sorter->add($this->mockEntry1());
        $sorter->add($this->mockEntry2());
        $sorter->add($this->mockEntry3());

        $this->assertNotEmpty(iterator_to_array($sorter->getEntries()));

        $sorter->clear();
        $this->assertEmpty(iterator_to_array($sorter->getEntries()));
    }

    public function testSorterRemoval(): void
    {
        $sorter = new Sorter();

        $sorter->add($this->mockEntry1());
        $sorter->add($this->mockEntry3());
        $sorter->add($this->mockEntry3()); // intentional

        $this->assertEquals(3, count(iterator_to_array($sorter->getEntries())));

        $sorter->remove($this->mockEntry3()->getKey());
        $this->assertEquals(1, count(iterator_to_array($sorter->getEntries())));

        $sorter->clear();
        $this->assertEmpty(iterator_to_array($sorter->getEntries()));
    }

    public function testSorterOrder(): void
    {
        $sorter = new Sorter();

        $sorter->add($this->mockEntry1());
        $sorter->add($this->mockEntry3());
        $sorter->add($this->mockEntry2());

        $result = iterator_to_array($sorter->getEntries());
        $this->assertEquals($this->mockEntry1()->getKey(), $result[0]->getKey());
        $this->assertEquals($this->mockEntry3()->getKey(), $result[1]->getKey());
        $this->assertEquals($this->mockEntry2()->getKey(), $result[2]->getKey());
    }
}
