from module import Module
from unit import Unit
from semester import Semester


def build_semester1():
    s1 = Semester("S1", "Semestre 1")
    uef11 = Unit("UEF11", "UE Fondamentale 11", [
        Module("F111", "Réseaux des couches basses", 3, 6, 1.5, 1.5, 1.5),
        Module("F112", "Algorithmique Avancée et Complexité", 2, 4, 1.5, 0, 1.5),
    ])
    uef12 = Unit("UEF12", "UE Fondamentale 12", [
        Module("F121", "Système d'exploitation", 2, 4, 1.5, 1.5, 0),
        Module("F122", "Architectures Modernes des Systèmes Informatiques", 2, 4, 1.5, 0, 1.5),
    ])
    uem11 = Unit("UEM11", "UE Méthodologie", [
        Module("M111", "Architecture et administration des bases de données", 2, 4, 1.5, 0, 1.5),
        Module("M112", "Méthodes et Technologies d'Implémentation", 3, 5, 1.5, 0, 1.5),
    ])
    ued11 = Unit("UED11", "UE Découverte", [
        Module("D111", "Systèmes de Communication Vocaux et Vidéos", 2, 2, 1.5, 0, 1.5),
    ])
    uet11 = Unit("UET11", "UE Transversale", [
        Module("T111", "Cloud Computing", 1, 1, 1.5, 0, 0,
               teaching_mode="Distance", continous_percent=0, exam_percent=100),
    ])
    for u in (uef11, uef12, uem11, ued11, uet11):
        s1.add_unit(u)
    return s1


def build_semester2():
    s2 = Semester("S2", "Semestre 2")
    uef21 = Unit("UEF21", "UE Fondamentale 21", [
        Module("F211", "Les Middlewares pour les systèmes répartis", 3, 6, 1.5, 1.5, 1.5),
        Module("F212", "Modélisation et Architectures logicielles", 2, 4, 1.5, 0, 1.5),
    ])
    # NB: UF221 = 67.5h in the canvas => C + TD + TP = 1.5 each
    uef22 = Unit("UEF22", "UE Fondamentale 22", [
        Module("UF221", "Réseaux de la couche IP", 3, 6, 1.5, 1.5, 1.5),
        Module("UF222", "Introduction au Machine Learning", 2, 4, 1.5, 0, 1.5),
    ])
    uem21 = Unit("UEM21", "UE Méthodologique", [
        Module("M211", "Infographie", 2, 3, 1.5, 0, 1.5),
        Module("M212", "Gestion de l'incertain", 2, 3, 1.5, 1.5, 0),
    ])
    ued21 = Unit("UED21", "UE Découverte", [
        Module("D211", "Internet of Things", 2, 3, 1.5, 0, 1.5),
    ])
    uet21 = Unit("UET21", "UE Transversale", [
        Module("T211", "Cybercriminalité", 1, 1, 1.5, 0, 0,
               teaching_mode="Distance", continous_percent=0, exam_percent=100),
    ])
    for u in (uef21, uef22, uem21, ued21, uet21):
        s2.add_unit(u)
    return s2


def find_module(semester, code):
    for u in semester.units:
        for m in u.modules:
            if m.name == code:
                return m
    raise KeyError(code)


if __name__ == "__main__":
    s1 = build_semester1()

    # Example grades of one student (tp, td, exam)
    demo = {
        "F111": (12, 11, 10), "F112": (14, None, 9), "F121": (None, 10, 11),
        "F122": (13, None, 12), "M111": (15, None, 8), "M112": (10, None, 12),
        "D111": (12, None, 10), "T111": (None, None, 11),
    }
    for code, (tp, td, exam) in demo.items():
        find_module(s1, code).set_grade(tp=tp, td=td, exam=exam)

    print(find_module(s1, "M112").summary())
    print()
    print(s1.report())
    print(f"Total hours: {s1.total_hours}h | coef {s1.coef} | credits {s1.credit}")