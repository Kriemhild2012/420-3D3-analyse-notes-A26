from models.etudiant import Etudiant


class GroupeCours:
    def __init__(self, nom: str):
        self.nom = nom
        self.etudiants: list[Etudiant] = []

    def ajouter_etudiant(self, etudiant: Etudiant) -> None:
        self.etudiants.append(etudiant)

    def moyenne(self) -> float:
        if not self.etudiants:
            return 0.0
        return round(sum(e.moyenne() for e in self.etudiants) / len(self.etudiants), 1)

    def nb_etudiants(self) -> int:
        return len(self.etudiants)

    def to_dict(self) -> dict:
        return {
            "type": "groupecours",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [e.to_dict() for e in self.etudiants]
        }