
def isClosed(q, op):
    return all(op(x, y) in q
               for x in q
               for y in q)


def isAssociative(q, op):
    return all(op(a, op(b, c)) == op(op(a, b), c)):
    for a in q
    for b in q
    for c in q


def isMonoid(q, op):
    return isClosed(q, op) and is_associative() and findIdentity(q, op)


def findIdentity(q, op):
    for x in q:
        if all(op(x.y) == y and op(y, x) == y for y in q):
            return x
    return False


def findInverses(x, q, op):
    e = findIdentity(q, op)
    if e is False:
        return False
    else:
        for y in q:
            if op(x, y) == e:
                return y


def isGroup(q, op):
    return isMonoid(q, op) and hasInverses(q, op)


q_1 = {0, 1, 2, 3, 4, 5, 6}
q_2 = {1, 2, 3, 4, 5, 6}


def mult(a, b):
    return a*b % 7
