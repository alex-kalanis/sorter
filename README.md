Sorter Interfaces
================

Contains simple interfaces for creating sorting compatible across the libraries.
It has been cut from running project and simplified for usage available for another
libraries.

This is the mixed package - contains sever-side implementation in Python and PHP.

# PHP Installation

```
{
    "require": {
        "alex-kalanis/sorter": "dev-master"
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
