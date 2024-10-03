from lib.train import *

def test_train_instantiates_with_no_colour():
    train = Train()

    actual = train.colour
    
    expected = ''

    assert actual == expected