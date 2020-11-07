<?php

namespace Sorter;


/**
 * Interface ISortEntry
 * @package Sorter
 * Basic necessity to sort anything
 */
interface ISortEntry
{
    const DIRECTION_ASC = 'ASC';
    const DIRECTION_DESC = 'DESC';

    /**
     * Sort by which key
     * @return string
     */
    public function getKey(): string;

    /**
     * Sorting direction
     * Preferably use constants above
     * @return string
     */
    public function getDirection(): string;
}
