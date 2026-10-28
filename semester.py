from academicelement import AcademicElement


class Semester(AcademicElement):
    """A semester containing several units."""

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self._units = list(units) if units else []

    @property
    def units(self):
        return tuple(self._units)

    def add_unit(self, unit):
        self._units.append(unit)

    @property
    def coef(self):
        return sum(u.coef for u in self._units)

    @property
    def credit(self):
        return sum(u.credit for u in self._units)

    @property
    def total_hours(self):
        return sum(u.total_hours for u in self._units)

    def calculate_average(self):
        if not self._units:
            return 0
        total = sum(u.calculate_average() * u.coef for u in self._units)
        return total / self.coef

    def calculate_credits(self):
        """Semester average >= 10 => all 30 credits; else sum of unit credits."""
        if not self._units:
            return 0
        if self.calculate_average() >= self.PASS_MARK:
            return self.credit
        return sum(u.calculate_credits() for u in self._units)

    def report(self):
        lines = [f"=== {self.name} - {self.title} ==="]
        for u in self._units:
            lines.append(f"{u.name}: avg={u.calculate_average():.2f} "
                         f"credits={u.calculate_credits()}/{u.credit}")
            for m in u.modules:
                lines.append(f"   {m.name:6} {m.title[:40]:40} "
                             f"avg={m.calculate_average():5.2f} "
                             f"credits={m.calculate_credits()}/{m.credit}")
        lines.append(f"Semester average: {self.calculate_average():.2f}")
        lines.append(f"Semester credits: {self.calculate_credits()}/{self.credit}")
        return "\n".join(lines)