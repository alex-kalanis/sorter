<?php

namespace Sorter;

use Traversable;


/**
 * Class Sorter
 * Simple sorter for determine order of result
 * No sorting inside allowed - the order IS important
 */
class Sorter implements ISorter
{
    /** @var ISortColumn[] */
    protected $columns = [];

    public function getColumns(): Traversable
    {
        foreach ($this->columns as $column) {
            yield $column;
        }
    }

    public function add(ISortColumn $column): ISorter
    {
        $this->columns[] = $column;
        return $this;
    }

    public function remove(string $columnKey): ISorter
    {
        foreach ($this->columns as $index => $column) {
            if ($column->getKey() == $columnKey) {
                unset($this->columns[$index]);
            }
        }
        return $this;
    }

    public function clear(): ISorter
    {
        $this->columns = [];
        return $this;
    }
}