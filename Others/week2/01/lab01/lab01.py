def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    i = 0
    rst = 1
    while i < k:
        rst = rst * n
        i+=1
        n = n-1
    return rst


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    dgt = 0
    rst = 0
    while y>0: 
        dgt = y%10
        y = y//10
        rst = rst+dgt
    return rst




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n>0:
        dgt1 = n%10
        n = n//10
        if dgt1 !=8:
            continue
        else:
            dgt2 = n%10
            if dgt2 == 8:
                return True
            else:
                continue
    return False