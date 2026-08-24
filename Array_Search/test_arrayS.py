import pytest
from arrayS import find_target

def test_target_found():
    assert find_target([2,1,4,5,1], 3) == [0, 1]
    assert find_target([2,2,4,5,1], 5) == [2, 4]

def test_target_not_found():
    assert find_target([2,1,4,5,1], 8) == 'Target not found'
    assert find_target([2,1,4,5,1], 20) == 'Target not found'

def test_error():
    with pytest.raises(TypeError):
        find_target(['dog','cat',4,], 9) #Although this cannot be as my main() function reprompts the user and raises ValueError.
