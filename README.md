# Run test package.

## Install

    $ pip install python-testpkg

## Write test package and run

    mytests/
        __init__.py # setUpPackage() / tearDownPackage()
        test_a.py
        test_b.py

    $ testpkg mytests [test filters]

The filter is case-insensitive and supports fuzzy matching. For example, filter `di`
will match 'test_db_index'.
