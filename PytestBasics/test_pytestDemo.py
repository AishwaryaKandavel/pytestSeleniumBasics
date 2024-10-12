#Any pytest file should start with test so that it can execute it
#pytest method should start with test
#Any code should be wrapped in a method
#to execute in CLI - cd <path_of_the_tests>, py.test - to execute, -v to get more info
#-s to get console output - print statements = py.test -v -s (all tests in the given path)
#to add file name = py.test test_assertions.py -v -s
# -k for regex = py.test -k 2 -v -s
# - m to run tests based on tags - mark = py.test -m smoke -v -s
#To skip test add predefined mark to function - @pytest.mark.skip
#Execute but do not fail - @pytest.mark.xfail

import pytest

@pytest.mark.smoke
def test_firstprogram1():
    print('Hello1')

def test_firstprogram2():
    print('Hello2')