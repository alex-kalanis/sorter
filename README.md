Sorter Interfaces
================

[![Build Status](https://travis-ci.org/alex-kalanis/sorter.svg?branch=master)](https://travis-ci.org/alex-kalanis/sorter)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/alex-kalanis/sorter/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/alex-kalanis/sorter/?branch=master)
[![Latest Stable Version](https://poser.pugx.org/alex-kalanis/sorter/v/stable.svg?v=1)](https://packagist.org/packages/alex-kalanis/sorter)
[![Minimum PHP Version](https://img.shields.io/badge/php-%3E%3D%207.3-8892BF.svg)](https://php.net/)
[![Downloads](https://img.shields.io/packagist/dt/alex-kalanis/sorter.svg?v1)](https://packagist.org/packages/alex-kalanis/sorter)
[![License](https://poser.pugx.org/alex-kalanis/sorter/license.svg?v=1)](https://packagist.org/packages/alex-kalanis/sorter)
[![Code Coverage](https://scrutinizer-ci.com/g/alex-kalanis/sorter/badges/coverage.png?b=master&v=1)](https://scrutinizer-ci.com/g/alex-kalanis/sorter/?branch=master)

Contains simple interfaces for creating sorting compatible across the libraries.
It has been cut from running project and simplified for usage available for another
libraries.

This is the mixed package - contains sever-side implementation in Python and PHP.

# PHP Installation

```
{
    "require": {
        "alex-kalanis/sorter": "1.0"
    }
}
```

(Refer to [Composer Documentation](https://github.com/composer/composer/blob/master/doc/00-intro.md#introduction) if you are not
familiar with composer)


# PHP Usage

1.) Use your autoloader (if not already done via Composer autoloader)

2.) Connect the "kalanis\kw_sorter" into your app. When it came necessary
you can extends every library to comply your use-case; mainly your processing.

# Python Installation

into your "setup.py":

```
    install_requires=[
        'kw_sorter',
    ]
```

# Python Usage

1.) Connect the "kw_sorter\sorter" into your app. When it came necessary
you can extends every library to comply your use-case; mainly your processing.
