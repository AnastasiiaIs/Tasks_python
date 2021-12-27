 g_a=[]

def hash_f(s):
    if len(s) > 2:
        f_ = len(s) * 2 - 1
    else:
        f_ = len(s) * 3
    return f_


def hash_set(x, y,a=None):
    if a is None:
        a=a_g
    key = hash_f(y)
    a[key]=x
    return a


def hash_get(x, y,a=None):
    if a is None:
        a=g_a
    key = hash_f(y)
    if a[key] == x:
        j = a[key]
    else:
        j = 'mistake'
    return j


def hash_del(y, a=None):
    if a is None:
        a=g_a
    key = hash_f(y)
    del a[key]
    return a

def hash_coef(a:list):
    c=0
    co=0
    for i in a:
        if a[i]!=0:
            c=c+1
    co=(c/len(a))
    return(co)
     

l=None
m = input()
n = input()
print(hash_f(n))
print(hash_set(m, n,l))
print(hash_get(m, n,l))
print(hash_del(n,l))
print(hash_coef(l))