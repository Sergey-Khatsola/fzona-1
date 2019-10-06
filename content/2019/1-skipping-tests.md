Title: Skipping tests depending on the Python version
Date: 2019-02-21 20:00
Author: Sergey Khatsiola
Category: BLOG
Tags: python, test
Slug: skipping-tests-depending-python-version
Status: published

SDFSDFSDFASDFASDFASDF ASDF ASDF ASDF


This library, combined with the **skipIf** method of [unittest library](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)
can be used to easily skip tests when using Python 3:

    :::python
    import six
    import unittest


    class MyTestCase(unittest.TestCase):


        @unittest.skipIf(six.PY3, "not compatible with Python 3")
        def test_example(self):
            # This test won't run under Python 3
            pass

## Credits

Thanks to my colleague **[Nicola](https://github.com/valnico)** for giving me the inspiration to write this post.
