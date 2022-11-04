def test(x):
    print('test 2')
    return x + 1

def test_answer():
    print('test 2')
    assert test(4) == 5
