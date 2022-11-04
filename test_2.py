def inc(x):
    print('2nd test')
    return x + 1

def test_answer():
    print('2nd test')
    assert inc(4) == 5
