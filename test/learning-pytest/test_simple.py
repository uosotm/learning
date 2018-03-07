# Take care the file name should have 'test_' prefix
# like 'test_simple'. Run the command
# in the same directory as the program file:
#
# $ pytest
#

def sum(x, y):
    return x + y

def test_answer():
    assert sum(0, 1) == 2
