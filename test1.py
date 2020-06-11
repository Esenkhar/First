try:
    try:
        print(1 / 0)
    except Exception as x:
        raise TypeError('Bad') from x
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
