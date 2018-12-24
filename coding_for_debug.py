try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    print('ValueError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# assert : python -O err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
# foo('0')

# logging
import logging
logging.basicConfig(level=logging.INFO)
s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


# 单元测试


# 文档测试
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()


