
from itertools import combinations_with_replacement


def get_combinations_with_r(s, n):
    return sorted([''.join(sorted(x)) for x in combinations_with_replacement(s, n)])

    
def test_get_combinations_with_r():
    assert get_combinations_with_r('cat', 2) == ['aa', 'ac', 'at', 'cc', 'ct', 'tt']
    assert get_combinations_with_r('dog', 3) == ['ddd', 'ddg', 'ddo', 'dgg', 'dgo', 
                                                 'doo', 'ggg', 'ggo', 'goo', 'ooo']
    assert get_combinations_with_r('dog', 8) == ['dddddddd', 'dddddddg', 'dddddddo', 'ddddddgg',
                                                 'ddddddgo', 'ddddddoo', 'dddddggg', 'dddddggo',
                                                 'dddddgoo', 'dddddooo', 'ddddgggg', 'ddddgggo',
                                                 'ddddggoo', 'ddddgooo', 'ddddoooo', 'dddggggg',
                                                 'dddggggo', 'dddgggoo', 'dddggooo', 'dddgoooo',
                                                 'dddooooo', 'ddgggggg', 'ddgggggo', 'ddggggoo',
                                                 'ddgggooo', 'ddggoooo', 'ddgooooo', 'ddoooooo',
                                                 'dggggggg', 'dggggggo', 'dgggggoo', 'dggggooo',
                                                 'dgggoooo', 'dggooooo', 'dgoooooo', 'dooooooo',
                                                 'gggggggg', 'gggggggo', 'ggggggoo', 'gggggooo',
                                                 'ggggoooo', 'gggooooo', 'ggoooooo', 'gooooooo',
                                                 'oooooooo']
