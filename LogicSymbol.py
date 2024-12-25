class Expr:
    def evaluate(self) -> bool:
        raise NotImplementedError
    
    def __str__(self) -> str:
        raise NotImplementedError


class Atomic(Expr):
    def __init__(self, phi: bool) -> None:
        self.phi = phi
        
    def evaluate(self) -> bool:
        return self.phi
    
    def __str__(self) -> str:
        return str(self.phi)


class Conditional(Expr):
    def __init__(self, antecedent: Expr, consequent: Expr) -> None:
        self.antecedent = antecedent
        self.consequent = consequent

    def evaluate(self) -> bool:
        return not self.antecedent.evaluate() or self.consequent.evaluate()
    
    def __str__(self):
        return f'({self.antecedent} => {self.consequent})'


class Conjunction(Expr):
    def __init__(self, phi: Expr, psi: Expr) -> None:
        self.phi = phi
        self.psi = psi
    
    def evaluate(self) -> bool:
        return self.phi.evaluate() and self.psi.evaluate()
    
    def __str__(self) -> str:
        return f'({self.phi} ∧ {self.psi})'


class Disjunction(Expr):
    def __init__(self, phi: Expr, psi: Expr) -> None:
        self.phi = phi
        self.psi = psi

    def evaluate(self) -> bool:
        return self.phi.evaluate() or self.psi.evaluate()

    def __str__(self) -> str:
        return f'({self.phi} ∨ {self.psi})'


class Biconditional(Expr):
    def __init__(self, phi: Expr, psi: Expr) -> None:
        self.phi = phi
        self.psi = psi

    def evaluate(self) -> bool:
        return (self.phi.evaluate() and self.psi.evaluate()) or (not self.phi.evaluate() and not self.psi.evaluate())

    def __str__(self) -> str:
        return f'({self.phi} <=> {self.psi})'


class Not(Expr):
    def __init__(self, phi: Expr) -> None:
        self.phi = phi

    def evaluate(self) -> bool:
        return not self.phi.evaluate()

    def __str__(self) -> str:
        return f'~{self.phi}'


if __name__ == '__main__':
    A = Atomic(True)
    B = Atomic(True)
    print(Biconditional(Conditional(A, B), Conjunction(Not(A), Disjunction(A, B))).evaluate())


