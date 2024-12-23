class Expr:
    def evaluate(self):
        raise NotImplementedError
    
    def __str__(self):
        raise NotImplementedError


class Op(Expr):
    def evaluate(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Atomic(Expr):
    def __init__(self, phi: bool):
        self.phi = phi
        
    def evaluate(self):
        return self.phi
    
    def __str__(self):
        return str(self.phi)


class Conditional(Op):
    def __init__(self, antecedent: Expr, consequent: Expr):
        self.antecedent = antecedent
        self.consequent = consequent

    def evaluate(self):
        return not self.antecedent.evaluate() or self.consequent.evaluate()
    
    def __str__(self):
        return f'({self.antecedent} => {self.consequent})'


class Conjunction(Op):
    def __init__(self, phi: Expr, psi: Expr):
        self.phi = phi
        self.psi = psi
    
    def evaluate(self):
        return self.phi.evaluate() and self.psi.evaluate()
    
    def __str__(self):
        return f'({self.phi} ∧ {self.psi})'


class Disjunction(Op):
    def __init__(self, phi: Expr, psi: Expr):
        self.phi = phi
        self.psi = psi

    def evaluate(self):
        return self.phi.evaluate() or self.psi.evaluate()

    def __str__(self):
        return f'({self.phi} ∨ {self.psi})'


class Biconditional(Op):
    def __init__(self, phi: Expr, psi: Expr):
        self.phi = phi
        self.psi = psi

    def evaluate(self):
        return (self.phi.evaluate() and self.psi.evaluate()) or (not self.phi.evaluate() and not self.psi.evaluate())

    def __str__(self):
        return f'({self.phi} <=> {self.psi})'


class Not(Op):
    def __init__(self, phi: Expr):
        self.phi = phi

    def evaluate(self):
        return not self.phi.evaluate()

    def __str__(self):
        return f'~{self.phi}'


if __name__ == '__main__':
    A = Atomic(True)
    B = Atomic(True)
    print(Biconditional(Conditional(A, B), Conjunction(Not(A), Disjunction(A, B))).evaluate())


