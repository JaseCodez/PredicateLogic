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
    for _ in range(a):
        lst.append([True])

    for _ in range(a):
        lst.append([False])

    prev = truth_permutation(n - 1)

    for i in range(a):
        lst[i].extend(prev[i])

    for i in range(a, len(lst)):
        lst[i].extend(prev[i - a])
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


if __name__ == '__main__':
    P = GenericAtomic('P')
    Q = GenericAtomic('Q')
    R = GenericAtomic('R')
    S = GenericAtomic('S')
    atomics = [P, Q, R, S]
    truth_table(Conjunction(Conditional(P, Q), Disjunction(Not(S), R)), atomics)

