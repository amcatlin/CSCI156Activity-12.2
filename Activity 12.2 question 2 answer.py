__author__ = 'Alicia'

def mean(*args):
    diff = len(args)
    if diff > 0:
        s = 0
        for i in args:
            s += i
        return s/len(args)
    else:
        return None

print(mean())
print(mean(6, 9, 7, 21, 1, 0))
print(mean(100, 8, 2, 50, 99, 25, 6, 99))