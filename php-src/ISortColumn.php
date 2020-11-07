<?php

namespace Sorter;


/**
 * Interface ISortColumn
 * @package Sorter
 * Basic necessity to sort anything
 */
interface ISortColumn
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
