from LogicSymbol import Conditional, Conjunction, Biconditional, Disjunction, Not, Expr, Atomic


class GenericAtomic(Atomic):
    def __init__(self, name: str):
        Atomic.__init__(self, True)
        self.name = name

    def setValue(self, val: bool) -> None:
        self.phi = val

    def __str__(self):
        return self.name


def truth_permutation(n: int) -> list[list[bool]]:
    if n == 1:
        return [[True], [False]]
    a = 2 ** n
    a //= 2
    lst = []
    prev = truth_permutation(n - 1)
    for i in range(a):
        temp = [True]
        temp.extend(prev[i])
        lst.append(temp)

    for i in range(a, a + a):
        temp = [False]
        temp.extend(prev[i - a])
        lst.append(temp)

    return lst


def truth_table(expr: Expr, lst: list[GenericAtomic]) -> None:
    perms = truth_permutation(len(lst))
    for a in lst:
        print(a.__str__() + '\t', end='')
    print(expr, end='')

    for i in range(len(perms)):
        print('\n')
        for x in range(len(lst)):
            lst[x].setValue(perms[i][x])

            # Formatting looks nicer
            if perms[i][x]:
                s = 'T'
            else:
                s = 'F'
            print(s + '\t', end='')

        if expr.evaluate():
            s = 'T'
        else:
            s = 'F'
        print('|' + s)


def is_contradiction(expr: Expr, lst: list[GenericAtomic]) -> bool:
    perms = truth_permutation(len(lst))

    for i in range(len(perms)):
        for x in range(len(lst)):
            lst[x].setValue(perms[i][x])

        if expr.evaluate():
            return False
    return True


def is_tautology(expr: Expr, lst: list[GenericAtomic]) -> bool:
    perms = truth_permutation(len(lst))

    for i in range(len(perms)):
        for x in range(len(lst)):
            lst[x].setValue(perms[i][x])

        if not expr.evaluate():
            return False
    return True


if __name__ == '__main__':

    P = GenericAtomic('P')
    Q = GenericAtomic('Q')
    R = GenericAtomic('R')
    atomics = [P, Q, R]
    s = Conditional(Biconditional(P, Not(Q)), Disjunction(R, Conjunction(Q, R)))
    truth_table(s, atomics)


