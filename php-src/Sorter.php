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
    /** @var ISortEntry[] */
    protected $entries = [];

    public function getEntries(): Traversable
    {
        yield from $this->entries;
    }

    public function add(ISortEntry $entry): ISorter
    {
        $this->entries[] = $entry;
        return $this;
    }

    public function remove(string $entryKey): ISorter
    {
        foreach ($this->entries as $index => $entry) {
            if ($entry->getKey() == $entryKey) {
                unset($this->entries[$index]);
            }
        }
        return $this;
    }

    public function clear(): ISorter
    {
        $this->entries = [];
        return $this;
    }

    public function getDefaultItem(): ISortEntry
    {
        return new SortByEntry();
    }
}