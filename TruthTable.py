class BoolExpr:
    def evaluate(self):
        raise NotImplementedError


class Atomic(BoolExpr):
    def evaluate(self):
        return True, False


class Bool(BoolExpr):
    def __init__(self, boolean: bool):
        self.boolean = boolean

    def evaluate(self):
        return self.boolean


class TruthTable(BoolExpr):
    def __init__(self, left: BoolExpr, right: BoolExpr, op: str, neg_left=False, neg_right=False):
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


