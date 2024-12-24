from LogicSymbol import Conditional, Conjunction, Biconditional, Disjunction, Not, Expr


class GenericAtomic(Expr):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class TruthTable(Expr):
    def __init__(self, left: Expr, right: Expr, op: str, neg_left=False, neg_right=False):
        self.left = left
        self.right = right
        self.op = op
        self.neg_left = neg_left
        self.neg_right = neg_right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.op.lower == 'and':
            self._and()
        elif self.op.lower == 'conditional':
            self._conditional()
        elif self.op.lower == 'biconditional':
            self._biconditional()
        elif self.op.lower == 'or':
            self._or()
        else:
            raise Exception

    def _conditional(self):
        pass

    def _and(self):
        pass

    def _or(self):
        pass

    def _biconditional(self):
        pass


def truth_permutation(n: int) -> list[list[str]]:
    if n == 1:
        return [['T'], ['F']]
    a = 2**n
    a //= 2
    lst = []
    for _ in range(a):
        lst.append(['T'])

    for _ in range(a):
        lst.append(['F'])
    prev = truth_permutation(n - 1)

    for i in range(a):
        lst[i].extend(prev[i])

    for i in range(a, len(lst)):
        lst[i].extend(prev[a - i])
    return lst


if __name__ == '__main__':
    for t in truth_permutation(3):
        print(t)

