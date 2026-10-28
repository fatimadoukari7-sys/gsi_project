from abc import ABC, abstractmethod


class AcademicElement(ABC):
    """Abstract base class for academic entities (Module, Unit, Semester)."""

    PASS_MARK = 10

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self._WEEKS = 15          # "private" attribute
        self._coef = 0
        self._credit = 0
        self.hours_lecture = 0
        self.hours_td = 0
        self.hours_tp = 0

    # coef / credit as properties so that Unit and Semester can compute them
    @property
    def coef(self):
        return self._coef

    @coef.setter
    def coef(self, value):
        self._coef = value

    @property
    def credit(self):
        return self._credit

    @credit.setter
    def credit(self, value):
        self._credit = value

    @property
    def total_hours(self):
        return self._WEEKS * (self.hours_lecture + self.hours_td + self.hours_tp)

    @abstractmethod
    def calculate_average(self):
        """Must be implemented by subclasses."""

    @abstractmethod
    def calculate_credits(self):
        """Must be implemented by subclasses."""

    def __str__(self):
        return f"{self.name} - {self.title}"