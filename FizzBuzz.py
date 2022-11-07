'''
Simple test case
'''

def inc(base_x):
    '''simple increment function'''
    print('2nd test!!')
    return base_x + 1

def test_answer():
    '''simple base function'''
    print('2nd test!!!!')
    assert inc(4) == 5
