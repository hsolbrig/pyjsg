# Note on tests
This project was originally developed to support [ShExJSG](https://github.com/hsolbrig/ShExJSG).  As a result, different
images of the `ShExJSG.py` occur in multiple points in the test.  We haven't been able to keep the namespaces completely
separate and, as a result, running this test suite as one large package results in unexpected failures.

For the time being, each sub-directory (test_basics, test_issues, ...) needs to be run separately.