def hash_f(s):
    if len(s) > 2:
        f_ = len(s) * 2 - 1
    else:
        f_ = len(s) * 3
    return f_


def hash_set(a: dict, x, y):
    key = hash_f(y)
    a[key] = x
    return a


def hash_get(a: dict, x, y):
    key = hash_f(y)
    if a[key] == x:
        j = a[key]
    else:
        j = 'mistake'
    return j


def hash_del(a: dict, y):
    key = hash_f(y)
    del a[key]
    return a


lst = dict()
m = input()
n = input()
print(hash_f(n))
print(hash_set(lst, m, n))
print(hash_get(lst, m, n))
print(hash_del(lst, n))
