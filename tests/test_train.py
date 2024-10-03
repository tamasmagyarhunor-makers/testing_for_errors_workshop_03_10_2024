from lib.train import *
import pytest

def test_train_instantiates_with_no_colour():
    train = Train()

    actual = train.colour
    
    expected = ''

    assert actual == expected

def test_train_set_colour_can_set_the_colour_red():
    train = Train()
    train.set_colour('red')

    actual = train.colour
    
    expected = 'red'

    assert actual == expected

def test_train_set_colour_can_set_the_colour_blue():
    train = Train()
    train.set_colour('blue')

    actual = train.colour
    
    expected = 'blue'

    assert actual == expected

def test_set_colour_throws_error_when_not_string_passed_in():
    train = Train()
    with pytest.raises(Exception) as e:
        train.set_colour(1)

    actual = str(e.value)
    expected = '1 is not a String. Colour should be a string'

    assert actual == expected