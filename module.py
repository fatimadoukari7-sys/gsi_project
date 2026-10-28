from academicelement import AcademicElement


class Module(AcademicElement):
    """A teaching module with pedagogical and evaluation attributes."""

    def __init__(self, name="", title="", coef=1, credit=1,
                 hours_lecture=1.5, hours_td=0, hours_tp=0,
                 teaching_mode="In-person",
                 continous_percent=40, exam_percent=60):
        super().__init__(name, title)
        if continous_percent + exam_percent != 100:
            raise ValueError("continous_percent + exam_percent must equal 100")
        self.coef = coef
        self.credit = credit
        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp
        self.teaching_mode = teaching_mode          # "Distance" or "In-person"
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent
        self._grades = {"tp": None, "td": None, "exam": None}

    # ---- Encapsulation: controlled access to grades ----
    def set_grade(self, tp=None, td=None, exam=None):
        for key, value in (("tp", tp), ("td", td), ("exam", exam)):
            if value is not None:
                if not 0 <= value <= 20:
                    raise ValueError(f"{key} grade must be between 0 and 20")
                self._grades[key] = value

    def get_grades(self):
        return dict(self._grades)   # copy: the original stays protected

    def summary(self):
        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}, Credits: {self.credit}\n"
            f"Hours: total {self.total_hours}, {self.hours_lecture} Lecture, "
            f"{self.hours_td} TD, {self.hours_tp} TP\n"
            f"Teaching mode: {self.teaching_mode}, "
            f"Evaluation: Continous {self.evaluation_continous_percent}% "
            f"Exam {self.evaluation_exam_percent}%"
        )

    # ---- Calculations ----
    def _percents(self):
        """Split the continuous percentage between TP and TD."""
        cont = self.evaluation_continous_percent
        if self.hours_tp and self.hours_td:
            return cont / 2, cont / 2
        if self.hours_td:
            return 0, cont
        if self.hours_tp:
            return cont, 0
        return 0, 0

    def calculate_average(self):
        p_tp, p_td = self._percents()
        tp = self._grades["tp"] or 0
        td = self._grades["td"] or 0
        exam = self._grades["exam"] or 0
        return (tp * p_tp + td * p_td + exam * self.evaluation_exam_percent) / 100

    def calculate_credits(self):
        return self.credit if self.calculate_average() >= self.PASS_MARK else 0