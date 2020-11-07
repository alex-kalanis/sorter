<?php

namespace Sorter;


/**
 * Class SortColumn
 * @package Sorter
 * Basic implementation of single column for sorting
 */
class SortColumn implements ISortColumn
{
    protected $key = '';
    protected $direction = self::DIRECTION_ASC;

    public function setKey(string $key): self
    {
        $this->key = $key;
        return $this;
    }

    public function getKey(): string
    {
        return $this->key;
    }

    public function setDirection(string $direction): self
    {
        $this->direction = in_array($direction, [static::DIRECTION_ASC, static::DIRECTION_DESC]) ? $direction : $this->direction;
        return $this;
    }

    public function getDirection(): string
    {
        return $this->direction;
    }
}
