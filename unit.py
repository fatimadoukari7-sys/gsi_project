from academicelement import AcademicElement


class Unit(AcademicElement):
    """A teaching unit (UE) containing several modules."""

    def __init__(self, name, title, modules=None):
        super().__init__(name, title)
        self._modules = list(modules) if modules else []   # avoid mutable default

    @property
    def modules(self):
        return tuple(self._modules)

    def add_module(self, module):
        self._modules.append(module)

    # Aggregated attributes
    @property
    def coef(self):
        return sum(m.coef for m in self._modules)

    @property
    def credit(self):
        return sum(m.credit for m in self._modules)

    @property
    def total_hours(self):
        return sum(m.total_hours for m in self._modules)

    def calculate_average(self):
        if not self._modules:
            return 0
        total = sum(m.calculate_average() * m.coef for m in self._modules)
        return total / self.coef

    def calculate_credits(self):
        """If unit average >= 10 the whole unit is acquired (compensation)."""
        if not self._modules:
            return 0
        if self.calculate_average() >= self.PASS_MARK:
            return self.credit
        return sum(m.calculate_credits() for m in self._modules)