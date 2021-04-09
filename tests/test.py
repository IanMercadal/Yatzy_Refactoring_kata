from src.yatzy_refactorizado import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance():
        assert 5 ==  Yatzy.chance(1,1,1,1,1) 
        assert 15 == Yatzy.chance(2,3,4,5,1)
        assert 16 == Yatzy.chance(3,3,4,5,1)
