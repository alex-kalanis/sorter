<?php

namespace Sorter;

use Traversable;


/**
 * Interface ISorter
 * @package Sorter
 * Basic interface
 * Make your app dependant on this interface
 */
interface ISorter
{
    /**
     * Get columns in sorting
     * @return Traversable ISortColumn
     */
    public function getColumns(): Traversable;

    /**
     * Add single column from input which will be used for sorting
     * @param ISortColumn $column
     * @return $this
     */
    public function add(ISortColumn $column): self;

    /**
     * Remove all columns containing that key
     * @param string $columnKey
     * @return $this
     */
    public function remove(string $columnKey): self;

    /**
     * Clear sorting columns, be ready for another set
     * @return $this
     */
    public function clear(): self;
}
